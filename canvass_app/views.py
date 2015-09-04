from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, loader
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            managerList = Manager.objects.filter(user = user)
            canvasserList = Canvasser.objects.filter(user = user)
            salesList = SalesPerson.objects.filter(user=user)
            if len(canvasserList) > 0:
                return HttpResponseRedirect("/index.html#view=canvasser")
            elif len(managerList) > 0:
                return HttpResponseRedirect("/index.html#view=manager")
            elif len(salesList)> 0:
                return HttpResponseRedirect("/index.html#view=salesPerson")
            else:
                return HttpResponseRedirect("/login.html")
    return HttpResponseRedirect("/login.html") #add hash #view=register


@csrf_exempt
def createUser(request):
    if request.POST:
        print(request.POST)
        user = User()
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.username = request.POST["username"]
        user.set_password(request.POST["password"])
        user.save()
        if request.POST["role"] == "canvasser":
            canvasser = Canvasser()
            canvasser.user = user
            canvasser.save()
            return HttpResponse("canvasser: " + str(canvasser.id) + ", user: " + str(user.id))
        elif request.POST["role"] == "salesPerson":
            sp = SalesPerson()
            sp.user = user
            sp.save()
        else:
            manager = Manager()
            manager.user = user
            manager.save()
            return HttpResponse("manager: "+ str(manager.id) + ", user: " + str(user.id))
    else:
        return HttpResponse("unable to create user")


# def canvasser_api(request):
#     if request.POST:
#         if request.POST[action = submit_lead]:
#             lead = Lead()
#
#         if request.Post[action = objection]:
#
#
#
# def post_rebuttal(request):
#     if request.POST:
#
#








