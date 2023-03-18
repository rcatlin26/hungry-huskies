import pygame

class Food:
    def __init__(self, img, x, y, speed):
        self.img = pygame.image.load(img)
        self.pos = [x, y]
        self.xcent = self.pos[0] + 25
        self.speed = speed

    def move(self):
        self.pos[1] += self.speed
    
    def totop(self):
        self.pos[1] = 0