from django.core.management.base import BaseCommand, CommandError
from lifeIsShort.models import 
from datetime import datetime

class Command(BaseCommand):
    help='Create the report after the given date '

    def add_arguments(self, parser):
        parser.add_argument('date_str', nargs='+', type=string)

    def handle(self, *args, **options):
        today = datetime.now().date()
        
        
        
