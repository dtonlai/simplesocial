from django.shortcuts import render
from django.urls imort reverse
from django.views import generic
from groups.models import Group,GroupMember
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequired,Mixin)

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields=('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
