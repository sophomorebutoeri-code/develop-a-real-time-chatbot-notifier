Python
import os
import time
import pytz
from datetime import datetime
from gtts import gTTS
import speech_recognition as sr
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# Chatbot Notifier Class
class ChatbotNotifier:
    def __init__(self):
        self.messages = []

    def send_message(self, message):
        self.messages.append(message)
        self.notify(message)

    def notify(self, message):
        print(f"New message: {message}")
        self.speak(message)

    def speak(self, message):
        language = 'en'
        speech = gTTS(text=message, lang=language, slow=False)
        speech.save("message.mp3")
        os.system("mpg321 message.mp3")

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            try:
                message = r.recognize_google(audio, language='en-US')
                self.send_message(message)
            except Exception as e:
                print(str(e))

# Main Program
notifier = ChatbotNotifier()
while True:
    notifier.listen()
    time.sleep(1)