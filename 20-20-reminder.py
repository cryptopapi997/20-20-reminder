import os
import time
import pygame
pygame.init()

def notify(title, text):
    sound = pygame.mixer.Sound("your_sound_path_here")
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    sound.play()

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        print('{:02d}:{:02d}'.format(mins, secs), end="\r" )
        time.sleep(1)
        t -= 1
        if t == 0:
            countdown(1200)



while (1==1):
    notify("20/20 RULE", "Look at something 20 feet away for 20 seconds or more")
    countdown(1200)
    time.sleep(1200)
    
