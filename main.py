# main.py
import speech_recognition as sr
from helper import speak
from commands import processCommand
import time

r = sr.Recognizer()

def listen(timeout=5, phrase_time_limit=5):
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            return audio
        except sr.WaitTimeoutError:
            return None

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    # Calibrate mic once
    with sr.Microphone() as source:
        print("Calibrating background noise...")
        r.adjust_for_ambient_noise(source, duration=1)

    while True:
        # Wake word detection
        print("Say 'Jarvis' to activate...")
        audio = listen(timeout=5, phrase_time_limit=5)
        if audio is None:
            continue  

        try:
            word = r.recognize_google(audio)
            print(f"You said: {word}")

            if word.lower() == "jarvis":
                speak("Yes? How can I help you?")
                time.sleep(0.2)
                # Command mode
                while True:
                    print("Jarvis Activated ... Listening for command to open Website.\n"
                          "Say 'Stop' to exit command mode or 'Shutdown' to shutdown program.")
                    audio = listen(timeout=6, phrase_time_limit=6)
                    if audio is None:
                        continue  
                    try:
                        command = r.recognize_google(audio)
                        print(f"Command: {command}")

                        result = processCommand(command)

                        if result == True:
                            time.sleep(0.2)
                            # task complete → go back to wake word
                            break
                        elif result == "exit":
                            time.sleep(0.2)
                            # exit command mode → go back to wake word
                            break
                        elif result == "terminate":
                            time.sleep(0.2)
                            # shutdown entire program
                            exit(0)

                    except sr.UnknownValueError:
                        speak("I couldn't understand. Please say again.")
                    except sr.RequestError:
                        speak("Network error. Check your internet connection.")
                        break

        except sr.UnknownValueError:
            print("Could not understand. Waiting for word 'Jarvis' again...")
        except sr.RequestError:
            print("Network error. Waiting....")

        time.sleep(0.2)
