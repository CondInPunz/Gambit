import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, screen, image):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 420

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            return True
