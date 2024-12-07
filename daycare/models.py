from django.contrib import admin
from django.db import models

from django.db import models

class Enrollment(models.Model):
    parent_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    child_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0,)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    allergies = models.CharField(max_length=255)
    # approved = models.BooleanField(default=False)

    def __str__(self):
        return self.parent_name

class ApprovedEnrollment(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name='approved_enrollment')
    approved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Approved: {self.enrollment.child_name}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Babysitter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    qualifications = models.TextField()
    experience = models.PositiveIntegerField(help_text="Experience in years")
    availability = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='babysitters/', blank=True, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
@admin.register(Babysitter)
class BabysitterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'experience', 'availability', 'approved')
    list_filter = ('approved', 'availability')
    search_fields = ('name', 'email')
    actions = ['approve_babysitters']

    def approve_babysitters(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected babysitters have been approved.")

    approve_babysitters.short_description = "Approve selected babysitters"



