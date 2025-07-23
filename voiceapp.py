import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to voice and convert to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting.")
        return ""

def main():
    speak("Hello! How can I help you?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hi there! How can I assist you?")
        elif "your name" in command:
            speak("I am your voice assistant.")
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        elif command:
            speak("You said: " + command)

if __name__ == "__main__":
    main()
