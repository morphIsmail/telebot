import pyowm
import telebot

owm = pyowm.OWM('a33cfa119f202b32cb4cd56de05e87dc', language="ru")
bot = telebot.TeleBot("884273444:AAHWaX3TjmnxLOgx1RA6jXIE3sQkgrb929Y")

@bot.message_handler(content_types=["text"])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    detail = w.get_detailed_status()
    temp = w.get_temperature('celsius')["temp"]
    hum = w.get_humidity()
    speed = w.get_wind()["speed"]

    answer = "В городе "+message.text+" сейчас "+str(detail)+" \nТемпература: "+str(temp)+" °С \nВлажность: "+str(hum)+" % \nСкорость ветра: "+str(speed)+" м/с"

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
