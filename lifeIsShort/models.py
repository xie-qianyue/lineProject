from django.db import models
from datetime import datetime
from lifeIsShort.util.TimeUnitEnum import TimeUnitEnum

class ObjectType(models.Model):
    type_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.type_name
		
class TypeLevelTwo(models.Model):
    type_name = models.CharField(max_length=50)
    father_type = models.ForeignKey(ObjectType, related_name='childrenTypes')
    def __unicode__(self):
        return self.type_name

class ActObject(models.Model):
    object_name = models.CharField(max_length=100, unique=True)
    object_type = models.ForeignKey(ObjectType)
    def __unicode__(self):
        return self.object_name

class ActivityType(models.Model):
    type_name = models.CharField(max_length=50, unique=True)
    def __unicode__(self):
        return self.type_name

class ActivityFrequency(models.Model):
    times = models.IntegerField()
    period = models.IntegerField()
    class Meta:
        unique_together = ('times', 'period')
    def __unicode__(self):
        return str(self.times) + " time(s) per " + TimeUnitEnum.get_time_unit_name(self.period)
        
class Activity(models.Model):
    activity_type = models.ForeignKey(ActivityType)
    act_object = models.ForeignKey(ActObject)
    comment = models.CharField(max_length=400, null=True, blank=True)
    act_frequency = models.ForeignKey(ActivityFrequency)
    is_actif = models.BooleanField(default=True)
    is_display_in_general_report = models.BooleanField(default=True)
    class Meta:
        unique_together = ('activity_type', 'act_object')    
    def __unicode__(self):        
        return self.activity_type.type_name + ' ' + self.act_object.object_name

class Day(models.Model):
    date = models.DateField()
    activity = models.ForeignKey(Activity)
    hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)    
    class Meta:
        unique_together = ('date', 'activity')
    def __unicode__(self):
        return self.date.strftime('%Y.%m.%d') + ' : ' + self.activity.__unicode__()

class GeneralViewReport(models.Model):
    date = models.DateField(unique=True)
    value = models.IntegerField()
    def __unicode__(self):
        return str(self.value) + " activity(s) on " + self.date.strftime('%Y.%m.%d')

"""
class BookType(models.Model):
    type_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.type_name

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_type = models.ForeignKey(BookType)
    def __unicode__(self):
        return self.book_name

class Reading(models.Model):
    book = models.ForeignKey(Book)
    date = models.DateField();

class Game(models.Model):
    game_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.game_name

class PlayingGame(models.Model):
    game = models.ForeignKey(game)
    date = models.DateField();
""" 
