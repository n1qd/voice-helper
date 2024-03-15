import speech_recognition as sr
from speakerpy.lib_speak import Speaker
from speakerpy.lib_sl_text import SeleroText


hi = ["привет", "добрый день", "доброе утро", "добрый вечер", "здарова", "салам"]

def talk_hi():
    text = SeleroText("Пример текста для синтеза речи")
    speaker = Speaker(model_id="ru_v3", language="ru", speaker="aidar", device="cpu")
    speaker.speak(text=text, sample_rate=48000, speed=1.0)



micIndex = None
for index, name in enumerate(sr.Microphone.list_microphone_names()): #определяем основной микрофон
    if name == "USB Audio Device":
        micIndex = index
        break

while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index = micIndex) as source: #
        print("Слушаю...")
        audio = r.listen(source)
    text = r.recognize_google(audio, language= 'ru-RU')
    text = text.lower()


    for val in hi:
        if text == val:
            talk_hi()