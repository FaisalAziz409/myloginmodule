import requests
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from.models import Signup, Weather

# Create your views here.

def index(request):
    return render(request,"index.html")


def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        address2=request.POST['address2']
        state=request.POST['state']
        city=request.POST['city']
        zip=request.POST['zip']

        user=User.objects.create_user(username=email, password=password, email=email)
        user.save()
        users = Signup(email=email, address=address, password=password, address1=address2, state=state, city=city, zip=zip)
        users.save()

        return render(request, "index.html", {"login": "successfully logged in"})

    else:
        return render(request, "index.html")


def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]

        user = auth.authenticate(request=request,username=email, password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"login.html",{"login":"succesfully logged"})
        else:
            return render(request, "weather.html")
    else:
        return render(request, "login.html",{"error":"invalid"})


def weather(request):
    if request.method=="GET":
        city_name=request.GET.get("city")
        cities = Weather(city=city_name)
        cities.save()
        cities = Weather.objects.all()
        context = []
        for i in cities:
            url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=90c20e3f513e5e32ad20bb4d5992b351".format(i)
            r = requests.get(url)
            r = r.json()
            city_weathers={
                "city":i,
                "temperature":r["main"]["temp"],
                "description":r['weather'][0]['description'],
                "icon":r['weather'][0]['icon']
            }
            context.append(city_weathers)
        return render(request,"weather.html",{"city_weathers":context})
    else:
        return render(request,"weather.html")






