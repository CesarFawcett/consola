import pygame

size = (650, 750)
carril_width = size[0] // 5

class Enemy:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move_down(self):
        self.y += 1
