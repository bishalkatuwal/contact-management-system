from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from.models import Contact
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


#def contactlist_view(request):
    #return render(request, 'contact_list.html')

class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  
        return context

    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user)
        query = self.request.GET.get('query')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(contact_number__icontains=query) |
                Q(email__icontains=query)
            )    

        return queryset

class AddContactView(LoginRequiredMixin, CreateView):

    model = Contact
    form_class = ContactForm
    template_name = 'add_contact.html'
    success_url = reverse_lazy('contact-list')  # Redirect to contact list or any desired page

    def form_valid(self, form):

        form.instance.user = self.request.user  # Set the logged-in user
        return super().form_valid(form)



class DeleteContactView(DeleteView):
    model = Contact
    template_name = 'delete_contact.html'
    success_url = reverse_lazy('home')
    


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    
    def get_context_data(self ,  *args, **kwargs):
        context = super(ContactDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Contact, id = self.kwargs['pk'])
        context['user'] = self.request.user  
        return context



class ContactupdateView(UpdateView):
    model = Contact
    template_name = 'contact_update.html'
    fields = ['profile_image' , 'name', 'contact_number', 'email']