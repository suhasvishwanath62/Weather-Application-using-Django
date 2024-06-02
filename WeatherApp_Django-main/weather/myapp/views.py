from django.shortcuts import render
import json 
import urllib.request



# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['search']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8984ea30bf142e46a345eedb7f9734e4').read()
        json_data = json.loads(res)
        data = {
        'countrycode' : str(json_data['sys']['country']),
        'city' : str(json_data['name']),
        'temprature': str(json_data['main']['temp']),
        'humidity': str(json_data['main']['humidity'])
        }
    else:
        city = ""
        data = {}
    return render(request, "index.html", data)
