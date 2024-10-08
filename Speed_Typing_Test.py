import pygame
from pygame.locals import *
import sys
import time 
import random
import os

class typing_Test:
    def __init__(self):
        pygame.init()  # Pygame modüllerini başlatır
        self.w = 960
        self.h = 540
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = "0%"
        self.results = 'Time:0 Accuracy:0 %Wpm:0'
        self.wpm = 0
        self.end = 0
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Type Speed Test')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        if os.path.exists('sentences.txt'):
            with open('sentences.txt') as f:
                sentences = f.read().splitlines()
            sentence = random.choice(sentences)
        else:
            fallback_sentences = [
                "The quick brown fox jumps over the lazy dog.",
                "Python is a powerful programming language.",
                "Pygame is great for making games in Python."
            ]
            sentence = random.choice(fallback_sentences)
        return sentence

    def show_results(self, screen):
        if not self.end:
            self.total_time = time.time() - self.time_start
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.word) * 100
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True
            self.results = f'Time:{round(self.total_time)} secs  Accuracy:{round(self.accuracy)}%  Wpm:{round(self.wpm)}'
            self.draw_text(screen, self.results, 350, 28, self.RESULT_C)
            self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))
            pygame.display.update()

    def run(self):
        self.reset_game()
        self.running = True
        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 650 and 250 <= y <= 300:
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                    if 310 <= x <= 510 and y >= 390 and self.end:
                        self.reset_game()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            self.show_results(self.screen)
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            self.input_text += event.unicode
            pygame.display.update()
            clock.tick(60)

    def reset_game(self):
        self.reset = False
        self.end = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0
        self.word = self.get_sentence()
        if not self.word:
            self.reset_game()
        self.screen.fill((0, 0, 0))
        msg = "Typing Speed Test"
        self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)
        self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)
        pygame.display.update()

typing_Test().run()





        


