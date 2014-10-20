from django.db import models
from datetime import datetime

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
    object_name = models.CharField(max_length=100)
    object_type = models.ForeignKey(ObjectType)
    def __unicode__(self):
        return self.object_name

class ActivityType(models.Model):
    type_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.type_name

"""
class Day(models.Model):
    date = models.DateField()
    def __unicode__(self):
        return self.date.strftime('%Y-%m-%d')
"""

class Activity(models.Model):
    activity_type = models.ForeignKey(ActivityType)
    act_object = models.ForeignKey(ActObject)
    day = models.DateField()
    hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    comment = models.CharField(max_length=400, null=True, blank=True)
    is_actif = models.BooleanField(default=True)

    class Meta:
        unique_together = ('activity_type', 'act_object', 'day')
    
    def __unicode__(self):        
        return self.activity_type.type_name + ' ' + self.act_object.object_name

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
