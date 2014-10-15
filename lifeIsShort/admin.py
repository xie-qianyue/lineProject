from django.contrib import admin
from lifeIsShort.models import ObjectType
from lifeIsShort.models import TypeLevelTwo
from lifeIsShort.models import ActObject
from lifeIsShort.models import ActivityType
from lifeIsShort.models import Activity

class ActObjectAdmin(admin.ModelAdmin):
    list_display = ('object_name', 'object_type')

admin.site.register(ObjectType)
admin.site.register(TypeLevelTwo)
admin.site.register(ActObject, ActObjectAdmin)
admin.site.register(ActivityType)
admin.site.register(Activity)
