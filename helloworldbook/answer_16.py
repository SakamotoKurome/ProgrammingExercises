import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pygame.draw.polygon(screen, [0, 0, 0], [
    [50, 50], [100, 50], [100, 100], [50, 100]], 1)
pygame.display.flip()
pygame.draw.ellipse(screen, [0, 0, 0], [200, 200, 100, 50], 1)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
