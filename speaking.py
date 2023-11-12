import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',120)#Speed of speech
engine.setProperty('voice','english')#Language of speech

inp = input('Enter the text to speak : ')

engine.say(inp)
engine.runAndWait()
