from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from daycare.forms import EnrollmentForm

from django.shortcuts import render, redirect
from django.http import HttpResponse

from daycare.models import Enrollment, ApprovedEnrollment, Babysitter


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def babysitters(request):
    return render(request, 'babysitters.html')
def sarah_jonson(request):
    return render(request, 'sarah_jonson.html')
def james_lee(request):
    return render(request, 'james_lee.html')
def emily_carter(request):
    return render(request, 'emily_carter.html')


def book_sarah_modal(request):
    return render(request, 'book_sarah_modal.html')
# def enrollment(request):
#     form = EnrollmentForm()
#     return render(request, 'enrollment.html', {'form': form})


def programs(request):
    return render(request, 'programs.html')
def imara_mall_location(request):
    return render(request, 'imara_mall_location.html')
def westlands_location(request):
    return render(request, 'westlands_location.html')
def calendar (request):
    return render(request, 'calendar.html')
def menu (request):
    return render(request, 'menu.html')
def infant (request):
    return render(request, 'infant.html')


def toddler (request):
    return render(request, 'toddler.html')
def preschool (request):
    return render(request, 'preschool.html')
def extended (request):
    return render(request, 'extended.html')
def enrolled (request):
    data = Enrollment.objects.all()
    context = {'data': data}

    return render(request, 'enrolled.html', context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
# def approved(request):
#      enrollment = get_object_or_404(Enrollment, id=id)
#      if request.method == "POST":
#          form = EnrollmentForm(request.POST, request.FILES, instance=enrollment)
#          if form.is_valid():
#              form.save()
#      return redirect('approved')
#      return render(request, template_name='approved.html')
# # def enrollment(request):
#     if request.method == 'POST':
#         form = EnrollmentForm(request.POST)
#         # Process form data here
#         if form.is_valid():
#             form.save()
#             return redirect('infant')
#         else:
#             form = EnrollmentForm()
#         return render(request, 'enrollment.html', {'form': form})
        # parent_name = request.POST.get('parent_name')
        # email = request.POST.get('email')
        # phone = request.POST.get('phone')
        # child_name = request.POST.get('child_name')
        # age = request.POST.get('age')
        # gender = request.POST.get('gender')
        # dob = request.POST.get('dob')
        # allergies = request.POST.get('allergies')

        # Save to database or process logic
        # Example: print data to console (replace with actual logic)
        # print(parent_name, email, phone, child_name, age, gender, dob, allergies)

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Enrollment

def enrollment(request):
    if request.method == 'POST':
        # Handle form submission
        parent_name = request.POST.get('parent_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        child_name = request.POST.get('child_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        allergies = request.POST.get('allergies')

        # Save to database
        Enrollment.objects.create(
            parent_name=parent_name,
            email=email,
            phone=phone,
            child_name=child_name,
            age=age,
            gender=gender,
            dob=dob,
            allergies=allergies
        )
        return HttpResponse("Form submitted successfully")

    elif request.method == 'GET' and 'approve' in request.GET:
        # Handle approval
        enrollment_id = request.GET.get('approve')
        enrollment = get_object_or_404(Enrollment, id=enrollment_id)
        enrollment.approved = True
        enrollment.save()
        return redirect('enrollment')  # Replace with the appropriate URL name

    elif request.method == 'GET' and 'delete' in request.GET:
        # Handle deletion
        enrollment_id = request.GET.get('delete')
        enrollment = get_object_or_404(Enrollment, id=enrollment_id)
        enrollment.delete()
        return redirect('enrollment')  # Replace with the appropriate URL name

    # Fetch all enrollments to display
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment.html', {'enrollments': enrollments})


# def approved(request):
#     return render(request, 'approved.html')
# def approved(request, id):
#     enrollment = get_object_or_404(Enrollment, id=id)
#     enrollment.approved = True
#     enrollment.save()
#     messages.success(request, f"{enrollment.child_name} has been successfully approved.")
#     return redirect('programs')


def approved(request, id):
    enrollment = get_object_or_404(Enrollment, id=id)

    # Check if already approved
    if hasattr(enrollment, 'approved_enrollment'):
        messages.info(request, f"{enrollment.child_name} is already approved.")
    else:
        ApprovedEnrollment.objects.create(enrollment=enrollment)
        messages.success(request, f"{enrollment.child_name} has been successfully approved.")

    return redirect('programs')
# def approve_enrollment(request, enrollment_id):
#     enrollment = get_object_or_404(Enrollment, id=enrollment_id)
#     ApprovedEnrollment.objects.create(enrollment=enrollment)
#     return redirect('enrollment')
#
# def delete_approved(request, approved_id):
#     approved_enrollment = get_object_or_404(ApprovedEnrollment, id=approved_id)
#     approved_enrollment.delete()
#     return redirect('approved')
from django.shortcuts import render
from .models import Event

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})
def babysitters_list(request):
    babysitters = Babysitter.objects.filter(approved=True)
    return render(request, 'babysitters_list.html', {'babysitters': babysitters})

def approve_babysitter(request, id):
    babysitter = get_object_or_404(Babysitter, id=id)
    babysitter.approved = True
    babysitter.save()
    messages.success(request, f"{babysitter.name} has been approved.")
    return redirect('babysitters_list')