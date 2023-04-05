
import speech_recognition as sr

def takecommand():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)
    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language='en-in')
        print(f"user : {query}")
    except Exception as e:
        print(e)
        return 'none'
    return query.lower()

if __name__ == "__main__":
	while True:
		takecommand()