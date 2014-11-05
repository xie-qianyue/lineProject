from django.core.management.base import BaseCommand, CommandError
from lifeIsShort.models import Day
from lifeIsShort.models import GeneralViewReport 
from datetime import datetime

class Command(BaseCommand):
    help='Create the report after the given date '

    def handle(self, *args, **options):
        aDay = datetime.strptime(args[0], '%Y%m%d')
	# import pdb; pdb.set_trace()
	day_list = Day.objects.filter(date__gt=aDay).filter(activity__is_display_in_general_report=True)
	"""
	We build a dictionary as a middle model bewteen the list and the db model 
	"""
	day_dict = {}
	for day in day_list:
	    date = day.date
	    if date not in day_dict:
		day_dict[date] = 1
	    else:
                day_dict[date] += 1        
	for date, value in day_dict.iteritems():
	    report, created = GeneralViewReport.objects.get_or_create(date=date, defaults={'value': value})
	    # import pdb; pdb.set_trace()
	    report.value = value
	    report.save()
        
        
        
