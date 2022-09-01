from Bar import Bar
import pygame
from time import time, sleep


class Bars:
    def __init__(self, array, x, y, width, height, screen=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        max_height = max(abs(a) for a in array)
        if max_height == 0: max_height = 1

        self.bars = [Bar(width / max(len(array),1), int(height * (value / max_height)), value) for value in array]
        self.__array = array
        self.moves = 0
        self.sleep_time = 1 / (len(array) + 1)
        self.start = time()
        self.screen = screen
        pygame.font.init()
        self.font_size = 30
        self.font = pygame.font.SysFont('mokoto', self.font_size)

    def draw(self, screen):
        for index, bar in enumerate(self.bars):
            y = self.y + self.height - bar.height
            x = self.x + index * bar.width
            bar.draw(screen, x, y)

    def __getitem__(self, item):
        if isinstance(item, slice):
            # self,array,x,y,width, height
            print(item.start, item.stop)
            return Bars(array=self.__array[item],
                        x=self.x + self.width / len(self.bars) * (item.start if item.start is not None else 0),
                        y=self.y,
                        width=self.width / len(self.bars) * (item.stop if item.stop is not None else len(self.bars)
                                                                                                     -
                                                                                                     item.start if item.start is not None else len(
                            self.bars)),
                        height=self.height,
                        screen=self.screen
                        )

        return self.bars[item]

    def __setitem__(self, key, value):
        self.bars[key] = value

    def __len__(self):
        return len(self.bars)

    def render_steps(self, screen):
        self.text = self.font.render(f"Steps : {self.moves}", False, (0, 0, 0))
        screen.blit(self.text, (0, 0))

    def render_time(self, screen):
        self.text = self.font.render(f"Time : {round(time() - self.start, 2)}", False, (0, 0, 0))
        screen.blit(self.text, (0, self.font_size))

    def setup(self):
        self.start = time()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        self.screen.fill((255, 255, 255))
        self.draw(self.screen)
        self.render_steps(self.screen)
        self.render_time(self.screen)
        pygame.display.flip()
