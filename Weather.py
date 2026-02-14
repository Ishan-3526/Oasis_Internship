import requests
import sys

def get_weather():
    api_key = "4f1c9d141e6823a4585e56646d833cbc"

    city = input("Enter City Name  ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        print(response.status_code)
        print(response.text)

        if response.status_code == 200:

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]

            print("\nWeather Details")
            print("Temperature :", temp, "°C")
            print("Humidity :", humidity, "%")
            print("Condition :", condition)

        else:
            print("Error :", data["message"])

    except:
        print("Something Went Wrong While Fetching Data")

    try:
        ch = int(input("\n1 = Check Another City\n2 = Break\n= "))
    except:
        print("Invalid Input , Exiting")
        sys.exit(0)

    if ch == 1:
        get_weather()
    elif ch == 2:
        sys.exit(0)
    else:
        print("Wrong Choice , Exiting")
        sys.exit(0)


print("Weather App Program")

try:
    ch = int(input('''
1 = Check Weather
2 = Break

'''))
except:
    print("Invalid Input !! Terminating")
    sys.exit(0)

if ch == 1:
    get_weather()

elif ch == 2:
    sys.exit(0)

else:
    print("Wrong Input !! Terminating")