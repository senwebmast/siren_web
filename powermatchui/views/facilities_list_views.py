from django.shortcuts import render
from ..models import facilities, Scenarios, ScenariosFacilities

def facilities_list(request):
    scenarios = Scenarios.objects.all()

    # Filter facilities by scenario
    selected_scenario = request.GET.get('scenario')
    if selected_scenario:
        scenario_obj = Scenarios.objects.get(idscenarios=selected_scenario)
        facility_ids = ScenariosFacilities.objects.filter(idscenarios=scenario_obj).values_list('idfacilities', flat=True)
        facs = facilities.objects.filter(idfacilities__in=facility_ids)
    else:
        facs = facilities.objects.all()

    context = {
        'facilities': facs,
        'scenarios': scenarios,
        'selected_scenario': int(selected_scenario) if selected_scenario else None,
    }
    return render(request, 'facilities_list.html', context)