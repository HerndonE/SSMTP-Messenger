#!/usr/bin/python3

'''
Ethan Herndon
SSMTP Weather to Text Message via Python
5.23.2020
'''

import requests
import time
import smtplib

''' Get Current Weather When Requested'''
api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=YOURAPIKEY&q='
city = "YOUR TOWN HERE"
url = api_address + city + '&units=imperial' # You can also use 'metric' depending on your location
json_data = requests.get(url).json()

formatted_data = json_data['weather'][0]['main']
weather_desc = "Description: " + json_data['weather'][0]['description']
temp = (json_data['main']['temp'])
temp_max = (json_data['main']['temp_max'])
feel_temp = (json_data['main']['feels_like'])

offsetInSeconds = some number #Relative to UTC/GMT. You can tailor this to your time zone
# Reference: https://www.epochconverter.com/timezones

sunup = (json_data['sys']['sunrise'] - offsetInSeconds) # In my case I am behind UTC/GMT otherwise use '+'
'''sunrise = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sunup))'''
sunrise = time.strftime("%H:%Mam", time.localtime(sunup))
sundown = (json_data['sys']['sunset'] - offsetInSeconds)
'''sunset = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sundown))'''
sunset = time.strftime("%H:%Mpm", time.localtime(sundown))


'''print("The weather in " + city + " is " + "\n") # Test print the weather in console
print(formatted_data)
print(weather_desc)
print("Current Temperature: " + str(temp) + "F")
print("Feels Like: " + str(feel_temp) + "F")
print("Maximum Temperature: " + str(temp_max) + "F")
print("Sunrise: " + sunrise)
print("Sunset: " + sunset)'''

one = city + " weather is " + "\n" # Assigned desired output as variables to be concatenated
two = formatted_data + "\n"
three = weather_desc + "\n"
four = "Current Temp: " + str(int(temp)) + "F" + "\n"
five = "Feels Like: " + str(int(feel_temp)) + "F" + "\n"
six = "Max Temp: " + str(int(temp_max)) + "F" + "\n"
eight = "Sunset: " + sunset + "\n"
seven = "Sunrise: " + sunrise + "\n" 

content = one + two + three + four + five + six + seven + eight
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('SENDER EMAIl','SENDER PASSWORD')
mail.sendmail('SENDER EMAIL','RECIEVER',content)
mail.close()

''' Send User 5 Day Forecast Each Day At 5pm '''
api_address = 'https://api.openweathermap.org/data/2.5/forecast?appid=YOURAPIKEY&q='
city = "YOUR TOWN HERE"
url = api_address + city + '&units=imperial'
json_data = requests.get(url).json()

day1 = (json_data['list'][3]['dt'] - offsetInSeconds) 
dayOne = time.strftime("%m-%d @ %Hpm", time.localtime(day1))
tempOne = (json_data['list'][3]['main']['temp'])

day2 = (json_data['list'][11]['dt'] - offsetInSeconds)
dayTwo = time.strftime("%m-%d @ %Hpm", time.localtime(day2))
tempTwo = (json_data['list'][11]['main']['temp'])

day3 = (json_data['list'][19]['dt'] - offsetInSeconds)
dayThree = time.strftime("%m-%d @ %Hpm", time.localtime(day3))
tempThree = (json_data['list'][19]['main']['temp'])

day4 = (json_data['list'][27]['dt'] - offsetInSeconds)
dayFour = time.strftime("%m-%d @ %Hpm", time.localtime(day4))
tempFour = (json_data['list'][27]['main']['temp'])

day5 = (json_data['list'][35]['dt'] - offsetInSeconds)
dayFive = time.strftime("%m-%d @ %Hpm", time.localtime(day5))
tempFive = (json_data['list'][35]['main']['temp'])

forecast = "5 Day Forecast \n" # Assigned Forecast output as variables to be concatenated
p1 = "Temp: " + str(int(tempOne)) + "F \n"
p2 = "Temp: " + str(int(tempTwo)) + "F \n"
p3 = "Temp: " + str(int(tempThree)) + "F \n"
p4 = "Temp: " + str(int(tempFour)) + "F \n"
p5 = "Temp: " + str(int(tempFive)) + "F \n"

content = forecast + dayOne +"\n" + p1 + dayTwo +"\n" + p2 + dayThree +"\n" + p3 + dayFour +"\n" + p4 + dayFive +"\n" + p5
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('SENDER EMAIl','SENDER PASSWORD')
mail.sendmail('SENDER EMAIL','RECIEVER',content)
mail.close()

# Reference: https://openweathermap.org/api
