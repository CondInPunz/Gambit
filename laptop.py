import pygame


class Laptop(pygame.sprite.Sprite):
    rooms_cams_accordance = {
        1: 4,
        2: 5,
        3: 6,
        4: 3,
        5: 8,
        6: 9,
        7: 10,
        8: 5
    }

    def __init__(self, screen, start_image, caught_looks, uncaught_looks, puppet):
        super().__init__()
        self.is_open = False
        self.is_caught = True
        self.screen = screen
        self.closed_image = start_image
        self.image = start_image
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 420
        self.cam = 1
        self.caught_looks = caught_looks
        self.uncaught_looks = uncaught_looks
        self.puppet = puppet

    def open(self):
        self.is_open = True
        if self.is_caught:
            self.image = self.caught_looks[0]
        else:
            self.image = self.uncaught_looks[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def close(self):
        self.is_open = False
        self.image = self.closed_image
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 420

    def catch(self):
        if Laptop.rooms_cams_accordance[self.cam] == self.puppet.room:
            self.is_caught = True
        else:
            self.is_caught = False
        print(self.is_caught)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            return True

    def establish_accordance(self):
        if self.is_open:
            if self.is_caught:
                self.image = self.caught_looks[self.cam - 1]
            else:
                self.image = self.uncaught_looks[self.cam - 1]
