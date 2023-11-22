import libraries.speechRecognizer as sr
import libraries.webSearcher as ws

def main():
    while True:
        currentMic = sr.getMicrophone()
        convertedSpeech = sr.speechToText(currentMic)

        if convertedSpeech:

            print(convertedSpeech)

            print("Is this what you said? Reply verbally with a yes or no.")
            confirmation = sr.speechToText(currentMic)

            if confirmation.lower() == "yes":
                ws.googleSearch(convertedSpeech)
                break
            
            else:
                print("Would you like to retry? Reply verbally with a yes or no.")
                retry = sr.speechToText(currentMic)

                if retry.lower() == "yes":
                    continue
                elif retry.lower() == "no":
                    print("Okay, thank you.")
                    break

        else:
            print("Would you like to retry? Reply verbally with a yes or no.")
            retry = sr.speechToText(currentMic)

            if retry.lower() == "yes":
                continue
            elif retry.lower() == "no":
                print("Okay, thank you.")
                break



print("Welcome to Voice Web Search")

main()

