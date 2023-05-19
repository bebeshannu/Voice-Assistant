import pyttsx3 as tt
import speech_recognition
from neuralintents.main import GenericAssistant
from model import assistent
recognizer=speech_recognition.Recognizer()
speaker=tt.init()
assistent.load_model("assistant_model")

speaker.setProperty("rate",150)


while True:
    try:
        with speech_recognition.Microphone() as mic:
            # recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            # audio=recognizer.listen(mic,timeout=5)
            # message=recognizer.recognize_google(audio)
            # print(message)
            response=assistent.request("Send a mail")
            print(response)
            speaker.say(response)
            speaker.runAndWait()
    except speech_recognition.UnknownValueError:
        pass  