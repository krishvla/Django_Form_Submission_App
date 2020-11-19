from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MasterIncident


class Home(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        context = {}
        context['login'] = True
        return render(request, 'login.html', context)
    def post(self, request, *args, **kwargs):
        data = request.POST
        #Login Form
        user = authenticate(request, username=data['loginusername'], password=data['loginpassword'])
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Credentials Not Matched')
        return redirect('home')

class Register(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {}
        context['register'] = True
        return render(request, 'register.html', context)
    def post(self, request, *args, **kwargs):
        data = request.POST
        try:
            if not User.objects.filter(username=data['username']).exists():
                user_obj = User.objects.create_user(data['username'], data['email'], data['password'])
                # password = hashlib.sha256((data['password']).encode()).hexdigest()
                user_obj.first_name = data['firstname']
                user_obj.save()
                messages.success(request, 'Account Successfully Created, Please Login to Continue..')
            else:
                messages.error(request, 'Username is Taken, Please try with differnt one..')
                return redirect('home')
        except Exception as err:
            print(err)
            messages.error(request, 'Error Occured, Please try again..')
        return redirect('register')

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully, Logged out')
    return redirect('home')

class Dashboard(LoginRequiredMixin, TemplateView):
    login_url = 'home'
    def get(self, request, *args, **kwargs):
        context = {}
        context['dashboard'] = True
        return render(request, 'dashboard.html', context)
    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data.getlist('sub_incident_types', 'none'))
        print(data)
        try:
            incident_obj = MasterIncident()
            incident_obj.location = data['location']
            incident_obj.description = data['incident_description']
            incident_obj.date = data['incident_date']
            incident_obj.time = data['incident_time']
            incident_obj.incident_location = data['incident_location']
            incident_obj.initial_severity = data['initial_severity']
            incident_obj.suspected_cause = data['suspected_cause']
            incident_obj.actions_takem = data['actions_taken']
            incident_obj.sub_incident_types = ', '.join(data.getlist('sub_incident_types', 'none'))
            incident_obj.user = request.user
            incident_obj.save()
            messages.success(request, 'Successfully Reported.')
            return redirect('dashboard')
        except Exception as err:
            print(err)
            messages.error(request, 'Error Occured')
        
        return redirect('home')

class Incidents(LoginRequiredMixin, TemplateView):
    login_url = 'home'
    def get(self, request, *args, **kwargs):
        context = {}
        context['incidents'] = True
        context['incidents'] = MasterIncident.objects.filter(user = request.user)
        return render(request, 'incidents.html', context)
