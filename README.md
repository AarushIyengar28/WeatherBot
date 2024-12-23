# WeatherBot
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"] 
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        user_input = input('Do you want the units to be farenheit or celcius?: ')
        temp_faren = temperature * 9/5 + 32
        if user_input == 'Farenheit'.lower():
            return f'The weather in {city} is {description} with a temperature of {temp_faren}°F and a humidity of {humidity}%'
        if user_input == 'Celcius'.lower():
            return f'The weather in {city} is {description} with a temperature of {temperature}°C and a humidity of {humidity}%'
        else:
            print("Check your spelling on celcius or farenheit")
    
    elif response.status_code == 404:

        
        return 'Im sorry, I could not get the weather data. Please check if you entered the city name correctly.'

    else:
        return 'There was an error. Please try one of the earlier steps again'
        


def chatbot():
    api_key = "26a76bccd81472b820fdd972993d1c8b"
    print('Hi, I am a WeatherBot. Ask me about a location\'s weather or type Exit to quit the chatbot')
    
    while True:  
        user_input = input("What do you want to ask?(weather if wanting a weather question and if you want to exit say exit): ").strip().lower()
        if user_input == 'exit':  
            print('Exiting the Chatbot. Goodbye!')
            break  

        if user_input == 'weather':  
            print('Tell me a specific location and I will tell you the weather of that location.')
            city = input('What place do you want the weather of: ')
            weather_info = get_weather(city, api_key)
            print(f'WeatherBot: {weather_info}')
        else:  
            print('I can only help with weather-related questions.')
            

chatbot()
