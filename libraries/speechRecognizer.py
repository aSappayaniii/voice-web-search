import speech_recognition as sr
import pprint

def getMicrophone():

    microphones = sr.Microphone.list_working_microphones() # Creates a dictionary of microphones connected to the computer

    if not microphones:
        print("No microphones were found.")
        return None
    
    print("Available microphones:")
    for i, mic in microphones.items():
        print(i, ":", mic)

    try:
        index = int(input("Enter the number of the microphone you want to use (If you don't know, leave blank.): ")) #Leaving it blank will utilize the default mic
        return index 
    except ValueError:
        print("Utilizing default microphone.")
        return None
    
def speechToText(microphone=None):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 100 # Values below this threshold are considered as silence, and values above it are considered speech.
    recognizer.pause_threshold = 2 # Seconds of silence before the program considers the speech is over.

    if microphone is not None:
        with sr.Microphone(device_index=microphone) as source:
            print("Listening!")
            audio = recognizer.listen(source)
    else:
        with sr.Microphone() as source:
            print("Listening!")
            audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f'Could not request results from Google Speech Recognition service; {e}')

