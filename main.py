import streamlit as st
from datetime import datetime
import random
import speech_recognition as sr
import pyttsx3

# --- Set Page Config ---
st.set_page_config(page_title="ElderEase - AI for Elders", layout="centered")

# --- Initialize TTS ---
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# --- Title ---
st.title("👵🏼 ElderEase: Your Friendly AI Companion")

# --- Voice Input ---
st.header("🎙️ Voice Chat")
if st.button("Start Listening"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio)
            st.success(f"You said: {user_input}")
        except sr.WaitTimeoutError:
            user_input = ""
            st.warning("Listening timed out.")
        except sr.UnknownValueError:
            user_input = ""
            st.warning("Could not understand audio.")
        except sr.RequestError:
            user_input = ""
            st.error("API unavailable.")
else:
    user_input = st.text_input("💬 Or type something...", "")

# --- Chat Response ---
if user_input:
    if "medicine" in user_input.lower():
        response = "Don’t forget to take your medicines on time!"
    elif "how are you" in user_input.lower():
        response = "I’m just a bot, but I’m happy to chat with you!"
    else:
        response = "I’m here to listen and help you feel better!"
    st.write(response)
    speak(response)

# --- Mood Tracker ---
st.header("📊 How are you feeling today?")
mood = st.slider("Select your mood", 0, 10, 5)
if mood <= 3:
    mood_response = "Sorry to hear that. Take some rest and stay hydrated."
elif mood >= 7:
    mood_response = "Glad you're feeling good!"
else:
    mood_response = "Hope your day gets better!"
st.write(f"🙂 {mood_response}")
speak(mood_response)

# --- Daily Tip ---
st.header("🌿 Daily Wellness Tip")
tips = [
    "Drink 6-8 glasses of water today.",
    "Take a short walk in the morning sunlight.",
    "Try deep breathing for 5 minutes.",
    "Call a friend or loved one today.",
    "Eat a fruit with breakfast."
]
tip = random.choice(tips)
st.success(tip)
speak(tip)

# --- Reminder Section ---
st.header("⏰ Set a Reminder")
reminder = st.text_input("What do you want to be reminded about?")
reminder_time = st.time_input("At what time?")

if st.button("Save Reminder"):
    reminder_msg = f"Reminder saved: '{reminder}' at {reminder_time.strftime('%I:%M %p')}"
    st.success(reminder_msg)
    speak(reminder_msg)

# Footer
st.markdown("---")
st.caption("Made with ❤️ for the Elderly")

