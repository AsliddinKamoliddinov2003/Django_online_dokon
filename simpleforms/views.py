from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import transaction

from .models import  *
from .forms import *
from .utils import parse_date_time



def index(request):
    news = News.objects.all()
    context = {
        "news": news
    }
    return render(request,"simpleforms/list.html", context)


def create(request):
    form = NewsForm()

    if request.method=="POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("news-list"))


    context = {
        "form":form
    }

    return render(request,"simpleforms/create.html",context)


def update(request, pk):
    news = News.objects.filter(id=pk)

    if not news.exists():
        return redirect(reverse("news-list"))
    else:
        news = news.first()

    form = NewsForm(instance=news)

    if request.method=="POST":
        news = NewsForm(request.POST, request.FILES, instance = news)
        if news.is_valid():
            news.save()
            return redirect(reverse("news-list"))

    context = {
        "form":form
    }

    return render(request,"simpleforms/update.html", context)


def delete(request, pk):
    try:
        news = News.objects.get(id=pk)
        news.delete()
    except News.DoesNotExist:
        pass
    return redirect(reverse("news-list"))


def home(request):
    filials = Filial.objects.all()
    context = {
        "filials":filials
    }
    return render(request, "simpleforms/home.html", context)


def create_director(request):
    director_form = DirectorForm()
    filial_form = FilialForm()

    if request.method == "POST":
        director_form = DirectorForm(request.POST, request.FILES)
        filial_form = FilialForm(request.POST)

        if director_form.is_valid() and  filial_form.is_valid():
            filial = filial_form.save(commit=False)
            director = director_form.save(commit=False)

            director.filial = filial

            filial.save()
            director.save()
      
            return redirect(reverse("home"))


    context = {
        "filial_form":filial_form,
        "director_form":director_form
    }
    return render(request, "simpleforms/create_director.html", context)


def update_director(request, pk):
    try:
        filial = Filial.objects.get(id=pk)
    except:
        return redirect(reverse("home"))

    
    director_form = DirectorForm(instance=filial.director)
    filial_form = FilialForm(instance=filial)

    if request.method=="POST":
        director_form = DirectorForm(request.POST, instance=filial.director)
        filial_form = FilialForm(request.POST,instance=filial)

        if director_form.is_valid() and  filial_form.is_valid():
            filial = filial_form.save(commit=False)
            director = director_form.save(commit=False)

            director.filial = filial

            filial.save()
            director.save()
      
            return redirect(reverse("home"))



    context = {
        "director_form":director_form,
        "filial_form":filial_form
    }
    return render(request,"simpleforms/update_director.html", context)


def delete_director(request, pk):
    try:
        Filial.objects.get(id=pk).delete()
    except:
        pass
    return redirect(reverse("home"))




    

