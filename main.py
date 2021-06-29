from flask import Flask, render_template, redirect, request
import json
import requests

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def WeatherApp():
    if request.method == "POST":
        city = request.form.get("city1")
        url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&unit=metric&appid=7d64f2cd5098629e2725ae9f1d5fbf02'.format(city)
        response = requests.get(url)
        weather_data = response.json() 

        temp = round(weather_data["main"]["temp"])
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        return render_template(
            "result.html",
            city=city,
            temp=temp,
            humidity=humidity,
            wind_speed=wind_speed,
        )


   
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    app.run(port=5000)