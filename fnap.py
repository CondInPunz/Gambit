import pygame
import controls
from laptop import Laptop
from puppet import Puppet
from button import Button
from door import Door
from scene import Scene

SCR_WIDTH, SCR_HEIGHT = 720, 540
MAIN_MENU = 0
LOAD_GAME = 1
GAME_MODE = 2
GAME_OVER = 3

def main():
    pygame.init()
    pygame.display.set_caption('FNAP')
    size = SCR_WIDTH, SCR_HEIGHT
    screen = pygame.display.set_mode(size)
    game_state = MAIN_MENU
    difficulty_lvl = 1

    main_scene = Scene(screen)

    '''обработка всех картинок'''
    office_img = controls.load_image_fnap('office.BMP')
    office_img = pygame.transform.scale(office_img, (720, 540))

    main_menu_img = controls.load_image_fnap('main_menu.BMP')
    main_menu_img = pygame.transform.scale(main_menu_img, (720, 540))

    first_night_btn_image = controls.load_image_fnap("1st_night.png")
    first_night_btn_image = pygame.transform.scale(first_night_btn_image, (300, 100))

    second_night_btn_image = controls.load_image_fnap("2st_night.png")
    second_night_btn_image = pygame.transform.scale(second_night_btn_image, (300, 100))

    third_night_btn_image = controls.load_image_fnap("3st_night.png")
    third_night_btn_image = pygame.transform.scale(third_night_btn_image, (300, 100))

    fourth_night_btn_image = controls.load_image_fnap("4st_night.png")
    fourth_night_btn_image = pygame.transform.scale(fourth_night_btn_image, (300, 100))

    fifth_night_btn_image = controls.load_image_fnap("5st_night.png")
    fifth_night_btn_image = pygame.transform.scale(fifth_night_btn_image, (300, 100))

    first_night_image = controls.load_image_fnap("1st_night.BMP")
    first_night_image = pygame.transform.scale(first_night_image, (720, 540))

    second_night_image = controls.load_image_fnap("2st_night.BMP")
    second_night_image = pygame.transform.scale(second_night_image, (720, 540))

    third_night_image = controls.load_image_fnap("3st_night.BMP")
    third_night_image = pygame.transform.scale(third_night_image, (720, 540))

    fourth_night_image = controls.load_image_fnap("4st_night.BMP")
    fourth_night_image = pygame.transform.scale(fourth_night_image, (720, 540))

    fifth_night_image = controls.load_image_fnap("5st_night.BMP")
    fifth_night_image = pygame.transform.scale(fifth_night_image, (720, 540))

    game_over_image = controls.load_image_fnap("GAME_OVER.BMP")
    game_over_image = pygame.transform.scale(game_over_image, (720, 540))

    cam_icons = []
    for i in range(8):
        cam_icon = controls.load_image_fnap(f"icon_cam{i + 1}.BMP")
        cam_icons.append(cam_icon)

    caught_cam_looks = []
    for i in range(5):
        caught_cam_look = controls.load_image_fnap(f"CAM{i + 1}+.BMP")
        caught_cam_look = pygame.transform.scale(caught_cam_look, (720, 540))
        caught_cam_looks.append(caught_cam_look)
    sixth_caught_cam_look = controls.load_image_fnap(f"CAM6.1+.BMP")
    sixth_caught_cam_look = pygame.transform.scale(sixth_caught_cam_look, (720, 540))
    caught_cam_looks.append(sixth_caught_cam_look)
    sixth_caught_cam_look2 = controls.load_image_fnap(f"CAM6.2+.BMP")
    sixth_caught_cam_look2 = pygame.transform.scale(sixth_caught_cam_look2, (720, 540))
    caught_cam_looks.append(sixth_caught_cam_look2)
    for i in range(6, 8):
        caught_cam_look = controls.load_image_fnap(f"CAM{i + 1}+.BMP")
        caught_cam_look = pygame.transform.scale(caught_cam_look, (720, 540))
        caught_cam_looks.append(caught_cam_look)

    uncaught_cam_looks = []
    for i in range(8):
        uncaught_cam_look = controls.load_image_fnap(f"CAM{i + 1}-.BMP")
        uncaught_cam_look = pygame.transform.scale(uncaught_cam_look, (720, 540))
        uncaught_cam_looks.append(uncaught_cam_look)

    scheme_image = controls.load_image_fnap('scheme.BMP')

    closed_laptop_img = controls.load_image_fnap("panel.BMP")
    closed_laptop_img = pygame.transform.scale(closed_laptop_img, (500, 200))

    jumpscare_img = controls.load_image_fnap("jumpscare.BMP")
    jumpscare_img = pygame.transform.scale(jumpscare_img, (1, 1))

    '''ивенты загрузки'''
    LOADEVENTTYPE = pygame.USEREVENT + 1
    load_game_count_started = False
    is_first_menu_load = True
    is_first_lost_game = True

    '''логика игры'''
    is_first_run = True
    game_lost = False
    room = 4
    CHANGEROOMTYPE = LOADEVENTTYPE + 1

    running = True
    while running:
        if game_state == MAIN_MENU:
            if is_first_menu_load:
                main_menu_btns = pygame.sprite.Group()
                first_night_btn = Button(screen, first_night_btn_image, 10, 175)
                main_menu_btns.add(first_night_btn)

                second_night_btn = Button(screen, second_night_btn_image, 10, 225)
                main_menu_btns.add(second_night_btn)

                third_night_btn = Button(screen, third_night_btn_image, 10, 275)
                main_menu_btns.add(third_night_btn)

                fourth_night_btn = Button(screen, fourth_night_btn_image, 10, 325)
                main_menu_btns.add(fourth_night_btn)

                fifth_night_btn = Button(screen, fifth_night_btn_image, 10, 375)
                main_menu_btns.add(fifth_night_btn)

                is_first_menu_load = False
                main_scene.set_background(main_menu_img)
                main_menu_btns.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if first_night_btn.update(event):
                        game_state = LOAD_GAME
                        difficulty_lvl = 1
                        is_first_menu_load = True
                    if second_night_btn.update(event):
                        game_state = LOAD_GAME
                        difficulty_lvl = 2
                        is_first_menu_load = True
                    if third_night_btn.update(event):
                        game_state = LOAD_GAME
                        difficulty_lvl = 3
                        is_first_menu_load = True
                    if fourth_night_btn.update(event):
                        game_state = LOAD_GAME
                        difficulty_lvl = 4
                        is_first_menu_load = True
                    if fifth_night_btn.update(event):
                        game_state = LOAD_GAME
                        difficulty_lvl = 5
                        is_first_menu_load = True

        if game_state == LOAD_GAME:
            if difficulty_lvl == 1:
                main_scene.set_background(first_night_image)
            if difficulty_lvl == 2:
                main_scene.set_background(second_night_image)
            if difficulty_lvl == 3:
                main_scene.set_background(third_night_image)
            if difficulty_lvl == 4:
                main_scene.set_background(fourth_night_image)
            if difficulty_lvl == 5:
                main_scene.set_background(fifth_night_image)

            if not load_game_count_started:
                pygame.time.set_timer(LOADEVENTTYPE, 2000, 1)
                load_game_count_started = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == LOADEVENTTYPE:
                    print('игра запущена')
                    game_state = GAME_MODE
                    load_game_count_started = False

        if game_state == GAME_MODE:
            if is_first_run:
                main_scene.set_background(office_img)
                pygame.time.set_timer(CHANGEROOMTYPE, 4000 // difficulty_lvl)
                puppet = Puppet()

                laptop = Laptop(screen, closed_laptop_img, caught_cam_looks, uncaught_cam_looks, puppet)
                laptops = pygame.sprite.Group()
                laptops.add(laptop)

                cam_buttons = pygame.sprite.Group()
                for i in range(8):
                    cam_button = Button(screen, cam_icons[i], 0, 0)
                    cam_buttons.add(cam_button)
                jumpscares = pygame.sprite.Group
                is_first_run = False
            main_scene.set_background(office_img)
            laptop.catch()
            laptops.draw(screen)
            laptop.establish_accordance()
            if laptop.is_open:
                cam_buttons.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == CHANGEROOMTYPE:
                    if not puppet.is_attacking:
                        puppet.change_room()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if laptop.update(event):
                        if not laptop.is_open:
                            laptop.open()
                        else:
                            laptop.close()

            if puppet.is_attacking:
                game_state = GAME_OVER
                is_first_run = True

        if game_state == GAME_OVER:
            main_scene.set_background(game_over_image)
            if is_first_lost_game:
                pygame.time.set_timer(LOADEVENTTYPE, 3000, 1)
                is_first_lost_game = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == LOADEVENTTYPE:
                    game_state = MAIN_MENU
                    is_first_lost_game = True

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
