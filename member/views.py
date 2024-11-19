from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import SignupForm
from django.views.generic import DetailView, CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from contact.models import Profile





class UserRegisterView(generic.CreateView):
    form_class =  SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['bio', 'user_image']
    template_name = 'profile/profile_create.html'
    success_url = reverse_lazy('profile/profile_detail')  # Redirect to profile detail page after creation

    def form_valid(self, form):
        # Link the profile to the logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        # If the user already has a profile, redirect to profile detail page
        if Profile.objects.filter(user=request.user).exists():
            return redirect('profile_detail')
        return super().dispatch(request, *args, **kwargs)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # Check if profile exists; if not, create it
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['bio', 'user_image']
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('contact-list')

    def get_object(self, queryset=None):
        # Fetch the profile of the logged-in user
        return self.request.user.profile