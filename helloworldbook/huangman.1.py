import pygame
import sys
import random


class HuangMan():
    def __init__(self):
        # 已猜测的字母
        self.guessed_letters = []

        self.set_man_info()
        self.set_word_info()
        self.get_default_info()
        self.get_guessed_result()

    # self.man_body 一个人形图像相关信息
    # self.man_body[0] 人形身体每一部分的颜色，控制该部分是否可以看见
    # self.man_body[0] 人形身体还有那些部分不可见
    def set_man_info(self):
        man_body = [[], []]
        for i in range(6):
            man_body[0].append([255, 255, 255])
            man_body[1].append(i)
        self.man_body = man_body

    # self.guess_word 从文件中随机获取的一个单词
    # self.guessed_result 根据单词的长度初始化猜测结果字符串
    def set_word_info(self):
        words = []
        file_obj = open('hangman_words.txt', 'r')
        for line in file_obj.readlines():
            words.append(line.strip())
        file_obj.close()
        self.guess_word = random.choice(words)
        guessed_result = ''
        for i in range(len(self.guess_word)):
            guessed_result += '-'
        self.guessed_result = guessed_result

    # 游戏过程中不会变动的部分
    def get_default_info(self):
        # 吊人的架子
        pygame.draw.lines(screen, [0, 0, 0], False, [
                          [100, 70], [100, 40]], 2)
        pygame.draw.lines(screen, [0, 0, 0], False, [
                          [100, 40], [200, 40]], 2)
        pygame.draw.lines(screen, [0, 0, 0], False, [
                          [200, 40], [200, 300]], 2)
        pygame.draw.lines(screen, [0, 0, 0], False, [
                          [150, 300], [250, 300]], 2)
        # "Your Guesses:" 标题
        screen.blit(font.render(
            str("Your Guesses:"), 1, (0, 0, 0)), [20, 350])
        pygame.display.flip()

    # 游戏过程中随状态变化的部分
    def get_guessed_result(self):
        # 人形图像身体各部分
        # 头
        pygame.draw.circle(screen,
                           self.man_body[0][0], [100, 100], 20, 2)
        # 身体
        pygame.draw.lines(screen, self.man_body[0][1],
                          False, [[100, 120], [100, 200]], 2)
        # 左手
        pygame.draw.lines(screen, self.man_body[0][2],
                          False, [[45, 140], [90, 140]], 2)
        # 右手
        pygame.draw.lines(screen, self.man_body[0][3],
                          False, [[110, 140], [155, 140]], 2)
        # 左腿
        pygame.draw.lines(screen, self.man_body[0][4],
                          False, [[95, 205], [80, 250]], 2)
        # 右腿
        pygame.draw.lines(screen, self.man_body[0][5],
                          False, [[105, 205], [120, 250]], 2)
        # 清除并显示单词猜测的状态
        pygame.draw.rect(screen, [255, 255, 255], [400, 180, 200, 50], 0)
        screen.blit(font.render(
            self.guessed_result, 1, (0, 0, 0)), [400, 180])
        # 显示已经猜测的字母
        screen.blit(font.render(
            ' '.join(self.guessed_letters), 1, (0, 0, 0)), [40, 400])
        pygame.display.flip()


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


pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()
game = HuangMan()
done = False

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if 94 <= event.key <= 122:
                if not done:
                    letter = pygame.key.name(event.key)
                    if not letter in game.guessed_letters:
                        game.guessed_letters.append(letter)
                    locations = find_letters(letter, game.guess_word)
                    if locations:
                        game.guessed_result = replace_letters(
                            game.guessed_result, locations, letter)
                        if game.guessed_result == game.guess_word:
                            done = True
                    else:
                        index = random.choice(game.man_body[1])
                        game.man_body[0][index] = [0, 0, 0]
                        game.man_body[1].remove(index)
                        if not game.man_body[1]:
                            done = True
                    game.get_guessed_result()
                else:
                    done = True

    if done:
        pygame.time.delay(1000)
        if game.guessed_result == game.guess_word:
            screen.fill([0, 255, 0])
            screen.blit(font.render('You Win!', 1, (0, 0, 0)), [250, 240])
        else:
            screen.fill([255, 0, 0])
            screen.blit(font.render('You lost!', 1, (0, 0, 0)), [250, 240])
        pygame.display.flip()
        # 重新开始游戏
        pygame.time.delay(3000)
        screen.fill([255, 255, 255])
        done = False
        game = HuangMan()
