import json
import os
import sys
import time
import webbrowser
from dotenv import load_dotenv
from groq import Groq
from gtts import gTTS
import musicLibrary
import pyautogui
import pygame
from pynput import keyboard
import pyttsx3
import requests
import speech_recognition as sr

load_dotenv()

recognizer = sr.Recognizer()
newsApi = "b526c2e05fcd4739ba65c983be7fcee5"
MEMORY_FILE = "memory.json"

# Initialize Pygame Mixer ONCE at the start
pygame.mixer.init()

# Global interruption flag
interrupted = False


def on_press(key):
  global interrupted
  if key == keyboard.Key.space:
    if pygame.mixer.music.get_busy():
      pygame.mixer.music.stop()
      interrupted = True
      print("\n[JARVIS Interrupted by Spacebar!]")


# Permanent background listener for spacebar
listener = keyboard.Listener(on_press=on_press)
listener.start()


# --- Text To Speech ---
def speak_old(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()


def speak(text):
  global interrupted
  interrupted = False
  print(f"JARVIS: {text}")
  try:
    tts = gTTS(text)
    tts.save("text.mp3")

    pygame.mixer.music.load("text.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
      if interrupted:
        break
      time.sleep(0.05)

    pygame.mixer.music.unload()
    if os.path.exists("text.mp3"):
      os.remove("text.mp3")
  except Exception as e:
    print(f"TTS Error: {e}")
    speak_old(text)


# --- Memory Functions ---
def load_memory():
  if os.path.exists(MEMORY_FILE):
    try:
      with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content:
          return json.loads(content)
    except Exception as e:
      print(f"Memory Load Error: {e}")

  return [{
      "role": "system",
      "content": (
          "You are Jarvis. ALWAYS respond in 1 short sentence (maximum 15"
          " words). Be concise, direct, and helpful."
      ),
  }]


def save_memory(data):
  try:
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)
      f.flush()
      os.fsync(f.fileno())
  except Exception as e:
    print(f"Memory Save Error: {e}")


# --- Speech Recognition via Groq Whisper ---
def listen_command_whisper():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("\n[JARVIS Listening for Command...]")
    r.adjust_for_ambient_noise(source, duration=0.8)
    audio = r.listen(source, timeout=10, phrase_time_limit=10)

  with open("temp_speech.wav", "wb") as f:
    f.write(audio.get_wav_data())

  print("[Transcribing with Whisper...]")
  try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    with open("temp_speech.wav", "rb") as file:
      transcription = client.audio.transcriptions.create(
          file=("temp_speech.wav", file.read()),
          model="whisper-large-v3",
          prompt="Pakistani English and Urdu accent.",
      )
    user_text = transcription.text.strip()
    print(f"You said: {user_text}")
    return user_text
  except Exception as e:
    print(f"Whisper Error: {e}")
    return ""
  finally:
    if os.path.exists("temp_speech.wav"):
      os.remove("temp_speech.wav")


# --- AI Process with Permanent Memory ---
def aiProcess(command):
  history = load_memory()
  history.append({"role": "user", "content": command})

  client = Groq(api_key=os.getenv("GROQ_API_KEY"))
  completion = client.chat.completions.create(
      model="llama-3.1-8b-instant", messages=history
  )

  reply = completion.choices[0].message.content
  history.append({"role": "assistant", "content": reply})
  save_memory(history)

  return reply


# --- Target-Specific Tab Closing Helper ---
def close_specific_tab(site_keyword):
  pyautogui.hotkey("ctrl", "shift", "a")
  time.sleep(0.3)

  pyautogui.typewrite(site_keyword, interval=0.05)
  time.sleep(0.3)
  pyautogui.press("enter")
  time.sleep(0.3)

  pyautogui.hotkey("ctrl", "w")


# --- Command Execution ---
def processCommand(c):
  c_clean = c.lower().strip()

  if "bye" in c_clean or "stop" in c_clean or "exit" in c_clean:
    speak("Goodbye, Boss.")
    sys.exit()

  elif "open google" in c_clean:
    webbrowser.open("https://google.com")
    speak("Opening Google")

  elif "open facebook" in c_clean:
    webbrowser.open("https://facebook.com")
    speak("Opening Facebook")

  elif "open instagram" in c_clean:
    webbrowser.open("https://instagram.com")
    speak("Opening Instagram")

  elif "open linkedin" in c_clean:
    webbrowser.open("https://linkedin.com")
    speak("Opening Linkedin")

  elif "open youtube" in c_clean:
    webbrowser.open("https://youtube.com")
    speak("Opening Youtube")

  elif "open gemini" in c_clean:
    webbrowser.open("https://gemini.google.com/app")
    speak("Opening Gemini")

  elif "open gpt" in c_clean or "open chat gpt" in c_clean or "chatgpt" in c_clean:
    webbrowser.open("https://chatgpt.com/")
    speak("Opening ChatGPT")

  elif c_clean.startswith("play"):
    song = c_clean.split(" ")[1]
    if song in musicLibrary.music:
      link = musicLibrary.music[song]
      webbrowser.open(link)
      speak(f"Playing {song}")
    else:
      speak("Song not found in library.")

  elif "news" in c_clean:
    r = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApi}"
    )
    if r.status_code == 200:
      data = r.json()
      articles = data.get("articles", [])
      for article in articles[:3]:
        speak(article["title"])

  elif "weather in" in c_clean:
    city = c_clean.split("weather in")[1].strip()
    try:
      url = f"https://wttr.in/{city}?format=%C,+temperature+%t,+feels+like+%f"
      res = requests.get(url)

      if res.status_code == 200:
        weather_info = f"The weather in {city} is {res.text}"
        print(weather_info)
        speak(weather_info)
      else:
        speak(f"Sorry, I couldn't fetch the weather of {city}.")

    except Exception:
      speak("Sorry, there was an issue getting the weather update.")

  # --- Targeted Tab / Browser Closing ---
  elif "close" in c_clean or "stop music" in c_clean or "pause" in c_clean:
    if "linkedin" in c_clean:
      close_specific_tab("linkedin")
      speak("Closed LinkedIn tab.")
    elif "youtube" in c_clean or "yt" in c_clean:
      close_specific_tab("youtube")
      speak("Closed YouTube tab.")
    elif "instagram" in c_clean:
      close_specific_tab("instagram")
      speak("Closed Instagram tab.")
    elif "facebook" in c_clean:
      close_specific_tab("facebook")
      speak("Closed Facebook tab.")
    elif "google" in c_clean:
      close_specific_tab("google")
      speak("Closed Google tab.")
    elif "gemini" in c_clean:
      close_specific_tab("gemini")
      speak("Closed Gemini tab.")
    elif "gpt" in c_clean or "chatgpt" in c_clean:
      close_specific_tab("chatgpt")
      speak("Closed ChatGPT tab.")
    elif "browser" in c_clean or "chrome" in c_clean:
      os.system("taskkill /f /im chrome.exe")
      speak("Browser closed Sir.")
    else:
      pyautogui.hotkey("ctrl", "w")
      speak("Closed current tab.")

  else:
    output = aiProcess(c)
    speak(output)


