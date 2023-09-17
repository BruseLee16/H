import pygame
from pygame.locals import *

pygame.init()

# Створення вікна гри
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Доганялки")

# Завантаження та масштабування фонового зображення
background = pygame.transform.scale(pygame.image.load("g.jpg"), (700, 500))

# Початкові позиції спрайтів
x1 = 100
y1 = 300

x2 = 300
y2 = 300

# Завантаження та масштабування зображень спрайтів
sprite1 = pygame.transform.scale(pygame.image.load("i.png"), (100, 100))
sprite2 = pygame.transform.scale(pygame.image.load("p.png"), (100, 100))

# Швидкість руху спрайтів
speed = 10

run = True
clock = pygame.time.Clock()
FPS = 60

# Функція для перевірки зіткнення спрайтів
def check_collision(x1, y1, x2, y2):
    if abs(x1 - x2) < 100 and abs(y1 - y2) < 100:
        return True
    return False

# Функція для відображення переможця
def display_winner():
    font = pygame.font.SysFont("Arial", 60)
    text = font.render("Wins!!!!!!!!!", True, (0, 255, 0))
    window.blit(text, (200, 200))

while run:
    # Відображення фонового зображення та спрайтів
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    # Керування першим спрайтом гравцем 1
    if keys[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys[K_UP] and y1 > 5:
        y1 -= speed
    if keys[K_DOWN] and y1 < 395:
        y1 += speed

    # Керування другим спрайтом гравцем 2
    if keys[K_a] and x2 > 5:
        x2 -= speed
    if keys[K_d] and x2 < 595:
        x2 += speed
    if keys[K_w] and y2 > 5:
        y2 -= speed
    if keys[K_s] and y2 < 395:
        y2 += speed
    
    # Перевірка зіткнення спрайтів
    if check_collision(x1, y1, x2, y2):
        display_winner()
        run = False
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()