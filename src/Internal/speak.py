import os #for passing command
import pygame #for executing our audio

def speak(data):
    voice="en-US-SteffanNeural"
    command=f'edge-tts --rate=-33% --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")
    try:
     pygame.mixer.music.play()

     while pygame.mixer.music.get_busy():
         pygame.time.Clock().tick(10)
    except Exception as e:
     print("sorry, luffy ate your output\n",e)
    finally:
     pygame.mixer.music.stop()
     pygame.mixer.quit()
     


 


# chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
# webbrowser.get(chrome_path).open('sn.fr.to')