# --- Non-Stop Active Loop ---
if __name__ == "__main__":
  speak("JARVIS system active.")
  r = sr.Recognizer()

  r.dynamic_energy_threshold = True
  r.energy_threshold = 300

  is_active = False

  while True:
    try:
      with sr.Microphone() as source:
        if not is_active:
          print("\n[Waiting for Wake Word 'Jarvis'...]")
          r.adjust_for_ambient_noise(source, duration=0.5)
          audio = r.listen(source, timeout=8, phrase_time_limit=4)
          wake_word = r.recognize_google(audio, language="en-US").lower()
          print(f"Heard: {wake_word}")

          wake_words_list = [
              "jarvis",
              "jarves",
              "travis",
              "service",
              "jarviz",
              "javis",
          ]
          if any(w in wake_word for w in wake_words_list):
            speak("Yes Boss?")
            is_active = True

        else:
          command = listen_command_whisper()

          if command and len(command.strip()) > 0:
            if any(
                word in command.lower()
                for word in ["bye", "exit", "stop", "sleep", "quiet"]
            ):
              speak("Going to standby mode.")
              is_active = False
            else:
              processCommand(command)
          else:
            print("[No command heard, back to standby...]")
            is_active = False

    except sr.WaitTimeoutError:
      continue
    except sr.UnknownValueError:
      continue
    except Exception as e:
      print(f"System Loop Exception: {e}")