import pygame
import sys
import random
import fnap
import os


def score_of_game(score):
    implication = font_of_score.render(str(score), True, (255, 255, 102))
    place = implication.get_rect(bottomright=(685, 100))
    screen.blit(implication, place)


def message(message_1, color_1):
    mes = font.render(message_1, True, color_1)
    screen.blit(mes, [display_width / 3, display_height / 6])


def message_2(message_2, color_2):
    mes2 = font.render(message_2, True, color_2)
    screen.blit(mes2, [display_width / 50, display_height / 3])


def start():
    screen.fill('#1b2838')
    krest = pygame.image.load('крест_ноль.png')
    null = krest.get_rect(midleft=(50, 290))
    snake = pygame.transform.scale(pygame.image.load('змейка1.png'), (197, 200))
    snake_print = krest.get_rect(midleft=(300, 290))
    fnaf = pygame.image.load('fnaf.png')
    fnaf_print = krest.get_rect(midleft=(515, 280))
    steam = pygame.transform.scale(pygame.image.load('steam.png'), (100, 100))
    steam_print = krest.get_rect(midleft=(30, 125))
    screen.blit(krest, null)
    screen.blit(snake, snake_print)
    screen.blit(fnaf, fnaf_print)
    screen.blit(steam, steam_print)


def win(mas, znak):
    for_future = 0
    for row in mas:
        for_future += row.count('')
        if row.count(znak) == 3:
            return znak
    for col in range(3):
        if mas[0][col] == znak and mas[1][col] == znak and mas[2][col] == znak:
            return znak
    if mas[0][0] == znak and mas[1][1] == znak and mas[2][2] == znak:
        return znak
    if mas[0][2] == znak and mas[1][1] == znak and mas[2][0] == znak:
        return znak
    if for_future == 0:
        return 'Дружба'
    return None


