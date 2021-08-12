from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import transaction

from .models import  News
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
    if request.method == "POST":
        title = request.POST.get("title", None)
        date = request.POST.get("date", None)
        time = request.POST.get("time", None)
        director = request.POST.get("director", None)
        image = request.POST.get("image", None)
        experience = request.POST.get("experience", None)
        
        with transaction.atomic():
            f = Filial(
                title = title,
                established_at = parse_date_time(date, time)
            )        
            f.save()

            d = Director(
                fullname = director,
                experience = experience,
                image = image,
                filial = f
                
            )
            d.save()

        return redirect(reverse("home"))

    context = {
        
    }
    return render(request, "simpleforms/create_director.html", context)


def update_director(request, pk):
    try:
        filial = Filial.objects.get(id=pk)
        date = filial.established_at.strftime("%Y-%m-%d")
        time = filial.established_at.strftime("%H:%M")
    except:
        return redirect(reverse("home"))

    if request.method == "POST":
        title = request.POST.get("title", None)
        date = request.POST.get("date", None)
        time = request.POST.get("time", None)
        director = request.POST.get("director", None)
        image = request.POST.get("image", None)
        experience = request.POST.get("experience", None)
        
        filial.title = title
        filial.established_at = parse_date_time(date, time)
        filial.director.fullname = director
        filial.director.image = image
        filial.director.experience = experience
        filial.save()
        filial.director.save()

        return redirect(reverse("home"))


    context = {
        "filial":filial,
        "date":date,
        "time":time
    }
    return render(request,"simpleforms/update_director.html", context)


def delete_director(request, pk):
    try:
        Filial.objects.get(id=pk).delete()
    except:
        pass
    return redirect(reverse("home"))




    

