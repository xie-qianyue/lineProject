from django.shortcuts import render
from lifeIsShort.models import Day
from lifeIsShort.models import Activity
from lifeIsShort.models import ActivityType
from lifeIsShort.models import ActObject
from django.utils import timezone
import json
from django.http import HttpResponse
	
def index(request):	    
	activity_list = Activity.objects.all().filter(is_actif=True)
	activity_dict = {}
	"""
        activity_dict :
        key : activity_type
        value : a list of activity of this type, element in the list is a tuple
        tuple : (activity, day set of this activity(only the most recent date is present), flag indicate if the recent date == today)
        """
        for activity in activity_list:
                if activity.activity_type.type_name not in activity_dict:
                        activity_dict[activity.activity_type.type_name] = list()
                recent_date = activity.day_set.order_by('-date')[0].date
                today = timezone.now().date()
                is_today = False                
                if(recent_date == today):
                        is_today = True
                activity_dict[activity.activity_type.type_name].append((activity, recent_date, is_today))
	
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
                
