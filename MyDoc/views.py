from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, _get_queryset, get_list_or_404, redirect
from django.views import View
from django.views.generic import CreateView

from .forms import *
from .models import *

from django.contrib.auth import login, authenticate, logout, admin


# Create your views here.


def index(request):
    contact = Contact.objects.all()

    appointment = Appointment.objects.all()

    dct = Doctor.objects.all()

    context = {
        'contact': contact,

        'appointment': appointment,

        'doctors': dct,
    }

    return render(request, 'MyDoc/index.html', context)


def doc_ndex(request):
    dct = Doctor.objects.all()
    context = {
        'doctors': dct
    }
    return render(request, 'MyDoc/doc_ndex.html', context)


def consultation(request):
    return render(request, 'MyDoc/consultation.html')


@login_required(login_url='MyDoc:login_patient')
def appointment(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        appnt = form.save(commit=False)
        appnt.name = request.POST['name']
        appnt.subject = request.POST['subject']
        appnt.number = request.POST['number']
        appnt.email = request.POST['email']
        appnt.message = request.POST['message']
        appnt.save()
        messages.success(request, f'Your appointment has been booked. Check your messages '
                                  f'tab after a while for instructions')
    form = AppointmentForm()
    return render(request, 'MyDoc/appointment.html', {'form': form})


def appnt_detail(request, appointment_id):
    u_appointment = get_object_or_404(UserAppointment, pk=appointment_id)
    return render(request, 'MyDoc/appnt_detail.html', {'u_appointment': u_appointment})


@login_required(login_url='MyDoc:login_patient')
def u_appointment(request):
    u_appointment = UserAppointment.objects.all().filter(user=request.user)
    context = {
        'u_appointment': u_appointment
    }
    return render(request, 'MyDoc/my_appnts.html', context)


def delete_appnt_detal(request, appointment_id):
    u_a = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'MyDoc/patient_confirm_delete.html', {'u_a': u_a})


def delete_appnt(request, appointment_id):
    u_a = UserAppointment.objects.get(pk=appointment_id)
    u_a.delete()
    messages.warning(request, f'Your appointment was deleted')
    u_a = UserAppointment.objects.all()
    return render(request, 'MyDoc/patient_confirm_delete.html', {'u_a': u_a})


@login_required(login_url='MyDoc:login_patient')
def message(request):
    mess = Message.objects.all().filter(to=request.user)
    context = {
        'message': mess
    }
    return render(request, 'MyDoc/message.html', context)


@login_required(login_url='MyDoc:login_patient')
def recept(request):
    recept = Recept.objects.all().filter(user=request.user)
    context = {
        'recept': recept
    }
    return render(request, 'MyDoc/receept.html', context)


def delete_mess(request, mess_id):
    mess = Message.objects.get(pk=mess_id)
    mess.delete()
    mess = Message.objects.all()
    return render(request, 'MyDoc/message.html', {'mess': mess})


def doctors(request):
    dct = Doctor.objects.all()
    context = {
        'doctors': dct
    }
    return render(request, 'MyDoc/doctors.html', context)


def patient_profile(request, user):
    form = PatientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = request.POST['username']
        user.image = request.POST['image']
        user.age = request.POST['age']
        user.gender = request.POST['gender']
        user.email = request.POST['email']
        user.contact = request.POST['contact']
        user.blood_type = request.POST['blood_type']
        user.height_cm = request.POST['height_cm']
        user.weight_kg = request.POST['weight_kg']
        user.user = request.user
        user.save()
        return render(request, 'MyDoc/my_profile.html', {'user': user})
    form = PatientForm()
    return render(request, 'MyDoc/profile_update.html', {'form': form})


