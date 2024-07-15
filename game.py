import pygame
import sys
import time

pygame.init()

width = 700
height = 500

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

ship_width = 40
ship_height = 30

background = (74, 35, 90)
white = (244, 246, 247)
yellow = (241, 196, 15)
orange = (186, 74, 0)
green = (35, 155, 86)
white1 = (253, 254, 254)
dark_gray = (23, 32, 42)

class SpaceShip:
    def __init__(self, x, y, w, h, colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour

    def draw(self):
        pygame.draw.rect(display, yellow, (self.x + self.w/2 - 8, self.y - 10, 16, 10))
        pygame.draw.rect(display, self.colour, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(display, dark_gray, (self.x + 5, self.y + 6, 10, self.h - 10))
        pygame.draw.rect(display, dark_gray, (self.x + self.w - 15, self.y + 6, 10, self.h - 10))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 10
        self.speed = -5

    def draw(self):
        pygame.draw.ellipse(display, orange, (self.x, self.y, self.d, self.d))

    def move(self):
        self.y += self.speed

    def hit(self, x, y, d):
        if x < self.x < x + d:
            if y + d > self.y > y:
                return True

class Alien:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.x_dir = 1
        self.speed = 3

    def draw(self):
        pygame.draw.ellipse(display, green, (self.x, self.y, self.d, self.d))
        pygame.draw.ellipse(display, dark_gray, (self.x + 10, self.y + self.d/3, 8, 8), 2)
        pygame.draw.ellipse(display, dark_gray, (self.x + self.d - 20, self.y + self.d/3, 8, 8), 2)
        pygame.draw.rect(display, dark_gray, (self.x, self.y+self.d-20, 50, 7))

    def move(self):
        self.x += self.x_dir*self.speed

    def shift_down(self):
        self.y += self.d
