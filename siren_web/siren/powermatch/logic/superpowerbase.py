#!/usr/bin/python3
#
#  Copyright (C) 2015-2023 Sustainable Energy Now Inc., Angus King
#
#  superpower.py - This file is part of SIREN.
#
#  SIREN is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of
#  the License, or (at your option) any later version.
#
#  SIREN is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General
#  Public License along with SIREN.  If not, see
#  <http://www.gnu.org/licenses/>.
#

from math import asin, ceil, cos, fabs, pow, radians, sin, sqrt
import os
import siren_web.siren.utilities.ssc as ssc
import time
from siren_web.siren.utilities.senutils import techClean, extrapolateWind, WorkBook
from siren_web.siren.powermatch.logic.powerclassesbase import *
# import Station
from siren_web.siren.powermap.logic.turbinebase import TurbineBase as Turbine

import tempfile # for wind extrapolate

the_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class SuperPowerBase():

    def haversine(self, lat1, lon1, lat2, lon2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
   #     convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = list(map(radians, [lon1, lat1, lon2, lat2]))

   #     haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))

   #     6367 km is the radius of the Earth
        km = 6367 * c
        return km

    def find_closest(self, latitude, longitude, wind=False):
        dist = 99999
        closest = ''
        if wind:
            filetype = ['.srw']
            technology = 'wind_index'
            index_file = self.wind_index
            folder = self.wind_files
        else:
            filetype = ['.csv', '.smw']
            technology = 'solar_index'
            index_file = self.solar_index
            folder = self.solar_files
        if index_file == '':
            fils = os.listdir(folder)
            for fil in fils:
                if fil[-4:] in filetype:
                    bit = fil.split('_')
                    if bit[-1][:4] == self.base_year:
                        dist1 = self.haversine(float(bit[-3]), float(bit[-2]), latitude, longitude)
                        if dist1 < dist:
                            closest = fil
                            dist = dist1
        else:
            fils = []
            if self.default_files[technology] is None:
                dft_file = index_file
                if os.path.exists(dft_file):
                    pass
                else:
                    dft_file = folder + '/' + index_file
                if os.path.exists(dft_file):
                    self.default_files[technology] = WorkBook()
                    self.default_files[technology].open_workbook(dft_file, )
                else:
                    return closest
            var = {}
            worksheet = self.default_files[technology].sheet_by_index(0)
            num_rows = worksheet.nrows - 1
            num_cols = worksheet.ncols - 1
#           get column names
            curr_col = -1
            while curr_col < num_cols:
                curr_col += 1
                var[worksheet.cell_value(0, curr_col)] = curr_col
            curr_row = 0
            while curr_row < num_rows:
                curr_row += 1
                lat = worksheet.cell_value(curr_row, var['Latitude'])
                lon = worksheet.cell_value(curr_row, var['Longitude'])
                fil = worksheet.cell_value(curr_row, var['Filename'])
                fils.append([lat, lon, fil])
            for fil in fils:
                dist1 = self.haversine(fil[0], fil[1], latitude, longitude)
                if dist1 < dist:
                    closest = fil[2]
                    dist = dist1
        if __name__ == '__main__':
            print(closest)
        return closest

    def do_defaults(self, station):
        if 'PV' in station.technology:
            technology = 'PV'
        elif 'Wind' in station.technology:
            technology = 'Wind'
        else:
            technology = station.technology
        if self.default_files[technology] is None:
            dft_file = self.variable_files + '/' + self.defaults[technology]
            if os.path.exists(dft_file):
                self.default_files[technology] = WorkBook()
                self.default_files[technology].open_workbook(dft_file)
            else:
                return
        var = {}
        worksheet = self.default_files[technology].sheet_by_index(0)
        num_rows = worksheet.nrows - 1
        num_cols = worksheet.ncols - 1
#       get column names
        curr_col = -1
        while curr_col < num_cols:
            curr_col += 1
            var[worksheet.cell_value(0, curr_col)] = curr_col
        curr_row = 0
        while curr_row < num_rows:
            curr_row += 1
            if (worksheet.cell_value(curr_row, var['TYPE']) == 'SSC_INPUT' or \
              worksheet.cell_value(curr_row, var['TYPE']) == 'SSC_INOUT') and \
              worksheet.cell_value(curr_row, var['DEFAULT']) != '' and \
              str(worksheet.cell_value(curr_row, var['DEFAULT'])).lower() != 'input':
                if worksheet.cell_value(curr_row, var['DATA']) == 'SSC_STRING':
                    self.data.set_string(worksheet.cell_value(curr_row, var['NAME']).encode('utf-8'),
                      worksheet.cell_value(curr_row, var['DEFAULT']).encode('utf-8'))
                elif worksheet.cell_value(curr_row, var['DATA']) == 'SSC_ARRAY':
                    arry = split_array(worksheet.cell_value(curr_row, var['DEFAULT']))
                    self.data.set_array(worksheet.cell_value(curr_row, var['NAME']).encode('utf-8'), arry)
                elif worksheet.cell_value(curr_row, var['DATA']) == 'SSC_NUMBER':
                    if isinstance(worksheet.cell_value(curr_row, var['DEFAULT']), float):
                        self.data.set_number(worksheet.cell_value(curr_row, var['NAME']).encode('utf-8'),
                          float(worksheet.cell_value(curr_row, var['DEFAULT'])))
                    else:
                        self.data.set_number(worksheet.cell_value(curr_row, var['NAME']).encode('utf-8'),
                          worksheet.cell_value(curr_row, int(var['DEFAULT'])))
                elif worksheet.cell_value(curr_row, var['DATA']) == 'SSC_MATRIX':
                    mtrx = split_matrix(worksheet.cell_value(curr_row, var['DEFAULT']))
                    self.data.set_matrix(worksheet.cell_value(curr_row, var['NAME']).encode('utf-8'), mtrx)

    def debug_sam(self, name, tech, module, data, status):
        data_typs = ['invalid', 'string', 'number', 'array', 'matrix', 'table']
        var_typs = ['?', 'input', 'output', 'inout']
        var_names = []
        ssc_info = ssc.Info(module)
        while ssc_info.get():
            var_names.append([ssc_info.name(), ssc_info.var_type(), ssc_info.data_type()])
        if status:
            status.log('SAM Variable list for ' + tech + ' - ' + name)
        else:
            print('SAM Variable list for ' + tech + ' - ' + name)
        var_names = sorted(var_names, key=lambda s: s[0].lower())
        info = []
        for fld in var_names:
            msg = fld[0].decode() + ',' + var_typs[fld[1]] + ',' + data_typs[fld[2]] + ','
            if fld[2] == 1:
                msg += data.get_string(fld[0]).decode()
            elif fld[2] == 2:
                msg += str(data.get_number(fld[0]))
            elif fld[2] == 3:
                dat = data.get_array(fld[0])
                if len(dat) == 0:
                    msg += '"[]"'
                else:
                    msg += '"['
                    stop = len(dat)
                    if stop > 12:
                        fin = '...] ' + str(stop) + ' items in total"'
                        stop = 13
                    else:
                        fin = ']"'
                    for i in range(stop):
                        msg += str(dat[i]) + ','
                    msg = msg[:-1]
                    msg += fin
            elif fld[2] == 4:
                msg += str(len(data.get_matrix(fld[0]))) + ' entries'
            info.append(msg)
        if status:
            for msg in info:
                status.log2(msg)
            status.log('Variable list complete for ' + tech + ' - ' + name)
        else:
            for msg in info:
                print(msg)
            print('Variable list complete for ' + tech + ' - ' + name)
        return

    def __init__(self, config, stations, demand_year=None, scenario_settings=None):
        self.config = config
        self.stations = stations
        self.power_summary = []
        self.base_year = demand_year
        self.biomass_multiplier = scenario_settings.get('Biomass multiplier', 8.25)
        try:
            resource = scenario_settings.get('Geothermal resource', None)
            if resource.lower()[0:1] == 'hy':
                self.geo_res = 0
            else:
                self.geo_res = 1
        except:
            self.geo_res = 0
        self.pv_dc_ac_ratio = [1.1] * 5
        self.pv_dc_ac_ratio = [float(scenario_settings.get('PV dc_ac_ratio', None))] * 5
        self.pv_dc_ac_ratio[0] = float(scenario_settings.get('Fixed PV dc_ac_ratio', 0))
        self.pv_dc_ac_ratio[1] = float(scenario_settings.get('Rooftop PV dc_ac_ratio', 0))
        self.pv_dc_ac_ratio[2] = float(scenario_settings.get('Single Axis PV dc_ac_ratio', 0))
        self.pv_dc_ac_ratio[3] = float(scenario_settings.get('Backtrack PV dc_ac_ratio', 0))
        self.pv_dc_ac_ratio[4] = float(scenario_settings.get('Tracking PV dc_ac_ratio', 0))
        self.pv_dc_ac_ratio[4] = float(scenario_settings.get('Dual Axis PV dc_ac_ratio', 0))
        self.pv_losses = float(scenario_settings.get('PV losses', 0))
        self.wave_cutout = float(scenario_settings.get('Wave cutout', 0))
        wf = scenario_settings.get('Wave efficiency', 0)
        if wf:
            if wf[-1] == '%':
                self.wave_efficiency = float(wf[-1]) / 100.
            else:
                self.wave_efficiency = float(wf)
            if self.wave_efficiency > 1:
                self.wave_efficiency = self.wave_efficiency / 100.
        self.wind_turbine_spacing = [8, 8] # onshore and offshore winds
        self.wind_row_spacing = [8, 8]
        self.wind_offset_spacing = [4, 4]
        self.wind_farm_losses_percent = [2, 2]
        self.wind_hub_formula = [None, None]
        self.wind_hub_spread = [None, None]
        self.wind_law = ['l', 'l']
        self.wind_turbine_spacing[0] = int(float(scenario_settings.get('Wind turbine_spacing', None)))
        self.wind_row_spacing[0] = int(float(scenario_settings.get('Wind row_spacing', None)))
        self.wind_offset_spacing[0] = int(float(scenario_settings.get('Wind offset_spacing', None)))
        self.wind_farm_losses_percent[0] = int(float(scenario_settings.get('Wind wind_farm_losses_percent', None).strip('%')))
        self.wind_law[0] = scenario_settings.get('Wind extrapolate , None')
        self.wind_hub_formula[0] = scenario_settings.get('Wind hub_formula , None')
        self.wind_hub_spread[0] = int(float(scenario_settings.get('Wind hub_spread', 0)))
        self.st_gross_net = float(scenario_settings.get('Solar Thermal gross_net', 0.87))
        self.st_tshours = float(scenario_settings.get('Solar Thermal tshours', 0))
        self.st_volume = float(scenario_settings.get('Solar Thermal volume', 12.9858))
        self.cst_gross_net = float(scenario_settings.get('CST gross_net', 0.87))
        self.cst_tshours = float(scenario_settings.get('CST tshours', 0))
        self.hydro_cf = float(scenario_settings.get('Hydro cf', 0.33))
        self.actual_power = scenario_settings.get('Files actual_power', None)
        if self.actual_power:
            self.actual_power = self.actual_power.replace('$YEAR$', self.base_year)
        self.solar_files = scenario_settings.get('Files solar_files', None)
        self.solar_files = self.solar_files.replace('$YEAR$', self.base_year)
        self.solar_index = scenario_settings.get('Files solar_index', None)
        self.solar_index = self.solar_index.replace('$YEAR$', self.base_year)
        self.wind_files = scenario_settings.get('Files wind_files', None)
        self.wind_files = self.wind_files.replace('$YEAR$', self.base_year)
        self.wind_index = scenario_settings.get('Files wind_index', None)
        self.variable_files = scenario_settings.get('Files variable_files', None)
        self.defaults = {}
        self.default_files = {}
        modules = scenario_settings.get('SAM Modules', None)
        pairs = modules.split()
        defaults = [tuple(pair.split('=')) for pair in pairs]
        for tech, default in defaults:
            if '_variables' in tech:
                tec = tech.replace('_variables', '')
                tec = techClean(tec)
                self.defaults[tec] = default
                self.default_files[tec] = None
            elif tech == 'helio_positions':
                self.default_files['helio_positions'] = default
                self.defaults['helio_positions'] = None
            elif tech == 'optical_table':
                self.default_files['optical_table'] = default
                self.defaults['optical_table'] = None
        self.default_files['solar_index'] = None
        self.default_files['wind_index'] = None
        self.default_files['actual'] = None
        subs_loss = scenario_settings.get('Grid substation_loss', None)
        if subs_loss[-1] == '%':
            self.grid_subs_loss = float(subs_loss[:-1]) / 100.
        else:
            self.grid_subs_loss = float(subs_loss) / 10.
        line_loss = scenario_settings.get('Grid line_loss', None)
        if line_loss[-1] == '%':
            self.grid_line_loss = float(line_loss[:-1]) / 100000.
        else:
            self.grid_line_loss = float(line_loss) / 1000.
        self.gen_pct = None
        ssc_api = ssc.API()

    def getPower(self):
        self.x = []
        self.stored = []
        self.ly = {}
        len_x = 8760
        for i in range(len_x):
            self.x.append(i)
        self.ly['Generation'] = []
        for i in range(len_x):
            self.ly['Generation'].append(0.)
        self.getPowerLoop()

    def getPowerLoop(self):
        self.all_done = False
        to_do = []
        for st in range(len(self.stations)):
            to_do.append(st)
        for st in range(len(to_do)):
  #      for st in range(len(self.stations)):
            stn = self.stations[to_do[st]]
            key = stn.name
            power = self.getStationPower(stn)
            total_power = 0.
            total_energy = 0.
            if power is None:
                pass
            else:
                if key in self.ly:
                    pass
                else:
                    self.ly[key] = []
                    for i in range(len(self.x)):
                        self.ly[key].append(0.)
                for i in range(len(power)):
                    if stn.grid_path_len is not None:
                        enrgy = power[i] * (1 - self.grid_line_loss * stn.grid_path_len - self.grid_subs_loss)
                    else:
                        enrgy = power[i] * (1 - self.grid_subs_loss)
                    self.ly[key][i] += enrgy / 1000.
                    total_energy += enrgy / 1000.
                    self.ly['Generation'][i] += power[i] / 1000.
                    total_power += power[i] / 1000.
            if total_energy > 0:
                pt = PowerSummary(stn.name, stn.technology, total_power, stn.capacity, total_energy)
            else:
                pt = PowerSummary(stn.name, stn.technology, total_power, stn.capacity)
            self.power_summary.append(pt)

    def getStationPower(self, station):
        def do_module(modname, station, field):
            module = ssc.Module(modname.encode('utf-8'))
            if (module.exec_(self.data)):
                farmpwr = self.data.get_array(field.encode('utf-8'))
                del module
                return farmpwr
            else:
                idx = 0
                msg = module.log(idx)
                while (msg is not None):
                    print(modname + ' error [', idx, ' ]: ', msg.decode())
                    idx += 1
                    msg = module.log(idx)
                del module
                return None

        if station.capacity == 0:
            return None
        self.data = None
        self.data = ssc.Data()
        farmpwr = [] # just in case
        if 'Wind' in station.technology:
            if 'Off' in station.technology: # offshore?
                wtyp = 1
            else:
                wtyp = 0
            closest = self.find_closest(station.lat, station.lon, wind=True)
            turbine = Turbine(self.config, station.turbine)
            if not hasattr(turbine, 'capacity'):
                return None
            wind_file = self.wind_files + '/' + closest
            hub_hght = 0
            if self.wind_hub_formula[wtyp] is not None: # if a hub height is specified
                formula = self.wind_hub_formula[wtyp].replace('rotor', str(turbine.rotor))
                try:
                    hub_hght = eval(formula)
                except:
                    pass
            temp_file = None
            if hub_hght > 0: # if a hub height is specified
                try:
                    wind_data = extrapolateWind(self.wind_files + '/' + closest, hub_hght, law=self.wind_law[wtyp],
                                spread=self.wind_hub_spread[wtyp])
                    if wind_data is not None:
                        temp_dir = tempfile.gettempdir()
                        temp_file = 'windfile.srw'
                        wf = open(temp_dir + '/' + temp_file, 'w')
                        for line in wind_data:
                            wf.write(line)
                        wf.close()
                        wind_file = temp_dir + '/' + temp_file
                except:
                    pass
            self.data.set_string(b'wind_resource_filename', wind_file.encode('utf-8'))
            no_turbines = int(station.no_turbines)
            if station.scenario == 'Existing' and (no_turbines * turbine.capacity) != (station.capacity * 1000):
                loss = round(1. - (station.capacity * 1000) / (no_turbines * turbine.capacity), 2)
                loss = loss * 100
                if loss < self.wind_farm_losses_percent[wtyp]:
                    loss = self.wind_farm_losses_percent[wtyp]
                self.data.set_number(b'system_capacity', station.capacity * 1000000)
                self.data.set_number(b'wind_farm_losses_percent', loss)
            else:
                self.data.set_number(b'system_capacity', no_turbines * turbine.capacity * 1000)
                self.data.set_number(b'wind_farm_losses_percent', self.wind_farm_losses_percent[wtyp])
            pc_wind = turbine.speeds
            pc_power = turbine.powers
            self.data.set_array(b'wind_turbine_powercurve_windspeeds', pc_wind)
            self.data.set_array(b'wind_turbine_powercurve_powerout', pc_power)
            t_rows = int(ceil(sqrt(no_turbines)))
            ctr = no_turbines
            wt_x = []
            wt_y = []
            for r in range(t_rows):
                for c in range(t_rows):
                    wt_x.append(r * self.wind_row_spacing[wtyp] * turbine.rotor)
                    wt_y.append(c * self.wind_turbine_spacing[wtyp] * turbine.rotor +
                                (r % 2) * self.wind_offset_spacing[wtyp] * turbine.rotor)
                    ctr -= 1
                    if ctr < 1:
                        break
                if ctr < 1:
                    break
            self.data.set_array(b'wind_farm_xCoordinates', wt_x)
            self.data.set_array(b'wind_farm_yCoordinates', wt_y)
            self.data.set_number(b'wind_turbine_rotor_diameter', turbine.rotor)
            self.data.set_number(b'wind_turbine_cutin', turbine.cutin)
            try:
                if station.hub_height > 0:
                    self.data.set_number(b'wind_turbine_hub_ht', station.hub_height)
            except:
                if hub_hght > 0:
                    self.data.set_number(b'wind_turbine_hub_ht', hub_hght)
            self.do_defaults(station)
            farmpwr = do_module('windpower', station, 'gen')
            if temp_file is not None: # if a hub height is specified
                try:
                    os.remove(temp_dir + '/' + temp_file)
                except:
                    pass
            return farmpwr
        elif station.technology == 'CST':
            closest = self.find_closest(station.lat, station.lon)
            base_capacity = 104.
            self.data.set_string(b'file_name', (self.solar_files + '/' + closest).encode('utf-8'))
            self.data.set_number(b'system_capacity', int(base_capacity * 1000))
            self.data.set_number(b'w_des', base_capacity / self.cst_gross_net)
            self.data.set_number(b'latitude', station.lat)
            self.data.set_number(b'longitude', station.lon)
            self.data.set_number(b'timezone', int(round(station.lon / 15.)))
            if station.storage_hours is None:
                tshours = self.cst_tshours
            else:
                tshours = station.storage_hours
            self.data.set_number(b'hrs_tes', tshours)
            sched = [[1] * 24] * 12
            self.data.set_matrix(b'weekday_schedule', sched[:])
            self.data.set_matrix(b'weekend_schedule', sched[:])
            if self.defaults['optical_table'] is None:
                optic_file = self.variable_files + '/' + self.default_files['optical_table']
                if not os.path.exists(optic_file):
                    return
                self.defaults['optical_table'] = []
                hf = open(optic_file)
                lines = hf.readlines()
                hf.close()
                for line in lines:
                    row = []
                    bits = line.split(',')
                    for bit in bits:
                        row.append(float(bit))
                    self.defaults['optical_table'].append(row)
                del lines
            self.data.set_matrix(b'OpticalTable', self.defaults['optical_table'][:])
            self.do_defaults(station)
            farmpwr = do_module('tcsgeneric_solar', station, 'gen')
            if farmpwr is not None:
                if station.capacity != base_capacity:
                    for i in range(len(farmpwr)):
                        farmpwr[i] = farmpwr[i] * station.capacity / float(base_capacity)
            return farmpwr
        elif station.technology == 'Solar Thermal':
            closest = self.find_closest(station.lat, station.lon)
            base_capacity = 104
            self.data.set_string(b'solar_resource_file', (self.solar_files + '/' + closest).encode('utf-8'))
            self.data.set_number(b'system_capacity', base_capacity * 1000)
            self.data.set_number(b'P_ref', base_capacity / self.st_gross_net)
            if station.storage_hours is None:
                tshours = self.st_tshours
            else:
                tshours = station.storage_hours
            self.data.set_number(b'tshours', tshours)
            sched = [[1.] * 24] * 12
            self.data.set_matrix(b'weekday_schedule', sched[:])
            self.data.set_matrix(b'weekend_schedule', sched[:])
            if ssc.API().version() >= 159:
                self.data.set_matrix(b'dispatch_sched_weekday', sched[:])
                self.data.set_matrix(b'dispatch_sched_weekend', sched[:])
                if ssc.API().version() >= 206:
                    self.data.set_number(b'gross_net_conversion_factor', self.st_gross_net)
                    if self.defaults['helio_positions'] is None:
                        helio_file = self.variable_files + '/' + self.default_files['helio_positions']
                        if not os.path.exists(helio_file):
                            return
                        self.defaults['helio_positions'] = []
                        hf = open(helio_file)
                        lines = hf.readlines()
                        hf.close()
                        for line in lines:
                            row = []
                            bits = line.split(',')
                            for bit in bits:
                                row.append(float(bit))
                            self.defaults['helio_positions'].append(row)
                        del lines
                    self.data.set_matrix(b'helio_positions', self.defaults['helio_positions'][:])
            else:
                self.data.set_number(b'Design_power', base_capacity / self.st_gross_net)
                self.data.set_number(b'W_pb_design', base_capacity / self.st_gross_net)
                vol_tank = base_capacity * tshours * self.st_volume
                self.data.set_number(b'vol_tank', vol_tank)
                f_tc_cold = self.data.get_number(b'f_tc_cold')
                V_tank_hot_ini = vol_tank * (1. - f_tc_cold)
                self.data.set_number(b'V_tank_hot_ini', V_tank_hot_ini)
            self.do_defaults(station)
            farmpwr = do_module('tcsmolten_salt', station, 'gen')
            if farmpwr is not None:
                if station.capacity != base_capacity:
                    for i in range(len(farmpwr)):
                        farmpwr[i] = farmpwr[i] * station.capacity / float(base_capacity)
            return farmpwr
        elif 'PV' in station.technology:
            closest = self.find_closest(station.lat, station.lon)
            self.data.set_string(b'solar_resource_file', (self.solar_files + '/' + closest).encode('utf-8'))
            dc_ac_ratio = self.pv_dc_ac_ratio[0]
            if station.technology[:5] == 'Fixed':
                dc_ac_ratio = self.pv_dc_ac_ratio[0]
                self.data.set_number(b'array_type', 0)
            elif station.technology[:7] == 'Rooftop':
                dc_ac_ratio = self.pv_dc_ac_ratio[1]
                self.data.set_number(b'array_type', 1)
            elif station.technology[:11] == 'Single Axis':
                dc_ac_ratio = self.pv_dc_ac_ratio[2]
                self.data.set_number(b'array_type', 2)
            elif station.technology[:9] == 'Backtrack':
                dc_ac_ratio = self.pv_dc_ac_ratio[3]
                self.data.set_number(b'array_type', 3)
            elif station.technology[:8] == 'Tracking' or station.technology[:9] == 'Dual Axis':
                dc_ac_ratio = self.pv_dc_ac_ratio[4]
                self.data.set_number(b'array_type', 4)
            self.data.set_number(b'system_capacity', station.capacity * 1000 * dc_ac_ratio)
            self.data.set_number(b'dc_ac_ratio', dc_ac_ratio)
            try:
                self.data.set_number(b'tilt', fabs(station.tilt))
            except:
                self.data.set_number(b'tilt', fabs(station.lat))
            if float(station.lat) < 0:
                azi = 0
            else:
                azi = 180
            if station.direction is not None:
                if isinstance(station.direction, int):
                    if station.direction >= 0 and station.direction <= 360:
                        azi = station.direction
                else:
                    dirns = {'N': 0, 'NNE': 23, 'NE': 45, 'ENE': 68, 'E': 90, 'ESE': 113,
                             'SE': 135, 'SSE': 157, 'S': 180, 'SSW': 203, 'SW': 225,
                             'WSW': 248, 'W': 270, 'WNW': 293, 'NW': 315, 'NNW': 338}
                    try:
                        azi = dirns[station.direction]
                    except:
                        pass
            self.data.set_number(b'azimuth', azi)
            self.data.set_number(b'losses', self.pv_losses)
            self.do_defaults(station)
            farmpwr = do_module('pvwattsv5', station, 'gen')
            return farmpwr
        elif station.technology == 'Biomass':
            closest = self.find_closest(station.lat, station.lon)
            self.data.set_string(b'file_name', (self.solar_files + '/' + closest).encode('utf-8'))
            self.data.set_number(b'system_capacity', station.capacity * 1000)
            self.data.set_number(b'biopwr.plant.nameplate', station.capacity * 1000)
            feedstock = station.capacity * 1000 * self.biomass_multiplier
            self.data.set_number(b'biopwr.feedstock.total', feedstock)
            self.data.set_number(b'biopwr.feedstock.total_biomass', feedstock)
            carbon_pct = self.data.get_number(b'biopwr.feedstock.total_biomass_c')
            self.data.set_number(b'biopwr.feedstock.total_c', feedstock * carbon_pct / 100.)
            self.do_defaults(station)
            farmpwr = do_module('biomass', station, 'gen')
            return farmpwr
        elif station.technology == 'Geothermal':
            closest = self.find_closest(station.lat, station.lon)
            self.data.set_string(b'file_name', (self.solar_files + '/' + closest).encode('utf-8'))
            self.data.set_number(b'nameplate', station.capacity * 1000)
            self.data.set_number(b'resource_potential', station.capacity * 10.)
            self.data.set_number(b'resource_type', self.geo_res)
            self.data.set_string(b'hybrid_dispatch_schedule', ('1' * 24 * 12).encode('utf-8'))
            self.do_defaults(station)
            pwr = do_module('geothermal', station, 'monthly_energy')
            if pwr is not None:
                farmpwr = []
                for i in range(12):
                    for j in range(the_days[i] * 24):
                        farmpwr.append(pwr[i] / (the_days[i] * 24))
                return farmpwr
            else:
                return None
        elif station.technology == 'Hydro':   # fudge Hydro purely by Capacity Factor
            pwr = station.capacity * 1000 * self.hydro_cf
            for hr in range(8760):
                farmpwr.append(pwr)
            return farmpwr
        elif station.technology == 'Wave':   # fudge Wave using 10m wind speed
            closest = self.find_closest(station.lat, station.lon)
            tf = open(self.solar_files + '/' + closest, 'r')
            lines = tf.readlines()
            tf.close()
            fst_row = len(lines) - 8760
            wnd_col = 4
            for i in range(fst_row, len(lines)):
                bits = lines[i].split(',')
                if float(bits[wnd_col]) == 0:
                    farmpwr.append(0.)
                else:
                    wave_height = 0.0070104 * pow(float(bits[wnd_col]) * 1.94384, 2)   # 0.023 * 0.3048 = 0.0070104 ft to metres
                    if self.wave_cutout > 0 and wave_height > self.wave_cutout:
                        farmpwr.append(0.)
                    else:
                        wave_period = 0.45 * float(bits[wnd_col]) * 1.94384
                        wave_pwr = pow(wave_height, 2) * wave_period * self.wave_efficiency
                        if wave_pwr > 1.:
                            wave_pwr = 1.
                        pwr = station.capacity * 1000 * wave_pwr
                        farmpwr.append(pwr)
            return farmpwr
        elif station.technology[:5] == 'Other':
            props = []
            propty = {}
            wnd50 = False
            try:
                for key, value in props:
                    propty[key] = value
                closest = self.find_closest(station.lat, station.lon)
                tf = open(self.solar_files + '/' + closest, 'r')
                lines = tf.readlines()
                tf.close()
                fst_row = len(lines) - 8760
                if closest[-4:] == '.smw':
                    dhi_col = 9
                    dni_col = 8
                    ghi_col = 7
                    tmp_col = 0
                    wnd_col = 4
                elif closest[-10:] == '(TMY2).csv' or closest[-10:] == '(TMY3).csv' \
                  or closest[-10:] == '(INTL).csv' or closest[-4:] == '.csv':
                    cols = lines[fst_row - 1].strip().split(',')
                    for i in range(len(cols)):
                        if cols[i].lower() in ['df', 'dhi', 'diffuse', 'diffuse horizontal',
                                               'diffuse horizontal irradiance']:
                            dhi_col = i
                        elif cols[i].lower() in ['dn', 'dni', 'beam', 'direct normal',
                                                 'direct normal irradiance']:
                            dni_col = i
                        elif cols[i].lower() in ['gh', 'ghi', 'global', 'global horizontal',
                                                 'global horizontal irradiance']:
                            ghi_col = i
                        elif cols[i].lower() in ['temp', 'tdry']:
                            tmp_col = i
                        elif cols[i].lower() in ['wspd', 'wind speed']:
                            wnd_col = i
                formula = propty['formula']
                operators = '+-*/%'
                for i in range(len(operators)):
                    formula = formula.replace(operators[i], ' ' + operators[i] + ' ')
                formula.replace(' /  / ', ' // ')
                formula.replace(' *  * ', ' ** ')
                propty['formula'] = formula
                if formula.find('wind50') >= 0:
                    closest = self.find_closest(station.lat, station.lon, wind=True)
                    tf = open(self.wind_files + '/' + closest, 'r')
                    wlines = tf.readlines()
                    tf.close()
                    if closest[-4:] == '.srw':
                        units = wlines[3].strip().split(',')
                        heights = wlines[4].strip().split(',')
                        for j in range(len(units)):
                            if units[j] == 'm/s':
                               if heights[j] == '50':
                                   wnd50_col = j
                                   break
                    fst_wrow = len(wlines) - 8760
                    wnd50_row = fst_wrow - fst_row
                    wnd50 = True
                for i in range(fst_row, len(lines)):
                    bits = lines[i].strip().split(',')
                    if wnd50:
                        bits2 = wlines[i + wnd50_row].strip().split(',')
                    formulb = propty['formula'].lower().split()
                    formula = ''
                    for form in formulb:
                        if form == 'dhi':
                            formula += bits[dhi_col]
                        elif form == 'dni':
                            formula += bits[dni_col]
                        elif form == 'ghi':
                            formula += bits[ghi_col]
                        elif form == 'temp':
                            formula += bits[tmp_col]
                        elif form == 'wind':
                            formula += bits[wnd_col]
                        elif form == 'wind50':
                            formula += bits2[wnd50_col]
                        else:
                            for key in list(propty.keys()):
                                if form == key:
                                    formula += propty[key]
                                    break
                            else:
                                formula += form
                        formula += ''
                    try:
                        pwr = eval(formula)
                        if pwr > 1:
                            pwr = 1.
                    except:
                        pwr = 0.
                    pwr = station.capacity * 1000 * pwr
                    farmpwr.append(pwr)
            except:
                pass
            return farmpwr
        else:
            return None

    def getValues(self):
        return self.power_summary

    def getPct(self):
        return self.gen_pct

    def getLy(self):
        try:
            return self.ly, self.x
        except:
            return None, None

    def getStnOuts(self):
        return self.stn_outs, self.stn_tech, self.stn_size, self.stn_pows, self.stn_grid, self.stn_path

    def getStnTech(self):
        return self.stn_outs, self.stn_tech

    def getStnPows(self):
        return self.stn_outs, self.stn_pows

    def getVisual(self):
        return self.model.getVisual()