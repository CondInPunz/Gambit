import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, image, x, y):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            return True

    def set_pos(self, coords):
        self.rect.x, self.rect.y = coords
