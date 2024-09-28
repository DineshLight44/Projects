import speech_recognition as sr
import webbrowser
import pyttsx3
import music

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def processcmd(c):
    if "google" in c.lower():
        webbrowser.open("https://google.com")
    elif "facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music.musi[song]
        webbrowser.open(link)


  


def speak(text):
    engine.say(text)  # Use the passed argument instead of a hardcoded string
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Rox...")
    while True:
        # Listen for the wake word "Jarvis"
        try:
            with sr.Microphone() as source:
                print("recognizing...")
                audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)

            word = recognizer.recognize_google(audio)
            print(word)
            if word.lower() == "jarvis":
                speak("yes")

                with sr.Microphone() as source:
                    print("listening...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processcmd(command)

        except Exception as e:
            print(f"Error: {e}")


