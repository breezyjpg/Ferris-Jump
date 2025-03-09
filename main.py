import pygame
import os
import sys
import random

WIN_WIDTH = 500
WIN_HEIGHT = 700

BG_IMG = pygame.image.load(os.path.join("images", "background.png"))
CRAB_IMG = pygame.image.load(os.path.join("images", "crab.png"))
PLAT_IMG = pygame.image.load(os.path.join("images", "plate.png"))

class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_game_over(win, score):
    font = pygame.font.SysFont("comicsans", 50)
    text = font.render("GAME OVER!", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    win.blit(text, (WIN_WIDTH // 2 - text.get_width() // 2, WIN_HEIGHT // 3))
    win.blit(score_text, (WIN_WIDTH // 2 - score_text.get_width() // 2, WIN_HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)  # Pause for 2 seconds

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Ferris Jump")

pygame.font.init()
SCORE_FONT = pygame.font.SysFont("comicsans", 30)
plates = [Plat(random.randrange(0, WIN_WIDTH), random.randrange(0, WIN_HEIGHT)) for i in range(10)]

x = 100
y = 100
dy = 0.0
h = 200
score = 0

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.blit(BG_IMG, (0, 0))

    for plat in plates:
        win. blit(PLAT_IMG, (plat.x, plat.y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 4
        CRAB_IMG = pygame.image.load(os.path.join("images", "crab.png"))
    if keys[pygame.K_RIGHT]:
        x += 4
        CRAB_IMG = pygame.transform.flip(pygame.image.load(os.path.join("images", "crab.png")),True, False)

    if y < h:
        y = h
        for plat in plates:
            plat.y = plat.y - dy
            if plat.y > WIN_HEIGHT:
                plat.y = 0
                plat.x = random.randrange(0,WIN_WIDTH)
                score += 1

    dy += 0.1
    y += dy

    if y > WIN_HEIGHT:
        draw_game_over(win, score)
        sys.exit()

    for plat in plates:
        if (x+50 > plat.x) and (x+20 < plat.x +68) and (y+70 > plat.y) and (y+70 <plat.y +14) and dy >0:
            dy = -9

    text = SCORE_FONT.render("Score: " +str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    win.blit(CRAB_IMG, (x,y))

    pygame.display.update()
