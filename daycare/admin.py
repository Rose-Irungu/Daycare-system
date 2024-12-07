from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from daycare.models import Enrollment, ApprovedEnrollment, Event

# Register your models here.
admin.site.register(Enrollment)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('child_name', 'parent_name', 'age', 'gender')

@admin.register(ApprovedEnrollment)
class ApprovedEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'approved_date')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'location')
    search_fields = ['title']

admin.site.register(Event, EventAdmin)