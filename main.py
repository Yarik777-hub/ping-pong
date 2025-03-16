from pygame import *
from random import randint

#создай окно игры
win = display.set_mode((700,500))
display.set_caption('Крутой Пинг Понг(то что надо)')
background= transform.scale(image.load("dom1.jpg"),(700,500))





# подключение музыки
mixer.init()
mixer.music.load("miusic.mp3")
mixer.music.play()

game = True


clock = time.Clock()
FPS = 40


while game:
    win.blit(background,(0,0)) 
    # проверка нажатия на кнопку выход
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    display.update()
    clock.tick(FPS)
