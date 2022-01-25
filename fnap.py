import pygame
import controls

SCR_WIDTH, SCR_HEIGHT = 720, 540
MAIN_MENU = 0
LOAD_GAME = 1
GAME_MODE = 2
GAME_OVER = 3


class Scene:
    def __init__(self, screen):
        self.screen = screen

    def set_background(self, image):
        self.screen.blit(image, (0, 0))


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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('FNAP')
    size = SCR_WIDTH, SCR_HEIGHT
    screen = pygame.display.set_mode(size)
    game_state = MAIN_MENU

    main_scene = Scene(screen)

    '''обработка всех картинок'''
    office_img = controls.load_image_fnap('office.BMP')
    office_img = pygame.transform.scale(office_img, (720, 540))

    main_menu_img = controls.load_image_fnap('main_menu.BMP')
    main_menu_img = pygame.transform.scale(main_menu_img, (720, 540))

    new_game_btn_image = controls.load_image_fnap("new_game_btn_img.png")
    new_game_btn_image = pygame.transform.scale(new_game_btn_image, (300, 100))

    first_night_image = controls.load_image_fnap("1st_night.BMP")
    first_night_image = pygame.transform.scale(first_night_image, (720, 540))

    game_over_image = controls.load_image_fnap("GAME_OVER.BMP")
    game_over_image = pygame.transform.scale(game_over_image, (720, 540))

    '''создание всех кнопок'''
    main_menu_btns = pygame.sprite.Group()
    new_game_btn = Button(screen, new_game_btn_image, 20, 250)
    main_menu_btns.add(new_game_btn)

    '''доп штуки'''
    LOADEVENTTYPE = pygame.USEREVENT + 1
    load_game_count_started = False

    '''логика игры'''
    game_lost = False
    room = 4
    CHANGEROOMTYPE = LOADEVENTTYPE + 1

    running = True
    while running:
        if game_state == MAIN_MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_btn.update(event):
                        game_state = LOAD_GAME
            main_scene.set_background(main_menu_img)
            main_menu_btns.draw(screen)

        if game_state == LOAD_GAME:
            main_scene.set_background(first_night_image)

            if not load_game_count_started:
                pygame.time.set_timer(LOADEVENTTYPE, 2000)
                load_game_count_started = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == LOADEVENTTYPE:
                    print('игра запущена')
                    pygame.time.set_timer(LOADEVENTTYPE, 0)
                    game_state = GAME_MODE

        if game_state == GAME_MODE:
            main_scene.set_background(office_img)
            pygame.time.set_timer(CHANGEROOMTYPE, 2000)
            print('night is on')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == CHANGEROOMTYPE:
                    room += 1
                    print(room)

            if room == 0 or room == 10:
                game_lost = True

            if game_lost:
                game_state = GAME_OVER
        if game_state == GAME_OVER:
            main_scene.set_background(game_lost)

        pygame.display.update()
    pygame.quit()


