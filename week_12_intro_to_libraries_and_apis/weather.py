"""
Experiment with a weather API.
"""

import requests
import json


def get_forecast(url: str) -> None:
    response = requests.get(url)
    vancouver_weather = json.loads(response.text)
    local_weather = vancouver_weather['list']
    print('Current weather in Vancouver:')
    print(local_weather[0]['weather'][0]['main'], '-', local_weather[0]['weather'][0]['description'])


def main():
    vancouver = 6173331
    api_key = "73e6dd36a2a073c414a629760ac198ce"
    url = "http://api.openweathermap.org/data/2.5/forecast?id=6173331&APPID=73e6dd36a2a073c414a629760ac198ce"
    get_forecast(url)


if __name__ == "__main__":
    main()
