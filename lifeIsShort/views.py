from django.shortcuts import render
# from lifeIsShort.models import Day
from lifeIsShort.models import Activity
	
def index(request):
	    
	activity_list = Activity.objects.all().filter(is_actif=True)
	#import pdb;pdb.set_trace()	
	context = {'activity_list' : activity_list}
	return render(request, 'lifeIsShort/index.html', context)
