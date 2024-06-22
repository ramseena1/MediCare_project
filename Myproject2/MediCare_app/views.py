from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib import messages

from MediCare_app.forms import user_Registration, patient_RegForm, doctor_RegForm


def Home_page(request):
    return render(request,'Home_page.html')

def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            print("<<<<<<<",1)
            login(request, user)
            return redirect('Home_page')
        elif user is not None and user.is_patient:
            print("<<<<<<<", 2)
            login(request, user)
            return redirect('Home_page')
        elif user is not None and user.is_doctor:
            print("<<<<<<<", 3)
            if user.doctor.Approve_status == 1:
                login(request, user)
                return redirect('Home_page')
        messages.info(request, "patient registered successfully")
    return render(request,'Login_page.html')


def redirect(param):
    pass


def Patient_Register_page(request):
    p_form=patient_RegForm()
    u_form=user_Registration()
    if request.method=='POST':
        p_form = patient_RegForm(request.POST)
        u_form = user_Registration(request.POST)
        if p_form.is_valid() and u_form.is_valid():
            user=u_form.save(commit=False)
            user.is_patient=True
            user.save()
            patient=p_form.save(commit=False)
            patient.user=user
            patient.save()
            messages.info(request, "patient registered successfully")
            return redirect('Login_page')
    return render(request,'Register_page.html',{'p_form':p_form,'u_form':u_form})



def Doctor_registration_page(request):
    d_form = doctor_RegForm()
    u_form = user_Registration()
    if request.method=='POST':
        d_form = doctor_RegForm(request.POST,request.FILES)
        u_form = user_Registration(request.POST)
        if d_form.is_valid() and u_form.is_valid:
            user=u_form.save(commit=False)
            user.is_doctor=True
            user.save()
            doctor=d_form.save(commit=False)
            doctor.user=user
            doctor.save()
            messages.info(request, "patient registered successfully")
            return redirect('Login_page')

    return render(request,'Doctor_registration.html',{'d_form':d_form,'u_form':u_form})


# Create your views here.
