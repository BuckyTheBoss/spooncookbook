from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import User, Profile
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.


class Signup(CreateView):
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('update_profile')
    template_name = 'create.html'
    extra_context = {'item_type': 'User', 'form_type': 'Create'}

    def form_valid(self, form):
        self.object = form.save()
        user = authenticate(self.request, username=self.object.username, password=form.cleaned_data['password1'])
        if user:
            login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())


class UpdateProfile(UpdateView):
    model = Profile
    fields = ['phone', 'address', 'image']
    success_url = '/'
    template_name = 'create.html'
    extra_context = {'item_type': 'Profile', 'form_type': 'Update'}

    def get_object(self, queryset=None):
        return self.request.user.profile
