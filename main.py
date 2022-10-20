from email.mime import audio

import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print (words)
    os.system("say " + words)


talk ("Привет, чем я могу помочь Вам?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Просто вывод, чтобы мы знали когда говорить
        print("Говорите")
        # Устанавливаем паузу, чтобы прослушивание
        # началось лишь по прошествию 1 секунды
        r.pause_threshold = 1
        # используем adjust_for_ambient_noise для удаления
        # посторонних шумов из аудио дорожки
        r.adjust_for_ambient_noise(source, duration=1)
        # Полученные данные записываем в переменную audio
        # пока мы получили лишь mp3 звук
        audio = r.listen(source)


    try:  # Обрабатываем все при помощи исключений

        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        # Просто отображаем текст что сказал пользователь
        print("Вы сказали: " + zadanie)
    # Если не смогли распознать текст, то будет вызвана эта ошибка
    except sr.UnknownValueError:
    # Здесь просто проговариваем слова "Я вас не поняла"
    # и вызываем снова функцию command() для
    # получения текста от пользователя
        talk("Я вас не поняла!!")
        zadanie = command()

    # В конце функции возвращаем текст задания
    # или же повторный вызов функции
    return zadanie


def makeSomething(zadanie):
    if 'открыть сайт'  in zadanie:
        talk ("Уже открываю")
        url = 'https://lenta.ru/'
        webbrowser.open(url)

    elif "стоп" in zadanie:
        talk ("Да, конечно, без проблем")
        sys.exit()
    elif   'имя'  in zadanie:
        talk ("Меня зовут Сири")


while True:
    makeSomething(command())

