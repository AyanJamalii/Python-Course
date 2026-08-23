# Problem 2, install an external module and use it according to your interest.
# so we are installing python text to speech module, which is called pyttsx3, we will install it using pip command in cmd and then we will use it in our code.


import pyttsx3
engine = pyttsx3.init()


engine.say("My name is Ayan! and i can just Speak english, nothing else :(")
engine.runAndWait()