import speech_recognition as sr
import pyttsx3
import ollama
import sys
import time
import webbrowser

# ================= TEXT TO SPEECH =================
engine = None
SPEAKING = False

VOICE_ID = (
    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\"
    "TTS_MS_EN-US_ZIRA_11.0"
)


def init_tts():
    global engine
    engine = pyttsx3.init(driverName="sapi5")
    engine.setProperty("voice", VOICE_ID)
    engine.setProperty("rate", 175)


def say(text):
    global SPEAKING
    try:
        if engine is None:
            init_tts()
        SPEAKING = True
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    finally:
        SPEAKING = False


# ================= SPEECH TO TEXT =================
def take_command():
    while SPEAKING:
        time.sleep(0.05)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source, phrase_time_limit=6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You:", query)
        return query.lower()
    except:
        return ""


# ================= OLLAMA =================
MODEL_NAME = "qwen2.5-coder:7b"


def chat_with_ollama(prompt):
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a confident, intelligent AI assistant like Iron Man's Jarvis. "
                    "Never say you are just a computer or that you have no feelings. "
                    "Speak professionally and address the user as sir."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.message.content


def ensure_ollama_ready():
    try:
        ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": "hello"}],
        )
        return True
    except Exception as e:
        print("Ollama connection error:", e)
        return False


# ================= MAIN =================
if __name__ == "__main__":
    init_tts()

    if not ensure_ollama_ready():
        say("Ollama is offline. Please start the Ollama server.")
        sys.exit(1)

    say("Welcome back, sir. Jarvis is online.")

    while True:
        query = take_command()
        if query == "":
            continue

        # -------- EXIT --------
        if "exit" in query or "quit" in query or "shutdown" in query:
            response = "Shutting down. Goodbye, sir."
            print("Jarvis:", response)
            say(response)
            break

        # -------- BASIC TALK --------
        if "how are you" in query:
            response = "I am operating at full efficiency, sir."
            print("Jarvis:", response)
            say(response)
            continue

        if "who are you" in query:
            response = "I am Jarvis, your personal artificial intelligence assistant."
            print("Jarvis:", response)
            say(response)
            continue

        if "what is your name" in query:
            response = "My name is Jarvis, sir."
            print("Jarvis:", response)
            say(response)
            continue

        if "hello" in query or "hi" in query:
            response = "Hello sir. How may I assist you?"
            print("Jarvis:", response)
            say(response)
            continue

        # -------- TIME --------
        if "time" in query:
            current_time = time.strftime("%I:%M %p")
            response = f"The current time is {current_time}, sir."
            print("Jarvis:", response)
            say(response)
            continue

        # -------- OPEN WEBSITES --------
        if query.startswith("open "):
            site = query.replace("open ", "", 1).strip()

            sites = {
                "youtube": "https://www.youtube.com",
                "google": "https://www.google.com",
                "wikipedia": "https://www.wikipedia.org",
                "linkedin": "https://www.linkedin.com",
                "github": "https://www.github.com",
            }

            url = sites.get(site, f"https://{site}.com")
            response = f"Opening {site}, sir."
            print("Jarvis:", response)
            say(response)
            webbrowser.open(url)
            continue

        # -------- OLLAMA FALLBACK --------
        reply = chat_with_ollama(query)
        print("Jarvis:", reply)
        say(reply)
