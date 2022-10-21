import random
import pygame
import sys


def find_letters(letter, a_string):
    locations = []
    start = 0
    while a_string.find(letter, start, len(a_string)) != -1:
        location = a_string.find(letter, start, len(a_string))
        locations.append(location)
        start = location + 1
    return locations


def replace_letters(string, locations, letter):
    new_string = ''
    for i in range(0, len(string)):
        if i in locations:
            new_string = new_string + letter
        else:
            new_string = new_string + string[i]
    return new_string


def show_result():
    pygame.draw.circle(screen, color[0], [100, 100], 20, 2)
    pygame.draw.lines(screen, color[1], False, [[100, 120], [100, 200]], 2)
    pygame.draw.lines(screen, color[2], False, [[45, 140], [90, 140]], 2)
    pygame.draw.lines(screen, color[3], False, [[110, 140], [155, 140]], 2)
    pygame.draw.lines(screen, color[4], False, [[95, 205], [80, 250]], 2)
    pygame.draw.lines(screen, color[5], False, [[105, 205], [120, 250]], 2)
    pygame.draw.rect(screen, [255, 255, 255], [400, 180, 200, 50], 0)
    screen.blit(font.render(result, 1, (0, 0, 0)), [400, 180])
    screen.blit(font.render(
        ' '.join(guessed), 1, (0, 0, 0)), [40, 400])
    pygame.display.flip()


pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])

color = []
color_index = []
for i in range(6):
    color.append([255, 255, 255])
    color_index.append(i)
pygame.draw.lines(screen, [0, 0, 0], False, [[100, 70], [100, 40]], 2)
pygame.draw.lines(screen, [0, 0, 0], False, [[100, 40], [200, 40]], 2)
pygame.draw.lines(screen, [0, 0, 0], False, [[200, 40], [200, 300]], 2)
pygame.draw.lines(screen, [0, 0, 0], False, [[150, 300], [250, 300]], 2)

font = pygame.font.Font(None, 50)
screen.blit(font.render(str("Your Guesses:"), 1, (0, 0, 0)), [20, 350])

words = []
file_obj = open('hangman_words.txt', 'r')
for line in file_obj.readlines():
    words.append(line.strip())
file_obj.close()
guess = random.choice(words)
result = ''
for i in range(len(guess)):
    result += '-'
screen.blit(font.render(result, 1, (0, 0, 0)), [400, 180])

pygame.display.flip()

guessed = []
clock = pygame.time.Clock()
done = False

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if 94 <= event.key <= 122:
                if not done and not result == guess:
                    letter = pygame.key.name(event.key)
                    if not letter in guessed:
                        guessed.append(letter)
                    locations = find_letters(letter, guess)
                    if locations:
                        result = replace_letters(
                            result, locations, letter)
                    else:
                        index = random.choice(color_index)
                        color[index] = [0, 0, 0]
                        color_index.remove(index)
                        if not color_index:
                            done = True
                    show_result()
                else:
                    done = True

    if done:
        pygame.time.delay(2000)
        if result == guess:
            screen.fill([0, 255, 0])
            screen.blit(font.render('You Win!', 1, (0, 0, 0)), [250, 240])
        else:
            screen.fill([255, 0, 0])
            screen.blit(font.render('You lost!', 1, (0, 0, 0)), [250, 240])
        pygame.display.flip()
