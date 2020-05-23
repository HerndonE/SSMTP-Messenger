'''
Ethan Herndon
Forecast Test Script
5.23.2020
'''


import requests
import time
import smtplib

api_address = 'https://api.openweathermap.org/data/2.5/forecast?appid=YOURAPIKEY&q='
city = "YOUR CITY HERE"
url = api_address + city + '&units=imperial'
json_data = requests.get(url).json()

offsetInSeconds = some number #Relative to UTC/GMT. You can tailor this to your time zone
# Reference: https://www.epochconverter.com/timezones

day1 = (json_data['list'][3]['dt'] - offsetInSeconds) # In my case I am behind UTC/GMT otherwise use '+'
dayOne = time.strftime("%m-%d %Hpm", time.localtime(day1))
tempOne = (json_data['list'][3]['main']['temp'])

day2 = (json_data['list'][11]['dt'] - offsetInSeconds)
dayTwo = time.strftime("%m-%d %Hpm", time.localtime(day2))
tempTwo = (json_data['list'][11]['main']['temp'])

day3 = (json_data['list'][19]['dt'] - offsetInSeconds)
dayThree = time.strftime("%m-%d %Hpm", time.localtime(day3))
tempThree = (json_data['list'][19]['main']['temp'])

day4 = (json_data['list'][27]['dt'] - offsetInSeconds)
dayFour = time.strftime("%m-%d %Hpm", time.localtime(day4))
tempFour = (json_data['list'][27]['main']['temp'])

day5 = (json_data['list'][35]['dt'] - offsetInSeconds)
dayFive = time.strftime("%m-%d %Hpm", time.localtime(day5))
tempFive = (json_data['list'][35]['main']['temp'])


print("5 Day Forecast")
print(dayOne)
print("Temp: " + str(int(tempOne)) + "F")

print(dayTwo)
print("Temp: " + str(int(tempTwo)) + "F")

print(dayThree)
print("Temp: " + str(int(tempThree)) + "F")

print(dayFour)
print("Temp: " + str(int(tempFour)) + "F")

print(dayFive)
print("Temp: " + str(int(tempFive)) + "F")

# Reference: https://openweathermap.org/api