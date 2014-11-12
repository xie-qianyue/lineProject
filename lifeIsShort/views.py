from django.shortcuts import render
from lifeIsShort.models import Day
from lifeIsShort.models import Activity
from lifeIsShort.models import ActivityType
from lifeIsShort.models import ActObject
from lifeIsShort.models import GeneralViewReport
from lifeIsShort.util.MyDateUtil import MyDateUtil
from django.utils import timezone
from datetime import date
import json
from django.http import HttpResponse
	
def index(request):	    
	activity_list = Activity.objects.filter(is_actif=True)
	activity_dict = {}
	"""
	activity_dict :
    key : activity_type
    value : a list of activity of this type, element in the list is a tuple
    tuple : (activity, day set of this activity(only the most recent date is present), flag indicate if the recent date == today, flag indicate if the activity reaches the frequency)
    """
	for activity in activity_list:
		if activity.activity_type.type_name not in activity_dict:
			activity_dict[activity.activity_type.type_name] = list()
		recent_date = activity.day_set.order_by('-date')[0].date
		today = timezone.now().date()
		is_today = False                
		if(recent_date == today):
			is_today = True
		is_done = is_act_done(activity)
		# import pdb;pdb.set_trace()		
		activity_dict[activity.activity_type.type_name].append((activity, recent_date, is_today, is_done))
	
	# import pdb;pdb.set_trace()	
	context = {'activity_dict' : activity_dict
                   }
	return render(request, 'lifeIsShort/index.html', context)

def add_activity(request):
	response_data = {}
	if request.method == "POST":
		today = timezone.now()
		activity_type = request.POST.get("activity_type")            
		activity_type_model = ActivityType.objects.get(type_name=activity_type)
		activity_object = request.POST.get("activity_object")             
		act_object_model = ActObject.objects.get(object_name=activity_object)             
		activity_model = Activity.objects.get(activity_type=activity_type_model, act_object=act_object_model)
		
		day = Day(date=today, activity=activity_model)
		day.save()
		
		today_string = today.strftime("%Y.%m.%d")
		response_data["result"] = "OK"
		response_data["today"] = today_string
                response_data["is_done"] = is_act_done(activity_model)
                
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		response_data["result"] = "KO"
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)

def get_general_report(request):
	today = timezone.now().date()
	first_day_year = date(today.year,1,1)	
	report_list = GeneralViewReport.objects.filter(date__gt=first_day_year)
	
	response_data = {}
	# import pdb;pdb.set_trace()
	for report in report_list:		
		date_in_second = (report.date-date(1970,1,1)).total_seconds()
		response_data[date_in_second] = report.value
		
	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
	)

def get_nb_times_act_by_period(activity):
	'''
	get number of times of an activity
	this method may be moved somewhere else
	'''
	today = timezone.now().date()
	period = activity.act_frequency.period
	first_day, last_day = MyDateUtil.get_first_and_last_day(today, period)
	# import pdb;pdb.set_trace()
	return Day.objects.filter(activity=activity, date__gte=first_day, date__lte=last_day).count()

def is_act_done(activity):
        '''
        check whether the activity has reached the frequency
        this method may be moved somewhere else
        '''
	is_done = False
	if(get_nb_times_act_by_period(activity) >= activity.act_frequency.times):
		is_done = True
	return is_done
