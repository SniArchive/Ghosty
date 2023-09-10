import speech_recognition as sr

def takeSpeech():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening..\n")
        r.pause_threshold= 0.8
        audio= r.listen(source)
    try:
        print()
        query= r.recognize_google(audio, language="en-in")
        print(f"you said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
    # return query

