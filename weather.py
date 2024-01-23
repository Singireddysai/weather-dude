import requests

####### getting ip for finding location
city=None
ip_adress=None
weather_data=None
output="city not found"

def get_ip():
    try:
        ipresponse=requests.get('https://api64.ipify.org?format=json')
        if(ipresponse.status_code==200):
            global ip_adress
            ip_adress=ipresponse.json()['ip']
        else:
            print(f'failed to get ip status code:{ipresponse.status_code}')
    except Exception as e:
        print(f'Exception occurred:{e}')
        
get_ip()
#################### getting location details - city using ipbase
def locateme():
    get_ip()
    geolocation_url='https://api.ipbase.com/v2/info'
    ipbase_api_key='ipb_live_9BOwR6uGOyiiQXGACAjp3AZrpWDsFTszoGSknjW9'
    params={'ip':ip_adress,
            'key':ipbase_api_key}
    try:
        response=requests.get(geolocation_url,params=params)
        if(response.status_code==200):
            global city
            city=response.json()['data']['location']['city']['name']
            lat=response.json()['data']['location']['latitude']
            lon=response.json()['data']['location']['longitude']
            country=response.json()['data']['location']['country']['name']
            return f'Right now your ip adress is at \n{city} of {country}\n lat:{lat} \nlon:{lon}' 
        else:
            print(f"error:{response.status_code}-{response.text}")
    except Exception as e:
        print(f'Exception Occurred:{e}')
        


############## getting weather details using openwheathermap 

def getweather(city):
    global output
    output="city not found"
    weather_url='https://api.openweathermap.org/data/2.5/weather'
    appid='ca25a4b63ba77afd0a2a8dc0751a144d'
    weather_params={'appid':appid,
                    'q':city,
                    'units':'metric'}

    try:
        weather_response=requests.get(weather_url,weather_params)
        if(weather_response.status_code==200):
            global weather_data 
            weather_data=weather_response.json()
            output=""
        else:
            print(f'error occurred:{weather_response.status_code}-{weather_response.text}')
            
    except Exception as e:
        print(f'exception occurred:{e}')


description=None
temp=None
mintemp=None
maxtemp=None
feelslike=None
humidity=None
visibility=None
timezone=None
windspeed=None
lon=None
lat=None
country=None
main=None
def weather_details():
    getweather(city=city)
    global temp
    temp=weather_data['main']['temp']
    global mintemp
    mintemp=weather_data['main']['temp_min']
    global maxtemp
    maxtemp=weather_data['main']['temp_max']
    global feelslike
    feelslike=weather_data['main']['feels_like']
    global humidity
    humidity=weather_data['main']['humidity']
    global visibility
    visibility=weather_data['visibility']
    global timezone
    timezone=weather_data['timezone']
    global windspeed
    windspeed=weather_data['wind']['speed']
    global description
    description=weather_data['weather'][0]['description']
    global lon
    lon=weather_data['coord']['lon']
    global lat
    lat=weather_data['coord']['lat']
    global country
    country=weather_data['sys']['country']
    global main
    main=weather_data['weather'][0]['main']