pygame.init()
font = pygame.font.SysFont("bahnschrift", 25)
font_of_score = pygame.font.SysFont("comicsansms", 35)
main_menu = pygame.font.SysFont("etna", 100)
podpisi = pygame.font.SysFont("etna", 35)
field = 10
speed_run = 15
time_of_game = pygame.time.Clock()
krest = pygame.image.load('крест_ноль.png')
game_state = 'MainMenu'
square = 146
margin = 25
width = 720
height = 540
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Гамбит')
start()
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
zone = [[''] * 3 for i in range(3)]
krest_or_null = 0
end = False
start_krest = 0
start_snake = 0
start_fnaf = 0
display_width = 720
display_height = 540
fps = 30
clock = pygame.time.Clock()
r = 0
game_lose = False
game_close = False
x_snake = display_width / 2
y_snake = display_height / 2
num = 0
x_change = 0
y_change = 0
enumerate = []
length_of_tors = 1
movement_x = round(random.randrange(90, 540 - field) / 10.0) * 10.0
movement_y = round(random.randrange(0, display_height - field) / 10.0) * 10.0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if not end:
                if game_state == 'MainMenu':
                    if 50 <= x <= 255 and 190 <= y <= 390:
                        game_state = 'KrestNull'
                        screen.fill('#1b2838')
                    if 300 <= x <= 497 and 190 <= y <= 390:
                        game_state = 'Snake'
                        screen.fill('#1b2838')
                    if 550 <= x <= 739 and 190 <= y <= 390:
                        game_state = 'fnap'
                elif game_state == 'KrestNull':
                    if 115 < x < 605 and 25 < y < 515:
                        col = (x - 90) // (square + margin)
                        row = y // (square + margin)
                        if zone[row][col] == '':
                            if krest_or_null % 2 == 0:
                                zone[row][col] = 'x'
                            else:
                                zone[row][col] = 'o'
                            krest_or_null += 1
            if game_state == 'KrestNull':
                if 5 < x < 107 and 25 < y < 120:
                    start()
                    game_state = 'MainMenu'
                    end = False
                    zone = [[''] * 3 for i in range(3)]
                    krest_or_null = 0
                    r = 0
            elif game_state == 'Snake':
                if 5 < x < 90 and 25 < y < 110:
                    r = 0
                    game_lose = False
                    game_close = False
                    x_snake = display_width / 2
                    y_snake = display_height / 2
                    num = 0
                    x_change = 0
                    y_change = 0
                    enumerate = []
                    length_of_tors = 1
                    movement_x = round(random.randrange(90, 540 - field) / 10.0) * 10.0
                    movement_y = round(random.randrange(0, display_height - field) / 10.0) * 10.0
                    start()
                    game_state = 'MainMenu'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_state == 'KrestNull' and end or game_state == 'Snake' and game_close:
                screen.fill('#1b2838')
                end = False
                zone = [[''] * 3 for i in range(3)]
                krest_or_null = 0
                game_lose = False
                game_close = False
                x_snake = display_width / 2
                y_snake = display_height / 2
                num = 0
                x_change = 0
                y_change = 0
                enumerate = []
                length_of_tors = 1
                movement_x = round(random.randrange(90, 540 - field) / 10.0) * 10.0
                movement_y = round(random.randrange(0, display_height - field) / 10.0) * 10.0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game_state == 'KrestNull' or game_state == 'Snake' or game_state == 'fnap':
                start()
                game_state = 'MainMenu'
                end = False
                zone = [[''] * 3 for i in range(3)]
                krest_or_null = 0
                r = 0
                game_lose = False
                game_close = False
                x_snake = display_width / 2
                y_snake = display_height / 2
                num = 0
                x_change = 0
                y_change = 0
                enumerate = []
                length_of_tors = 1
                movement_x = round(random.randrange(90, 540 - field) / 10.0) * 10.0
                movement_y = round(random.randrange(0, display_height - field) / 10.0) * 10.0
        elif event.type == pygame.KEYDOWN:
            if game_state == 'Snake':
                if event.key == pygame.K_LEFT:
                    if x_change != field and y_change != 0 or num == 0:
                        x_change = -field
                        y_change = 0
                        num = 1
                elif event.key == pygame.K_RIGHT:
                    if x_change != -field and y_change != 0 or num == 0:
                        x_change = field
                        y_change = 0
                        num = 1
                elif event.key == pygame.K_UP:
                    if x_change != 0 and y_change != field or num == 0:
                        y_change = -field
                        x_change = 0
                        num = 1
                elif event.key == pygame.K_DOWN:
                    if x_change != 0 and y_change != -field or num == 0:
                        y_change = field
                        x_change = 0
                        num = 1

    if game_state == 'MainMenu':
        x, y = pygame.mouse.get_pos()
        if 50 <= x <= 255 and 190 <= y <= 390 and start_krest != 50:
            start_krest += 10
        elif (x < 50 or x > 255 or y < 190 or y > 390) and start_krest != 0:
            start_krest -= 10
        if 300 <= x <= 497 and 190 <= y <= 390 and start_snake != 50:
            start_snake += 10
        elif (x < 300 or x > 497 or y < 190 or y > 390) and start_snake != 0:
            start_snake -= 10
        if 550 <= x <= 739 and 190 <= y <= 390 and start_fnaf != 50:
            start_fnaf += 10
        elif (x < 550 or x > 739 or y < 190 or y > 390) and start_fnaf != 0:
            start_fnaf -= 10
        krest_null = pygame.transform.scale(krest, (220 + start_krest, 205 + start_krest))
        null = krest.get_rect(midleft=(50 - (start_krest // 2), 290 - (start_krest // 2)))
        screen.fill('#1b2838')
        snake = pygame.transform.scale(pygame.image.load('змейка1.png'), (197 + start_snake, 200 + start_snake))
        snake_print = krest.get_rect(midleft=(300 - (start_snake // 2), 290 - (start_snake // 2)))
        fnaf = pygame.transform.scale(pygame.image.load('fnaf.png'), (200 + start_fnaf, 200 + start_fnaf))
        fnaf_print = krest.get_rect(midleft=(515 - (start_fnaf // 2), 280 - (start_fnaf // 2)))
        steam = pygame.transform.scale(pygame.image.load('steam.png'), (75, 75))
        steam_print = krest.get_rect(midleft=(15, 120))
        winner = main_menu.render('GAMBIT', True, (255, 0, 0))
        place = winner.get_rect(bottomright=(530, 115))
        kr = podpisi.render('Крестики-нолики', True, (255, 255, 255))
        kr_place = winner.get_rect(bottomright=(335, 485))
        zm = podpisi.render('Змейка', True, (255, 255, 255))
        zm_place = winner.get_rect(bottomright=(635, 485))
        fp = podpisi.render('Fnap', True, (255, 255, 255))
        fp_place = winner.get_rect(bottomright=(850, 485))
        screen.blit(kr, kr_place)
        screen.blit(zm, zm_place)
        screen.blit(fp, fp_place)
        screen.blit(winner, place)
        screen.blit(krest_null, null)
        screen.blit(snake, snake_print)
        screen.blit(fnaf, fnaf_print)
        screen.blit(steam, steam_print)

    if game_state == 'KrestNull':
        if not end:
            back = pygame.transform.scale(pygame.image.load('back.png'), (102, 102))
            back_coords = back.get_rect(midleft=(5, 75))
            screen.blit(back, back_coords)
            x, y = pygame.mouse.get_pos()
            if 5 < x < 107 and 25 < y < 120 and r != 50:
                r += 5
                pygame.draw.circle(screen, '#66c0f4', (57, 75), r)
                clock.tick(fps)
                pygame.display.flip()
                screen.blit(back, back_coords)
            elif (x < 5 or x > 107 or y < 25 or y > 120) and r != 0:
                r -= 5
                pygame.draw.rect(screen, '#1b2838', (0, 0, 100, 200))
                pygame.draw.circle(screen, '#66c0f4', (57, 75), r)
                clock.tick(fps)
                pygame.display.flip()
                screen.blit(back, back_coords)
            for row in range(3):
                for col in range(3):
                    if zone[row][col] == 'x':
                        color = red
                    elif zone[row][col] == 'o':
                        color = green
                    else:
                        color = white
                    x = 90 + col * square + (col + 1) * margin
                    y = row * square + (row + 1) * margin
                    pygame.draw.rect(screen, color, (x, y, square, square))
                    if color == red:
                        pygame.draw.line(screen, white, (x + 1, y + 2), (x + square - 3, y + square - 3), 5)
                        pygame.draw.line(screen, white, (x + square - 3, y + 2), (x + 1, y + square - 3), 5)
                    elif color == green:
                        pygame.draw.circle(screen, white, (x + square // 2, y + square // 2), square // 2, 5)
            if krest_or_null % 2 != 0:
                end = win(zone, 'x')
            else:
                end = win(zone, 'o')

            if end:
                screen.fill(black)
                winner = font_of_score.render(end + ' победила(-и)!', True, (255, 255, 102))
                place = winner.get_rect(bottomright=(500, 275))
                screen.blit(winner, place)
                with open('info.txt', 'a') as f:
                    f.write(f'\nКрестики-нолики: {end} wins')

    if game_state == 'Snake':
        if not game_close:
            if x_snake >= 610 or x_snake < 110 or y_snake >= display_height or y_snake < 0:
                game_close = str(length_of_tors - 1)
            x_snake += x_change
            y_snake += y_change
            screen.fill('#1b2838')
            pygame.draw.rect(screen, (0, 0, 0), [90, 0, 540, 540])
            back = pygame.transform.scale(pygame.image.load('back.png'), (85, 85))
            back_coords = back.get_rect(midleft=(3, 75))
            screen.blit(back, back_coords)
            x, y = pygame.mouse.get_pos()
            if r == 40:
                pygame.draw.circle(screen, '#66c0f4', (45, 75), r)
                screen.blit(back, back_coords)
            if 5 < x < 90 and 25 < y < 110 and r != 40:
                r += 5
                pygame.draw.circle(screen, '#66c0f4', (45, 75), r)
                clock.tick(fps)
                pygame.display.flip()
                screen.blit(back, back_coords)
            elif (x < 5 or x > 90 or y < 25 or y > 110) and r != 0:
                r -= 5
                pygame.draw.rect(screen, '#1b2838', (0, 0, 90, 200))
                pygame.draw.circle(screen, '#66c0f4', (45, 75), r)
                clock.tick(fps)
                pygame.display.flip()
                screen.blit(back, back_coords)
            pygame.draw.rect(screen, green, [movement_x, movement_y, field, field])
            head_and_shoulders = []
            head_and_shoulders.append(x_snake)
            head_and_shoulders.append(y_snake)
            enumerate.append(head_and_shoulders)
            if len(enumerate) > length_of_tors:
                del enumerate[0]
            for elem in enumerate[:-1]:
                if elem == head_and_shoulders:
                    game_close = str(length_of_tors - 1)

            for i in enumerate:
                pygame.draw.rect(screen, (192, 192, 192), [i[0], i[1], field, field])
            score_of_game(length_of_tors - 1)
            pygame.display.update()

            if x_snake == movement_x and y_snake == movement_y:
                movement_x = round(random.randrange(90, 540 - field) / 10.0) * 10.0
                movement_y = round(random.randrange(0, display_height - field) / 10.0) * 10.0
                length_of_tors += 1

            time_of_game.tick(speed_run)
            if game_close:
                screen.fill(black)
                winner = font_of_score.render('Ваш счёт: ' + str(length_of_tors - 1), True, (255, 255, 102))
                place = winner.get_rect(bottomright=(450, 275))
                screen.blit(winner, place)
                with open('info.txt', 'a') as f:
                    f.write(f'\nЗмейка: {str(length_of_tors - 1)}')
    if game_state == 'fnap':
        fnap.main()

    pygame.display.update()
