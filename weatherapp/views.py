from django.shortcuts import render
import urllib.request
import json
from django.contrib import messages
# Create your views here.
def home(request):
    date = {'city': '',
            'country': '',
            'climate': '',
            'discp': '',
            'tempareture': '',
            }
    if request.method == 'POST':
        city = request.POST['search-bar']
        try:
            response = urllib.request.urlopen(
                f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=35f252b4310e24b2cb46776c332fb99e')
            json_response = json.load(response)
            date = {'city': city,
                    'country': json_response['sys']['country'],
                    'climate': json_response["weather"][0]['main'],
                    'discp': json_response["weather"][0]["description"],
                    'tempareture': json_response["main"]['temp'],
                    }
        except:
            messages.info(request,f"{city} doesn't exsist")
    return render(request, 'home.html',{'data':date})