import pygame
import sys
import os


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass


def load_image(name):
    fullname = os.path.join('fnap_img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
