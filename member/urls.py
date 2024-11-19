from django.urls import path
from .views import UserRegisterView,ProfileDetailView, ProfileCreateView, ProfileEditView

urlpatterns = [
   
path('register/', UserRegisterView.as_view(), name = 'register'),
path('profile/', ProfileDetailView.as_view(), name='profile_detail'),
path('profile/create/', ProfileCreateView.as_view(), name='profile_create'),
path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),



]
