from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,palyer_x,player_y,w,h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = palyer_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):
    def update_R(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 330:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update_L(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 330:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        

window = display.set_mode((700,500))
display.set_caption('Горячее яйцо')
background = transform.scale(image.load('font.jpg'),(700,500))
font.init()
font1 = font.SysFont('Arial',70)
font2 = font.SysFont('Arial',30)
win = font1.render('YOU WIN!',True,(255,215,0))
lose = font1.render('YOU LOSE!',True,(255,215,0))



player1 = Player('1 player.png',50,200,100,170,5)
player2 = Player('2 player.png',550,200,100,170,5)


egg = GameSprite('egg.png',325,250,50,60,3)


clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))


        egg.rect.x += speed_x
        egg.rect.y += speed_y
    
    
        
        player1.update_R()
        player1.reset()
        player2.update_L()
        player2.reset()
        egg.update()
        egg.reset()


        if egg.rect.y <= 0 or egg.rect.y >= 440:
            speed_y *= -1
        if  sprite.collide_rect(player1,egg) or sprite.collide_rect(player2,egg):
            speed_x *= -1
        

    clock.tick(FPS)
    display.update()
