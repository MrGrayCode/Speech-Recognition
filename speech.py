import speech_recognition as sr

r=sr.Recognizer()

s=''
while s.lower()!='bye':
	with sr.Microphone() as source:
		print('Say something!')
		audio=r.listen(source)
	try:
		s=r.recognize_google(audio)
		print('I think you said ' + s)
	except sr.UnknownValueError:
		print('Sorry, try again!')
	except sr.RequestError as e:
		print('Could not request results from Google Speech Recognition service; {0}'.format(e))
print('Have a nice day!')
