#!/usr/bin/python3

"""
Name:        Ethan Herndon
Description: SSMTP Weather to Text Message via Python
Date:        1.13.24
Reference:   https://openweathermap.org/api
             https://www.epochconverter.com/timezones
"""

import requests
import time
import smtplib


def weather_setup(city):
    api_address = f"https://api.openweathermap.org/data/2.5/weather?appid=YOURAPIKEY&q="  # Get current weather when
    # requested
    url = f"{api_address}{city}&units=imperial"  # Change to 'metric' depending on country of origin
    return url


def weather_print(message, sender_email, sender_password, end_user):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email, sender_password)
    mail.sendmail(sender_email, end_user, message)
    mail.close()


def weather_main():
    city = f"YOUR TOWN HERE"
    weather_api_url = weather_setup(city)
    json_data = requests.get(weather_api_url).json()

    formatted_data = json_data['weather'][0]['main']
    weather_desc = f"Description: {json_data['weather'][0]['description']}"
    temp = (json_data['main']['temp'])
    temp_max = (json_data['main']['temp_max'])
    feel_temp = (json_data['main']['feels_like'])

    # some number relative to UTC/GMT. You can tailor this to your time zone https://www.epochconverter.com/timezones
    offset_in_seconds = "Offset In seconds HERE"

    # In my case I am behind UTC/GMT otherwise use '+', time format ex:
    # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sunup = (json_data['sys']['sunrise'] - offset_in_seconds)
    sunrise = time.strftime("%H:%Mam", time.localtime(sunup))
    sundown = (json_data['sys']['sunset'] - offset_in_seconds)
    sunset = time.strftime("%H:%Mpm", time.localtime(sundown))

    sender_email, sender_password, end_user = "", "", ""
    # Assigned variables into a desired output
    message = f"{city} weather is \n{formatted_data}\n{weather_desc}\nCurrent Temp: {str(int(temp))}F\nFeels Like: " \
              f"{str(int(feel_temp))}F\nMax Temp: {str(int(temp_max))}F\nSunset: {sunset}\nSunrise: {sunrise}"

    weather_print(message, sender_email, sender_password, end_user)


if __name__ == '__main__':
    weather_main()
