import sys
import yaml
import speech_recognition as sr
from brain import brain
from GreyMatter.SenseCells.tts import tts
from subprocess import call

profile = open('profile.yaml.default')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
proxy_username = profile_data['proxy_username']
proxy_password = profile_data['proxy_password'] 
tts('Welcome ' + name + ', systems are now ready to run. How can I help you?')
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=5)
        print("Say something!")
        audio = r.listen(source)
     try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        call(["espeak",speech_text])
        print("Jarvis thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Jarvis could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    brain(name, speech_text, city_name, city_code, proxy_username, proxy_password)
    main()
main()
