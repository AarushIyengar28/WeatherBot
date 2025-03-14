import requests
import matplotlib.pyplot as plt

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"] 
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        temp_faren = temperature * 9/5 + 32
        user_input = input('Do you want the units to be farenheit or celcius?: ')
        
        if user_input == 'Farenheit'.lower():
            formatted_message = f'The weather in {city} is {description} with a temperature of {temp_faren}°F and a humidity of {humidity}%'
            return {"temprature": temp_faren, "humidity": humidity}, formatted_message
        if user_input == 'Celcius'.lower():
            formatted_message = f'The weather in {city} is {description} with a temperature of {temperature}°F and a humidity of {humidity}%'
            return {"temperature": temperature, "humidity": humidity}, formatted_message
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
            weather_info1 = get_weather(city, api_key)
            print(f'WeatherBot: {weather_info1}')
            compare = input('Do you want to comapre the weather of 2 cities?(yes/no): ').strip().lower()
            if compare == 'yes':
                city2 = input('Enter a city for comaprison: ').strip().lower()
                weather_data1, weather_info1 = get_weather(city, api_key)
                weather_data2, weather_info2 = get_weather(city2, api_key)
                if weather_data1 and weather_data2:
                    comparison_type = input('Do you want to compare temprature or humidity: ').strip().lower()
                    if comparison_type == 'temprature':
                        temp1 = weather_data1["temprature"]
                        temp2 = weather_data2["temprature"]
                        
                        labels = [city, city2]
                        values = [temp1, temp2]
                        
                        plt.yticks([i * 10 for i in range(10)])

                
                        plt.bar(labels, values)
                        plt.show()
                if comparison_type == 'humidity':
                    humidity1 = weather_data1["humidity"]
                    humidity2 = weather_data2["humidity"]
                    labels = [city, city2]
                    values = [humidity1, humidity2]
                    plt.yticks([i * 10 for i in range(10)])

                
                    plt.bar(labels, values)
                    plt.show()        
                        
                        


chatbot()

    






