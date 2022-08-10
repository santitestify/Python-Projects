import pyttsx3

# creating an object for pyttsx3 class
engine = pyttsx3.init()

# see how many voices you have in your computer
for voice in engine.getProperty("voices"):
    print(voice)

voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id) # voice spanish
engine.setProperty("voice", voices[1].id)  # voice english


# creating a function to convert texto to speech
def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()


# ask the user to enter text
text = input("Enter your text now: ")

speak(text)