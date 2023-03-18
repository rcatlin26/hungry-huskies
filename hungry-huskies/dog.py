import pygame

class Dog:
    def __init__(self, img, name, favfood, x, y):
        self.img = pygame.image.load(img)
        self.name = name
        self.favfood = favfood
        self.pos = [x, y]
        self.xcent = self.pos[0] + 50