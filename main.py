import streamlit as st
from datetime import datetime
import random

# --- Set Page Config ---
st.set_page_config(page_title="ElderEase - AI for Elders", layout="centered")

# --- Title ---
st.title("👵🏼 ElderEase: Your Friendly AI Companion")

# --- Chat Section ---
st.header("💬 Talk with ElderEase")
user_input = st.text_input("Say something...", "")

if user_input:
    # Simple AI logic (replace with real chatbot or LLM API)
    if "medicine" in user_input.lower():
        st.write(' Don’t forget to take your medicines on time!')
    elif "how are you" in user_input.lower():
        st.write(" I’m just a bot, but I’m happy to chat with you!")
    else:
        st.write("I’m here to listen and help you feel better!")

# --- Mood Tracker ---
st.header("📊 How are you feeling today?")
mood = st.slider("Select your mood", 0, 10, 5)
if mood <= 3:
    st.write("😔 Sorry to hear that. Take some rest and stay hydrated.")
elif mood >= 7:
    st.write("😊 Glad you're feeling good!")
else:
    st.write("🙂 Hope your day gets better!")

# --- Daily Tip ---
st.header("🌿 Daily Wellness Tip")
tips = [
    "Drink 6-8 glasses of water today.",
    "Take a short walk in the morning sunlight.",
    "Try deep breathing for 5 minutes.",
    "Call a friend or loved one today.",
    "Eat a fruit with breakfast."
]
st.success(random.choice(tips))

# --- Reminder Section ---
st.header("⏰ Set a Reminder")
reminder = st.text_input("What do you want to be reminded about?")
reminder_time = st.time_input("At what time?")

if st.button("Save Reminder"):
    st.success(f"Reminder saved: '{reminder}' at {reminder_time.strftime('%I:%M %p')}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ for the Elderly")
