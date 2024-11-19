from django.urls import path
from.views import home_view
from.views import AddContactView, ContactListView, DeleteContactView,ContactDetailView, ContactupdateView

urlpatterns = [
   path('', home_view, name='home'),
   path('contact/', ContactListView.as_view(), name='contact-list'),
   path("add_contact/", AddContactView.as_view(), name = 'add-contact' ), 
   path("contact/<int:pk>",ContactDetailView.as_view(), name = 'contact-detail'),
   path("contact/<int:pk>/remove", DeleteContactView.as_view(), name = 'contact-delete' ),
   path("contact/edit/<int:pk>", ContactupdateView.as_view(), name = 'contact-update'),







]
