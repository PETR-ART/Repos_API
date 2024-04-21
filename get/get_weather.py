# подключаем библиотеку для работы с запросами
import requests

city = 'Йошкар-Ола'


def get_weather():
    # формируем запрос
    url = ('https://api.openweathermap.org/data/2.5/weather?q='
           +city+'&units=metric&lang=ru&appid=08e34e35ab68be2b75939da620c9b612')

    # отправляем запрос на сервер и сразу получаем результат
    weather_data = requests.get(url).json()

    # получаем данные о температуре и о том, как она ощущается
    temperature = round(weather_data['main']['temp'])

    # выводим значения на экран
    return str(temperature)
