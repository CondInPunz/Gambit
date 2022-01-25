import pygame
import os


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def load_image_fnap(name):
    fullname = os.path.join('fnap_img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    return image


def load_image_menu(name):
    fullname = os.path.join('menu_img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    return image
