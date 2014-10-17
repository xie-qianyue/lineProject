from django.shortcuts import render
from lifeIsShort.models import Day


def index(request):
    day_list = Day.objects.all()
    """
    for day in day_list
        activity_list = day.activities.all()
    """
    context = {'day_list' : day_list}   
    return render(request, 'lifeIsShort/index.html', context)
    


