import random
import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
for i in range(100):
    width = random.randint(0, 320)
    height = random.randint(0, 240)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    pygame.draw.rect(screen, [R, G, B], [left, top, width, height], 0)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
