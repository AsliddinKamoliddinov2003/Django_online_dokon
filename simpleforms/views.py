from django.shortcuts import redirect, render
from django.urls import reverse


from .models import Category, News



def index(request):
    news = News.objects.all()
    context = {
        "news": news
    }
    return render(request,"simpleforms/list.html", context)



def create(request):
    if request.method == "POST":
        title = request.POST.get("title", None)
        content = request.POST.get("content", None)
        category_id = request.POST.get("category_id", None)

        category = Category.objects.get(id=category_id)

        n = News()
        n.title = title
        n.content = content
        n.category = category

        n.save()
        return redirect(reverse("news-list"))

    categories = Category.objects.all()
    context = {
        "categories": categories
    }

    return render(request,"simpleforms/create.html",context)



def update(request, pk):
    news = News.objects.filter(id=pk)

    if not news.exists():
        return redirect(reverse("news-list"))
    else:
        news = news.first()


    if request.method == "POST":
        title = request.POST.get("title", None)
        content = request.POST.get("content", None)
        category_id = request.POST.get("category_id", None)

        category = Category.objects.get(id=category_id)

        news.title = title
        news.content = content
        news.category = category

        news.save()
        return redirect(reverse("news-list"))

    categories = Category.objects.all()
    context = {
        "categories": categories,
        "news":news
    }

    return render(request,"simpleforms/update.html", context)

def delete(request, pk):
    try:
        news = News.objects.get(id=pk)
        news.delete()
    except News.DoesNotExist:
        pass
    return redirect(reverse("news-list"))

    

