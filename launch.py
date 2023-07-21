from bardapi import Bard
import pyttsx3
import speech_recognition as sr
import time
import wikipedia
import subprocess
import datetime
import re
import webbrowser

#Set BardAI API key
token = "YAjPakof_DHcxzVIYvUJD7zm6TvlPEtHq-zrX0H-1Cgjw0_ZPQpV1_zTquXrEwvhA5RbHA."

#Initialize text-to-speech engine
engine = pyttsx3.init()

def transcribe(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Couldn't hear that. Can you repeat..?")

def generate_response(prompt):
    response = Bard(token).get_answer(prompt)
    return response["choices"][0]["text"]
    
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hell. Good Morning, Sir")
        speak_text("Hello. Good Morning,Sir")
    elif hour>=12 and hour<18:
        print("Hello. Good Afternoon, Sir")
        speak_text("Hello. Good Afternoon,Sir")
    else:
        print("Hello. Good Evening, Sir")
        speak_text("Hello. Good Evening,Sir")

#Ignore "*" in text
def ignore_star(text):
  output = re.sub(r"\*", "\anna", "", text)
  return output

print('Loading your AI personal assistant - Anna')
speak_text('Loading your AI personal assistant - Anna')
wishMe()
    
def main():
    while True:
        #Wait for user to say 'Anna'
        print("Say 'Anna' to ask anything...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if 'anna' in transcription:
                    #Record More Audio
                    filename = "input.wav"
                    print("Ask anything...")
                    source.pause_threshold = 1
                    audio = recognizer.listen(source, phrase_time_limit = None, timeout = None)
                    with open(filename, "wb") as f:
                      f.write(audio.get_wav_data())
                    
                    #Transcribe Audio to Text
                    text = transcribe(filename)
                    statement = text.replace("genius", "")
                    if statement:
                        print(f"Thinking... {statement}")
                        
                        #Generate Response using BardAI
                        prompt = "Answer in brief and short and make sure that the answers are as short as possible but must have full and complete sentences, without mentioning brief and short in your answer, " + (statement)
                        response = Bard(token).get_answer(prompt)['content']
                        ai_response = ignore_star(response)
                        print(f"AI: {response}")
                        
                        #Read response using text-to-speech
                        speak_text(ai_response)

                if 'wikipedia' in transcription:
                  speak_text('Searching Wikipedia...')
                  statement = statement.replace("wikipedia", "")
                  results = wikipedia.summary(statement, sentences=3)
                  speak_text("According to Wikipedia")
                  print("According to Wikipedia," + results)
                  speak_text(results)

                elif 'time' in statement or 'date' in statement:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    strDate=datetime.datetime.now().strftime("%A, %d %B")
                    speak_text(f"Today is {strDate} and, its {strTime} now in the clock")

                elif "shut down" in statement:
                    print('your personal assistant Anna is shutting down,Good bye')
                    speak_text('your personal assistant Anna is shutting down,Good bye')
                    break

                elif "logout" in statement:
                    print("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    speak_text("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                    subprocess.call(["shutdown", "/l"])

                elif 'search'  in statement:
                    statement = statement.replace("search", "")
                    webbrowser.open_new_tab(statement)
                    time.sleep(5)

            except Exception as e:
                print("An error encountered: {}".format(e))

if __name__ == "__main__":
    main()