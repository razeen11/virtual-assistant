import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

intro_list = ['who are you', 'what can you do', 'introduce yourself']
greet_list=['hello','hai','hai sera','hello sera','hey sera','hey']

try:
    engine = pyttsx3.init()
except ImportError:
    print("Driver not found")
except RuntimeError:
    print("Driver fails to initialise")

voices = engine.getProperty('voices')

'''for voice in voices:
    print(voice.id)'''
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
# rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


def read_voice_cmd():
    voice_text = ''
    print('Listening..')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network Error')
    return voice_text


if __name__ == '__main__':
    speak_text_cmd("   Assistance mode activated! Awaiting your command sir..")

    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))
        if voice_note in greet_list:
            print("Hi sir, How can I help you?")
            speak_text_cmd("Hi sir, How can I help you?")
            continue
        elif voice_note in intro_list:
            print("I was named SERA, 'Smart and Eminent, Robust Assistant'. I could operate through this laptop to "
                  "ease your needs.. Yours command, My satisfaction!")
            speak_text_cmd("I was named, sera, Smart and Eminent Robust Assistant. I could operate through this laptop to "
                           "ease your needs.. Yours command, My satisfaction!")
            continue
        elif 'how are you' in voice_note:
            print("I was made to be perfect, Hope you're good too!")
            speak_text_cmd("I was made to be perfect, Hope you're good too!")
            continue
        elif 'your inspiration' in voice_note:
            print("JARVIS is my role model. To be frank, I'm still under development to be like him. ;-")
            speak_text_cmd("JARVIS is my role model. To be frank, I'm still under development to be like him.")
            continue
        elif 'open' in voice_note:
            speak_text_cmd('Done sir')
            os.system('explorer C:\\"{}"'.format(voice_note.replace('open ', '')))
            print('Done')
            continue
        elif 'launch' in voice_note:
            speak_text_cmd('Launching sir')
            os.system('explorer C:\\"{}"'.format(voice_note.replace('launch ', '')))
            print('Done')
            continue
        elif 'thank you' in voice_note:
            print('You are welcome,sir!')
            speak_text_cmd('You are welcome,sir!')
            exit()
        elif 'bye' in voice_note:
            print('Glad to assist you,sir :-) ')
            speak_text_cmd('Glad to assist you,sir!')
            exit()
        elif 'bye sera' in voice_note:
            print('Glad to assist you,sir :-) ')
            speak_text_cmd('Glad to assist you,sir!')
            exit()
        elif 'see you sera' in voice_note:
            print('see you too')
            speak_text_cmd('see you too,sir!')
            exit()
        elif 'my father' in voice_note:
            print('Your father is Mr V.M.S.Iqbal')
            speak_text_cmd('Your father is mister V.M.S.Eqbal')
            exit()
        elif 'my mother' in voice_note:
            print('Your mother is Mrs K.Sakkeena')
            speak_text_cmd('Your mother is Mrs K.Sakkeena')
            exit()
        elif '' in voice_note:
            speak_text_cmd('wrong or not any commands received,I gonna sleep')
            print('Slept;-)')
            exit()
