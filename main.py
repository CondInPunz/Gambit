import pygame
import sys


def win(mas, znak):
    for_future = 0
    for row in mas:
        for_future += row.count('')
        if row.count(znak) == 3:
            return znak
    for col in range(3):
        if mas[0][col] == znak and mas[1][col] == znak and mas[2][col] == znak:
            return znak
    if mas[0][1] == znak and mas[1][1] == znak and mas[2][2] == znak:
        return znak
    if mas[0][2] == znak and mas[1][1] == znak and mas[2][0] == znak:
        return znak
    if for_future == 0:
        return 'Frendship'
    return None


if __name__ == "__main__":
    pygame.init()
    game_state = 'MainMenu'
    square = 100
    margin = 15
    width = height = square * 3 + margin * 4
    size = (width, height)
    screen = pygame.display.set_mode(size)
    screen.fill('#1b2838')
    pygame.display.set_caption('Крестики-нолики')
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    zone = [[''] * 3 for i in range(3)]
    krest_or_null = 0
    end = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not end:
                if game_state == 'MainMenu':
                    x, y = pygame.mouse.get_pos()
                    if x <= width // 3:
                        game_state = 'KrestNull'
                elif game_state == 'KrestNull':
                    x, y = pygame.mouse.get_pos()
                    col = x // (square + margin)
                    row = y // (square + margin)
                    if zone[row][col] == '':
                        if krest_or_null % 2 == 0:
                            zone[row][col] = 'x'
                        else:
                            zone[row][col] = 'o'
                        krest_or_null += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if game_state == 'KrestNull':
                    end = False
                    zone = [[''] * 3 for i in range(3)]
                    krest_or_null = 0

        if game_state == 'KrestNull':
            if not end:
                for row in range(3):
                    for col in range(3):
                        if zone[row][col] == 'x':
                            color = red
                        elif zone[row][col] == 'o':
                            color = green
                        else:
                            color = white
                        x = col * square + (col + 1) * margin
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
                    print(end)

        pygame.display.update()
    pygame.quit()
