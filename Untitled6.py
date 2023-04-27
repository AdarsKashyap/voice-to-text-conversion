#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import pyttsx3 as pt
import pyaudio as py
import webbrowser as we
import pyjokes as pj
import speech_recognition as sr
def voice():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print(" SPEAK NOW..!")
        command.adjust_for_ambient_noise(source)
        audio=command.listen(source)
        try:
            print("Listening...")
            data=command.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not recognized, Ask again.. !")
voice()


# In[ ]:




