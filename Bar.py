import pygame

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


class Bar:
    def __init__(self, width, height, value=0):
        self.width = width
        self.height = height
        self.value = value
        self.active = False

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, BLUE if self.active else BLACK, (x, y, self.width, self.height))

    def __lt__(self, other):
        return float(self) < float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __eq__(self, other):
        return float(self) == float(other)

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)

    def __mul__(self, other):
        return self.value * other

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __truediv__(self, other):
        return self.value / other

    def __abs__(self):
        return abs(self.value)

    def __floordiv__(self, other):
        return int(self.value / other)