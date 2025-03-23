from pygame import *
from random import randint
from random import choice

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
        if key_pressed[K_w] and self.rect.y>10:
            self.rect.y-= self.speed 
        if key_pressed[K_s] and self.rect.y<450 - 10-self.rect.width:
            self.rect.y+= self.speed
class Player2(Game_sprite):
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>10:
            self.rect.y-= self.speed 
        if key_pressed[K_DOWN] and self.rect.y<450 - 10-self.rect.width:
            self.rect.y+= self.speed

class Ball(Game_sprite):
    
    def __init__(self, img, x,y, w,h, speed):
        super().__init__(img, x,y, w,h, speed)
        self.direct = [0,0]

    def update(self):
        global score_l,score_r
        self.rect.x += self.speed*self.direct[0]
        self.rect.y += self.speed*self.direct[1]
        if self.rect.y<=0 or self.rect.y>=500-self.rect.height:
            self.direct[1]*=-1
        # if self.rect.x<=0 or self.rect.x>=700-self.rect.width:
        #     self.direct[0]*=-1
        if self.rect.colliderect(hero1) or self.rect.colliderect(hero2):
            self.direct[0]*=-1
        if self.rect.x<=0:
            score_r+=1
            self.start()
        if self.rect.x>=700-self.rect.width:
            score_l+=1
            self.start()

    def start(self):
        self.rect.x = 325
        self.rect.y = 225
        ball.direct[0]= choice([-1,1])
        ball.direct[1]= choice([-1,1])
        





hero1 = Player1('Simpson1-Photoroom.png',15 ,250, 150,100, 15)
hero2 = Player2('Simpson (2)-Photoroom.png',600 ,250, 68,100, 15)
ball = Ball('Ponchick(1)-Photoroom.png',350-25,250-25,50,50,5)
ball.direct[0]= choice([-1,1])
ball.direct[1]= choice([-1,1])

# подключение музыки
mixer.init()
mixer.music.load("miusic.mp3")
mixer.music.play()

game = True

score_l = 0
score_r = 0
rule = 3

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

    hero2.update_r()
    hero2.reset()

    ball.reset()
    ball.update()

    display.update()
    clock.tick(FPS)
