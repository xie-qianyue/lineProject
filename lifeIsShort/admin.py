from django.contrib import admin
from lifeIsShort.models import ObjectType
from lifeIsShort.models import TypeLevelTwo
from lifeIsShort.models import ActObject
from lifeIsShort.models import ActivityType
from lifeIsShort.models import Activity
from lifeIsShort.models import Day

class ActObjectAdmin(admin.ModelAdmin):
    list_display = ('object_name', 'object_type')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('day', 'activity_type', 'act_object')

class DayAdmin(admin.ModelAdmin):
    list_display = ('date', 'activities')

admin.site.register(ObjectType)
admin.site.register(TypeLevelTwo)
admin.site.register(ActObject, ActObjectAdmin)
admin.site.register(ActivityType)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Day)
