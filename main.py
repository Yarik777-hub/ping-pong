from pygame import *
from random import randint

#создай окно игры
win = display.set_mode((700,500))
display.set_caption('Крутой Пинг Понг(то что надо)')
background= transform.scale(image.load("dom1.jpg"),(700,500))

class Game_sprite(sprite.Sprite):
    def __init__(self, img, x,y, w,h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Player1(Game_sprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>10:
            self.rect.y-= self.speed 
        if key_pressed[K_DOWN] and self.rect.y<500 - 10-self.rect.width:
            self.rect.y+= self.speed
class Player2(Game_sprite):
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_W] and self.rect.y>10:
            self.rect.y-= self.speed 
        if key_pressed[K_S] and self.rect.y<500 - 10-self.rect.width:
            self.rect.y+= self.speed





hero1 = Player1('Simpson1.png',100 ,250, 68,100, 15)




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



    hero1.update_l()
    hero1.reset()

    display.update()
    clock.tick(FPS)
