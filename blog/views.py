from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Users


# получение данных из бд
def index(request):
    user = Users.objects.all()
    return render(request, "index.html", {"user": user})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Users()
        tom.user = request.POST.get("user")
        tom.save()
    return HttpResponseRedirect("/")