from django.shortcuts import render
# from lifeIsShort.models import Day
from lifeIsShort.models import Activity
	
def index(request):
	    
	activity_list = Activity.objects.all().filter(is_actif=True)

	activity_dict = {}
        for activity in activity_list:
                if activity.activity_type.type_name not in activity_dict:
                        activity_dict[activity.activity_type.type_name] = list()
                activity_dict[activity.activity_type.type_name].append(activity)
	
	# import pdb;pdb.set_trace()	
	context = {'activity_dict' : activity_dict
                   }
	return render(request, 'lifeIsShort/index.html', context)
