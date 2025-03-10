import logging

from django.shortcuts import render, redirect
from django.views import View

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
            return redirect('login')
        return render(request, 'users/create.html', {'form': form})


class UserFormEditView(View):
    '''.'''
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = CustomUserForm(instance=user)
        return render(request, 'users/update.html', {'form': form, 'user_id': user_id})


    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')        
        return render(request, 'users/update.html', {'form': form, 'user_id': user_id})


class UserFormDeleteView(View):
    '''.'''
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = CustomUserForm(instance=user)
        return render(
            request,
            'users/delete.html',
            {
                'form': form,
                'user': user,
                'user_id': user_id
            }
        )


    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users')
