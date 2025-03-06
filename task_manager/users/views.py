from django.shortcuts import render, redirect
from django.views import View

# from django.http import HttpResponse
# from django.views.generic import (
#     CreateView,
#     DeleteView,
#     DetailView,
#     ListView,
#     TemplateView,
#     UpdateView
# )
# 1 use model, form_class, template_name in default views

# 2 realize mixins
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView

from django.template import RequestContext

from .models import CustomUser
from .forms import CustomUserForm


class IndexView(View):
    '''View for listing users.'''
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserFormCreateView(View):
    '''.'''
    def get(self, request, *args, **kwargs):
        form = CustomUserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # to /login/ page
        return render(request, 'users/create.html', {'form': form})


# # STUDY EXAMPLES
# # recommended way
# class SmthStuffFormView(View):

#     def post(self, request, *args, **kwargs):
#         form = SmthStuffForm(request.POST)
#         if form.is_valid():
#             # form.save(commit=False) # save data
#             pass

# # naive way
# class DoSmthView(View):

#     # for POST method
#     def post(self, request, *args, **kwargs):
#         form = DoSmthForm(request.POST)
#         if form.is_valid():
#             pass
    
#     # for GET method
#     def get(self, request, *args, **kwargs):
#         form = DoSmthForm()


# class SmthCreateView(LoginRequiredMixin, CreateView):
#     '''MIXIN example.'''
#     model = User
#     fields = ['name']

#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)


# class IndexUsers(ListView):
#     '''Mixin example.'''
#     model = User
#     context_object_name = 'users'
#     # extra_context = {'title': _('Users')} # ? 

#     # mixin example
#     def get(self, request, *args, **kwargs):
#         users = User.objects.all[:15]
#         return render(request, 'users/index.html', context={
#             'users': users,
#         })

