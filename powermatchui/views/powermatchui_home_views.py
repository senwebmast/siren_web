from django.views.generic import TemplateView

class PowerPlotHomeView(TemplateView):
    template_name = 'powermatchui_home'


# homes_views.py
from decimal import Decimal
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import path
from ..forms import DemandYearScenario, RunPowermatchForm
from siren_web.database_operations import fetch_demand_data, fetch_scenarios_data, fetch_settings_data,  fetch_full_generator_storage_data
from siren_web.models import Demand
from powermatchui.powermatch.pmcore import Facility, Optimisation, PM_Facility, powerMatch
from powermatchui.views.exec_powermatch import submit_powermatch

@login_required
def powermatchui_home(request):
    demand_year = request.session.get('demand_year', '')  # Get demand_year and scenario from session or default to empty string
    scenario= request.session.get('scenario', '')
    success_message = ""
    if request.method == 'POST':
        # Handle form submission
        demand_year_scenario = DemandYearScenario(request.POST)
        if demand_year_scenario.is_valid():
            demand_year = demand_year_scenario.cleaned_data['demand_year']
            request.session['demand_year'] = demand_year
            scenario = demand_year_scenario.cleaned_data['scenario']
            request.session['scenario'] = scenario # Assuming scenario is an instance of Scenarios
            success_message = "Settings updated."
    demand_year_scenario = DemandYearScenario()
    runpowermatch_form = RunPowermatchForm()

    context = {
        'demand_year_scenario': demand_year_scenario, 'runpowermatch_form': runpowermatch_form,
        'success_message': success_message, 'demand_year': demand_year, 'scenario': scenario
        }
    return render(request, 'powermatchui_home.html', context)

def run_powermatch(request):
    demand_year = request.session.get('demand_year', '')  # Get demand_year and scenario from session or default to empty string
    scenario= request.session.get('scenario', '')
    success_message = ""
    if request.method == 'POST':
        runpowermatch_form = RunPowermatchForm(request.POST)
        if not demand_year:
            success_message = "Set the demand year and scenario first."
        elif runpowermatch_form.is_valid():
            level_of_detail = runpowermatch_form.cleaned_data['level_of_detail']
            option = level_of_detail[0]
            sp_output, headers, sp_pts = submit_powermatch(demand_year, scenario, option, 1, None)
            sp_data = []
            for row in sp_output:
                formatted_row = []
                for item in row:
                    if isinstance(item, Decimal):
                        formatted_row.append('{:,.2f}'.format(item))
                    else:
                        formatted_row.append(item)
                sp_data.append(formatted_row)

            context = {
                'sp_data': sp_data, 'headers': headers, 'sp_pts': sp_pts,
                'success_message': success_message, 'demand_year': demand_year, 'scenario': scenario
            }
            return render(request, 'display_table.html', context)
        else:
            demand_year_scenario = DemandYearScenario()
            runpowermatch_form = RunPowermatchForm()
        context = {
            'demand_year_scenario': demand_year_scenario,'runpowermatch_form': runpowermatch_form,
            'success_message': success_message, 'demand_year': demand_year, 'scenario': scenario
            }
        return render(request, 'powermatchui_home.html', context)
            
def start_powermatch_task(request):
    # Start the Celery task asynchronously
    task = run_powermatch_task.delay(settings, generators, demand_year, option, pmss_details, pmss_data, re_order, dispatch_order, pm_data_file, data_file)
    return JsonResponse({'task_id': task.id})

def get_task_progress(request, task_id):
    # Get progress of the Celery task
    task = run_powermatch_task.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        return JsonResponse({'progress': 100, 'message': 'Task completed successfully'})
    elif task.state == 'FAILURE':
        return JsonResponse({'progress': 0, 'message': 'Task failed'})
    else:
        # Get task progress from task.info dictionary (if available)
        progress = task.info.get('progress', 0)
        message = task.info.get('message', 'Task in progress')
        return JsonResponse({'progress': progress, 'message': message})