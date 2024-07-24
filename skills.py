import os
import webbrowser
from datetime import datetime
import sys
import subprocess
from num2words import num2words

import voice

try:
    import requests  # pip install requests
except:
    pass


def check(data, answer):
# получение имени функции из ответа из data_set
    func_name = answer.split()[0]
    if func_name == 'repeat':
        repeat(data.replace('компьютер скажи', ''))
    elif func_name == 'time':
        time()
    else:
        # озвучка ответа из модели data_set
        voice.speaker(answer.replace(func_name, ''))

        # запуск функции из skills
        exec(func_name + '()')


def browser():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    webbrowser.open('https://www.youtube.com', new=2)


def game():
    '''Нужно разместить путь к exe файлу любого вашего приложения'''
    try:
        subprocess.Popen('E:\steam\steam.exe')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    # Эта команда отключает ПК под управлением Windows

    # os.system('shutdown')
    print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
    '''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
    try:
        params = {'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'appid': '34345142b37cd0f7aaf71a2991a4519e'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(
            f"На улице {w['weather'][0]['description']}, {num2words(round(w['main']['temp']), lang='ru')} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def repeat(data):
    voice.speaker(data)


def time():
    voice.speaker('Сейчас ' + num2words(datetime.now().hour, lang="ru") + num2words(datetime.now().minute, lang='ru'))

def music():
	webbrowser.open('https://music.yandex.ru/home', new=2)

def offBot():
    '''Отключает бота'''
    sys.exit()


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass
