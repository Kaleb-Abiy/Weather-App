from django.shortcuts import render
import requests


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f042661b84ea04dcad1725192bbe296e'
    if request.method == 'POST':
        city = request.POST['city']
        r = requests.get(url.format(city)).json()
        main = r['main']['temp']
        desc = r['weather'][0]['description']
        icon = r['weather'][0]['icon']
        country = r['sys']['country'].lower()
        print(country)
    else:
        return render(request, 'index.html')    
        
        
    return render(request, 'index.html', {'main': main, 'desc':desc, 'icon':icon, 'country':country, 'city':city})
