from django.shortcuts import render



def register(request):
    if request.method == "POST":
        gmail = request.POST.get("gmail", None)
        password1 = request.POST.get("password1", None)
        password2 = request.POST.get("password2", None)

        if gmail and password1 == password2:
            print("ok")
        else:
            print("net")

    return render(request, "learning.html")