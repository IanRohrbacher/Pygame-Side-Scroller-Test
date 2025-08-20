import pygame
import sys

pygame.init()

up_down = False
UPkey = False
LEFTkey = False
RIGHTkey = False

ground_brown = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ground_green = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ground_black = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = 0.0
y = 0
move_over = 0

SCREEN = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Side Scroller")


SCREEN.fill((35, 147, 252))
pygame.display.flip()

for p in range(10):
    ground_brown[p] = pygame.Rect(0 + move_over, 420, 80, 80)
    ground_green[p] = (0 + move_over, 430), (80 + move_over, 430)
    ground_black[p] = (0 + move_over, 420), (80 + move_over, 420), (80 + move_over, 500), (0 + move_over, 500)
    move_over += 80

for u in range(10):
    pygame.draw.rect(SCREEN, (196, 119, 31), ground_brown[u])
    pygame.draw.lines(SCREEN, (93, 240, 29), False, (ground_green[u]), width=20)
    pygame.draw.lines(SCREEN, (0, 0, 0), False, (ground_black[u]), width=2)

pygame.draw.lines(SCREEN, (255, 205, 117), False, ((40, 419), (40, 379)), width=5)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_UP:
                print("up press")
                UPkey = True
            if event.key == pygame.K_LEFT:
                print("left press")
                LEFTkey = True
            if event.key == pygame.K_RIGHT:
                print("right press")
                RIGHTkey = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("up unpress")
                UPkey = False
            if event.key == pygame.K_LEFT:
                print("left unpress")
                LEFTkey = False
            if event.key == pygame.K_RIGHT:
                print("right unpress")
                RIGHTkey = False

    if RIGHTkey and LEFTkey:
        print("x = " + str(x))
        pygame.time.wait(50)

    elif RIGHTkey:
        if x != 740:
            x += 2

        pygame.draw.lines(SCREEN, (255, 205, 117), False, ((40 + x, 419), (40 + x, 379)), width=5)
        pygame.draw.lines(SCREEN, (35, 147, 252), False, ((35 + x, 419), (35 + x, 379)), width=5)

        print("x = " + str(x))
        pygame.time.wait(50)

    elif LEFTkey:
        if x != 0:
            x -= 2

        pygame.draw.lines(SCREEN, (255, 205, 117), False, ((40 + x, 419), (40 + x, 379)), width=5)
        pygame.draw.lines(SCREEN, (35, 147, 252), False, ((45 + x, 419), (45 + x, 379)), width=5)

        print("x = " + str(x))
        pygame.time.wait(50)

    if UPkey:
        for o in range(2):
            for i in range(10):
                if o == 0:
                    y += 5
                    pygame.draw.lines(SCREEN, (255, 205, 117), False, ((40 + x, 419 - y), (40 + x, 379 - y)), width=5)
                    pygame.draw.lines(SCREEN, (35, 147, 252), False, ((40 + x, 419 - y), (40 + x, 424 - y)), width=5)
                elif o == 1:
                    y -= 5
                    pygame.draw.lines(SCREEN, (255, 205, 117), False, ((40 + x, 419 - y), (40 + x, 379 - y)), width=5)
                    pygame.draw.lines(SCREEN, (35, 147, 252), False, ((40 + x, 379 - y), (40 + x, 344 - y)), width=5)

                pygame.display.flip()

                print("y = " + str(y))
                if LEFTkey:
                    if x != 0:
                        x -= 2

                    pygame.draw.lines(SCREEN, (255, 205, 117), False, ((40 + x, 419 - y), (40 + x, 379 - y)), width=5)
                    pygame.draw.lines(SCREEN, (35, 147, 252), False, ((45 + x, 419), (45 + x, 379)), width=5)
                    pygame.draw.lines(SCREEN, (35, 147, 252), False, ((45 + x, 419 - y), (45 + x, 379 - y)), width=5)

                    print("x = " + str(x))

                elif RIGHTkey:
                    if x != 740:
                        x += 2

                    pygame.draw.lines(SCREEN, (255, 205, 117), False, ((40 + x, 419 - y), (40 + x, 379 - y)), width=5)
                    pygame.draw.lines(SCREEN, (35, 147, 252), False, ((35 + x, 419), (35 + x, 379)), width=5)
                    pygame.draw.lines(SCREEN, (35, 147, 252), False, ((35 + x, 419 - y), (35 + x, 379 - y)), width=5)

                    print("x = " + str(x))
                pygame.time.wait(50)

    pygame.display.flip()