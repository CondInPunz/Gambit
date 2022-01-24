import pygame
import controls


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('UMSDHGC')
    size = width, height = 960, 720
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        office_img = controls.load_image('office.BMP')
        office_img = pygame.transform.scale(office_img, (960, 720))
        screen.blit(office_img, (0, 0))

        pygame.display.flip()
    pygame.quit()


