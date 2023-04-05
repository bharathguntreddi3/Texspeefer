import pyttsx3
def text_to_speech(text):
    text_speech = pyttsx3.init()  # initialize
    voices = text_speech.getProperty('voices')
    text_speech.setProperty('voice', voices[1].id)
    text_speech.say(text)   # convert
    text_speech.runAndWait()
#     text_speech.save_to_file(text,'text.mp3')   # save to media

text_to_speech("Hello world")