import pygame

size = (650, 750)
carril_width = size[0] // 5

class Player:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def move_left(self):
        if self.x > carril_width:
            self.x -= carril_width

    def move_right(self):
        if self.x < 4 * carril_width:
            self.x += carril_width

    def draw(self, screen):
        screen.blit(self.image, (self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()
