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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 645:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        

window = display.set_mode((700,500))
display.set_caption('Горячее яйцо')
background = transform.scale(image.load('font.jpg'),(700,500))
font.init()
font1 = font.SysFont('Arial',70)
font2 = font.SysFont('Arial',30)
win = font1.render('YOU WIN!',True,(255,215,0))
lose = font1.render('YOU LOSE!',True,(255,215,0))



player1 = Player('1 player.png',0,200,100,170,5)
player2 = Player('2 player.jpg',600,200,100,170,5)


clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
    
        
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()

    clock.tick(FPS)
    display.update()