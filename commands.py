import webbrowser
from helper import speak
import time


def processCommand(c):
    c = c.lower()

    # ==== SOCIAL MEDIA ====
    if 'open youtube' in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True

    elif 'open facebook' in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        return True

    elif 'open instagram' in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
        return True

    elif 'open twitter' in c or 'open x' in c:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
        return True

    elif 'open tiktok' in c:
        speak("Opening TikTok")
        webbrowser.open("https://www.tiktok.com")
        return True

    elif 'open snapchat' in c:
        speak("Opening Snapchat")
        webbrowser.open("https://www.snapchat.com")
        return True
    
    elif 'open whatsapp' in c:
        speak("Opening WhatsApp")
        webbrowser.open("https://www.whatsapp.com")
        return True

    elif 'open reddit' in c:
        speak("Opening Reddit")
        webbrowser.open("https://www.reddit.com")
        return True

    elif 'open discord' in c:
        speak("Opening Discord")
        webbrowser.open("https://www.discord.com/app")
        return True

    elif 'open linkedin' in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        return True


    # ==== IMPORTANT WEBSITES ====
    elif 'open google' in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return True

    elif 'open gmail' in c:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
        return True

    elif 'open maps' in c or 'open google maps' in c:
        speak("Opening Google Maps")
        webbrowser.open("https://maps.google.com")
        return True

    elif 'open wikipedia' in c:
        speak("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")
        return True

    elif 'open amazon' in c:
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")
        return True

    elif 'open netflix' in c:
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com")
        return True

    elif 'open spotify' in c:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")
        return True

    elif 'open github' in c:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
        return True

    elif 'open stackoverflow' in c or 'open stack overflow' in c:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
        return True


    # ==== EXIT COMMAND MODE ====
    elif 'stop' in c or 'exit' in c or 'sleep' in c:
        speak("Okay, going back to sleep.")
        return "exit"

    # ==== EXIT ENTIRE PROGRAM ====
    elif 'finish' in c or 'quit' in c or 'shutdown' in c:
        speak("Shutting down. Goodbye!")
        return "terminate"



    # ==== UNKNOWN COMMAND ====
    else:
        speak("I cannot understand. Please repeat.")
        return False
