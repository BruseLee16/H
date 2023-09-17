from typing import Any
from pygame import *
from pygame.sprite import AbstractGroup

win_width = 700
win_height = 500

win = display.set_mode((win_width, win_height))
display.set_caption("Maze")
beckground = transform.scale(image.load("g.jpg"), (win_width, win_height ))
end = transform.scale(image.load("s.jpg"), (win_width, win_height ))
class GameSprite(sprite.Sprite):
    def __init__(self, imeage, x, y, speed):
        super().__init__
        self.image = transform.scale(image.load(imeage), (65, 65))
        self.speed = speed


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset (self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self,):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and  self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.y += self.speed   

class Enemy(GameSprite):
    def __init__(self, playre_imeage, x, y, speed):
        super().__init__(playre_imeage, x, y, speed)
        self.direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"

        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed

        if self.direction == "right":
            self.rect.x += self.speed

class wall(sprite.Sprite):
    def __init__(self, color, x, y, w, h):
        super().__init__()
        self.color = color
        self.w = w
        self.h = h

        self.image = Surface((self.w, self.h))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset (self):
        win.blit(self.image, (self.rect.x, self.rect.y))

game = True
finish = False
clock = time.Clock()
FPS = 60

player = Player('i.png', 5, win_height - 80, 4)
monstr = Enemy ('p.png', win_width - 80, 280, 2)
exite = GameSprite('ex.png', 600, 400,0 )

color = (154, 205, 50)
w1 = wall(color, 100, 20, 450, 10)
w2 =  wall(color, 100, 480, 350, 10)
w3 =  wall(color, 100, 20, 10, 380)
w4 =  wall(color, 200, 130, 10, 350)
w5 =  wall(color, 450, 130, 10, 360)
w6 =  wall(color, 300, 20, 10, 350)
w7 =  wall(color, 390, 120, 130, 10)

w_list = (w1, w2, w3, w4, w5, w6, w7)
mixer.init()
mixer.music.load("mz.mp3")
mixer.music.play(100)
lose_sount = mixer.Sound("ly.mp3")
win_sount = mixer.Sound("x.mp3") 

font.init()
f = font.Font(None, 70)
win_text = f.render("You Win!", True, (255, 215, 0))
lose_text = f.render("You Lose!", True, (255, 215, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        win.blit(beckground, (0, 0))
        player.update()
        player.reset()
        monstr.update()
        monstr.reset()
        exite.reset()
        w1.reset()
        w2.reset()
        w3.reset()
        w4.reset()
        w5.reset()
        w6.reset()
        w7.reset()


        for w in w_list:
            if player.rect.colliderect(monstr.rect) or player.rect.colliderect(w.rect):
                finish = True
                win.blit(lose_text, (200, 200))
                lose_sount.play()
                mixer.music.stop()
        if player.rect.colliderect(exite.rect):
            finish = True
            win.blit(win_text, (200, 200))
            win_sount.play()
            win.blit(end, (0, 0))
            mixer.music.stop()
    if player.rect.colliderect(monstr.rect):
        pass
    
    display.update()
    clock.tick(FPS)
