def patient(request):
    form = PatientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = request.POST['username']
        user.image = request.FILES['image']
        user.age = request.POST['age']
        user.gender = request.POST['gender']
        user.email = request.POST['email']
        user.contact = request.POST['contact']
        user.blood_type = request.POST['blood_type']
        user.birth_date = request.POST['birth_date']
        user.residence = request.POST['residence']
        user.languages = request.POST['languages']
        user.health_insurance = request.POST['health_insurance']
        user.height_cm = request.POST['height_cm']
        user.weight_kg = request.POST['weight_kg']
        user.user = request.user
        user.save()
        messages.success(request, f'Welcome to Denvers Hospital')
        return redirect('MyDoc:my_profile')
    form = PatientForm()
    return render(request, 'MyDoc/patient.html', {'form': form})


def detail(request, pat_id):
    patient = get_object_or_404(Patient, pk=pat_id)
    return render(request, 'MyDoc/detail_pat.html', {'patient': patient})


def med_detal(request):
    medrecs = Medrecs.objects.all()
    context = {
        'medrecs': medrecs
        }
    return render(request, 'MyDoc/med_users.html', context)

""" medrecs = Medrecs.objects.all().filter(doctor__doctor_name=request.user, user__patient__medrecs__in=pat_id)
 """

def my_appnts(request):
    meds = Medrecs.objects.all().filter(user=request.user)
    return render(request, 'MyDoc/med_users.html', {'meds': meds})


def my_profile(request):
    if request.user.is_authenticated:
        meds = Medrecs.objects.all().filter(user=request.user)
        return render(request, 'MyDoc/my_profile.html', {'meds': meds})
    else:
        return redirect('MyDoc:login_patient')


def profile_update(request):
    if request.method == 'POST':
        u_update = UserUpdate(request.POST, instance=request.user)
        p_update = ProfileUpdate(request.POST, request.FILES or None, instance=request.user.patient)
        if u_update.is_valid() and p_update.is_valid():
            u_update.save()
            p_update.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('MyDoc:my_profile')
    else:
        u_update = UserUpdate(instance=request.user)
        p_update = ProfileUpdate(instance=request.user.patient)
    context = {
        'u_update': u_update,
        'p_update': p_update
    }

    return render(request, 'MyDoc/profile_update.html', context)


def medrecs(request):
    meds = Medrecs.objects.all()
    return render(request, 'MyDoc/Department.html', {'meds': meds})


@login_required(login_url='MyDoc:login_admn')
def all_patients(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient
    }
    return render(request, 'MyDoc/all_patients.html', context)


def login_admn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        admin = authenticate(username=username, password=password)
        if admin is not None:
            if admin.is_staff and admin.is_active:
               login(request, admin)
               return redirect('MyDoc:all_patients')
    return render(request, 'MyDoc/sign-in.html')


def delete_pat(request, pat_id):
    patient = Patient.objects.get(pk=pat_id)
    patient.delete()
    patient = Patient.objects.all()
    return render(request, 'MyDoc/all_patients.html', {'patient': patient})


def register_patient(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        user.set_password(password1)
        user.save()
        user = authenticate(username=username, password=password1, first_name=first_name, last_name=last_name,
                            email=email)
        if user is not None:
            if user.is_active:
                messages.success(request, f'Registration Successful. You will be logging'
                                          f' in as {user.username} Complete Patient Registration')
                login(request, user)
                return redirect('MyDoc:patient')
    return render(request, 'MyDoc/register.html', {'form': form})


def login_patient(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user.patient:
                messages.success(request, f'Login Successful. You are logged in as {user.username}')
                login(request, user)
                return redirect('MyDoc:my_profile')
            else:
                messages.error(request, 'You are an Admin. This is the patients site')
                return redirect('MyDoc:all_patients')
        else:
            messages.error(request, 'INVALID LOGIN TRY AGAIN!!')
    return render(request, 'MyDoc/sign-in.html')


def logout_patient(request):
    logout(request)
    return redirect('MyDoc:index')


def contact(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        mes = form.save(commit=False)
        mes.name = request.POST['name']
        mes.email = request.POST['email']
        mes.subject = request.POST['subject']
        mes.message = request.POST['message']
        mes.save()
    form = ContactForm()
    return render(request, 'MyDoc/contact.html', {'form': form})


"""On Production Level the user sde"""
