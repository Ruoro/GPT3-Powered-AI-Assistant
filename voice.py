# import openai
# import pyttsx3
# import speech_recognition as sr
# import time
# import os
# from gtts import gTTS


# # Set up the OpenAI API key
# openai.api_base = "https://api.openai.com"
# openai.api_key = "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"


# # Set up the speech engine
# engine = pyttsx3.init()

# def transcribe_audio_to_text(filename):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(filename) as source:
#         audio = recognizer.record(source)
#         try:
#             return recognizer.recognize_google(audio)
#         except:
#             print("Could not catch that")

# def get_response(prompt):
#     response = openai.Completion.create(
#         engine = "text-davinci-003",
#         messages=[
#         {"role": "system", "content": "You are a helpful Voice assistant."},
#         {"role": "user", "content": prompt}
#                 ],
#         prompt = prompt,
#         max_tokens = 1000,
#         n = 1,
#         stop = None,
#         temperature = 0.6,
#     )
#     return response['choices'][0]['text']

# def speak_text(text):
#     engine.say(text)
#     engine.runAndWait()

# def main():
#     while True:
#         # wait for user to say genius
#         print ("Say 'Genius' to start recording your question")
#         with sr.Microphone() as source:
#             recognizer = sr.Recognizer()
#             audio = recognizer.listen(source)
#             try:
#                 transcription = recognizer.recognize_google(audio)
#                 if transcription.lower() == "genius":
#                     # Record the user's question
#                     filename = 'input.wav'
#                     print ("Recording your question")  
#                     with sr.Microphone() as source:
#                         recognizer = sr.Recognizer()
#                         source.pause_threshold = 1
#                         audio = recognizer.listen(source, phrase_time_limit = None, timeout = None)
#                         with open(filename, 'wb') as f:
#                             f.write(audio.get_wav_data())
                    
#                 # transcribe (question) audio to text
#                     text = transcribe_audio_to_text(filename)
#                     if text:
#                         print (f"You said: {text}")

#                         # get response from OpenAI
#                         response = get_response(text)
#                         print(f"Genius says: {response}")
#                         tts = gTTS(response, lang='en')
#                         tts.save("sample.mp3")
                        
#                         speak_text(response)
#             except Exception as e:
#                 print('An error occurred: {}'.format(e))

# if __name__ == "__main__":
#     main()




import openai
import pyttsx3
import speech_recognition as sr
import os
from gtts import gTTS

# Set up the OpenAI API key and base URL
openai.api_key = "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"
openai.api_base = "https://api.openai.com/v1/completions"

# Set up the speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            print("Could not catch that")

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model ="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful Voice assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.6,
    )
    return response['choices'][0]['text']

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Say 'Genius' to start recording your question")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "genius":
                    filename = 'input.wav'
                    print("Recording your question")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, 'wb') as f:
                            f.write(audio.get_wav_data())

                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")

                        response = get_response(text)
                        print(f"Genius says: {response}")
                        tts = gTTS(response, lang='en')
                        tts.save("sample.mp3")

                        speak_text(response)
            except Exception as e:
                import traceback
                print("An error occurred:")
                traceback.print_exc()

if __name__ == "__main__":
    main()
