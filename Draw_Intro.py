import sys
import time
import pygame
from random import randint, choice
from Draw_Blocks import draw_blocks
from Images_Of_Blocks import images
from Global import PALM, CURSOR, IMAGES_OF_BANGS, IMAGE_OF_INTRO_TANK, SURF


def draw_intro(
        list_of_objects: list,
        screen: pygame.Surface,
        score: int,
        score_of_red: int,
        score_of_blue: int,
        flag_of_full_win: bool
) -> tuple[int, int, int, list]:

    """
    Отображает заставочный экран
    :param list_of_objects: массив блоков и танков
    :param screen: экран
    :param score: флаг количества заходов на главный экран
    :param score_of_red: счётчик побед красного
    :param score_of_blue: счётчик побед синего
    :param flag_of_full_win: флаг победы в матче (5 побед с одной из сторон)
    :return: score, score_of_red, score_of_blue, list_of_objects:
    """

    if flag_of_full_win:
        pygame.mouse.set_visible(True)
        pygame.mouse.set_cursor(CURSOR)

        score_of_red = 0
        score_of_blue = 0

        pygame.display.set_caption(f'Favorite Tanks')

        image_of_enter = pygame.image.load('buttons/enter2.0.png')
        image_of_wasd = pygame.image.load('buttons/wasd2.0.png')
        image_of_arrows = pygame.image.load('buttons/arrows.png')

        list_of_intro_texts = [
            '        Поиграем!',
            '           В Бой !',
            '         Нагибать!',
            '         Поехали!',
            '       Побеждать!'
        ]

        font1 = pygame.font.Font(None, 200)
        font2 = pygame.font.Font(None, 90)
        font3 = pygame.font.Font(None, 60)

        text_q = font3.render('Q', True, (190, 190, 190))
        text_m = font3.render('M', True, (190, 190, 190))
        text_name = font1.render('Т а н к и', True, (210, 0, 0))
        text_welcome = font2.render('Добро пожаловать!', True, (190, 190, 190))
        text_start_game = font3.render('С Т А Р Т', True, (140, 140, 140))

        if score == 0:
            pygame.mixer.music.load('music/intro_music.mp3')
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.load(f'music/music{str(randint(2, 10))}.mp3')
            pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play()

            text_welcome = font2.render(choice(list_of_intro_texts), True, (190, 190, 190))

        screen.fill('black')

        wasd_flag = False
        arrows_flag = False

        count = 0

        start_flag = True
        while start_flag:
            count += 0.003
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.load('sounds/finish.mp3')
                    pygame.mixer.music.set_volume(0.9)
                    pygame.mixer.music.play()

                    time.sleep(2)

                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if wasd_flag and arrows_flag:
                            start_flag = False
                        else:
                            if not wasd_flag:
                                pygame.draw.rect(screen, 'red', (40, 320, 170, 8))
                                screen.blit(text_welcome, (100, 420))
                            if not arrows_flag:
                                pygame.draw.rect(screen, 'red', (590, 320, 170, 8))
                                screen.blit(text_welcome, (100, 420))

                            pygame.display.update()
                            pygame.time.wait(100)

                        sound = pygame.mixer.Sound('sounds/shot.wav')
                        sound.set_volume(0.7)
                        sound.play()

                        time.sleep(0.2)
                        break

                    elif event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.load('sounds/finish.mp3')
                        pygame.mixer.music.set_volume(0.9)
                        pygame.mixer.music.play()

                        time.sleep(2)

                        pygame.quit()
                        sys.exit()

                    elif event.key == pygame.K_w or \
                            event.key == pygame.K_q or \
                            event.key == pygame.K_a or \
                            event.key == pygame.K_s or \
                            event.key == pygame.K_d:

                        text_q = font3.render('Q', True, (100, 45, 45))

                        image_of_wasd = pygame.image.load('buttons/wasd2.0_red.png')
                        wasd_flag = True

                    elif event.key == pygame.K_DOWN or \
                            event.key == pygame.K_RIGHT or \
                            event.key == pygame.K_LEFT or \
                            event.key == pygame.K_UP or \
                            event.key == pygame.K_m:

                        image_of_arrows = pygame.image.load('buttons/arrows_red.png')
                        text_m = font3.render('M', True, (100, 45, 45))

                        arrows_flag = True

                screen.fill('black')
                screen.blit(pygame.transform.scale(IMAGE_OF_INTRO_TANK, (300, 300)), (250, 100))
                screen.blit(pygame.transform.scale(image_of_enter, (100, 100)), (690, 490))
                screen.blit(pygame.transform.scale(image_of_wasd, (150, 100)), (50, 200))
                screen.blit(pygame.transform.scale(image_of_arrows, (150, 100)), (600, 200))
                screen.blit(text_q, (55, 205))
                screen.blit(text_m, (605, 205))
                screen.blit(text_name, (122, 10))
                screen.blit(text_welcome, (100, 420))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 100 < mouse[0] < 685 and 530 < mouse[1] < 590:
                pygame.draw.rect(screen, (190, 0, 0), (100, 520, 580, 60))
                screen.blit(text_start_game, (300, 530))
                screen.blit(text_welcome, (100, 420))

                pygame.mouse.set_cursor(PALM)

                if any(click):
                    if wasd_flag and arrows_flag:
                        start_flag = False
                    else:
                        if not wasd_flag:
                            pygame.draw.rect(screen, 'red', (40, 320, 170, 8))
                            screen.blit(text_welcome, (100, 420))
                        if not arrows_flag:
                            pygame.draw.rect(screen, 'red', (590, 320, 170, 8))
                            screen.blit(text_welcome, (100, 420))

                        pygame.display.update()

                    sound = pygame.mixer.Sound('sounds/shot.wav')
                    sound.set_volume(0.7)
                    sound.play()

                    time.sleep(0.2)

            elif 690 < mouse[0] < 795 and 495 < mouse[1] < 595:
                pygame.draw.rect(screen, (190, 0, 0), (690, 490, 100, 100))
                screen.blit(pygame.transform.scale(image_of_enter, (100, 100)), (690, 490))
                screen.blit(text_start_game, (300, 530))
                screen.blit(text_welcome, (100, 420))

                pygame.mouse.set_cursor(PALM)

                if any(click):
                    if wasd_flag and arrows_flag:
                        start_flag = False
                    else:
                        if not wasd_flag:
                            pygame.draw.rect(screen, 'red', (40, 320, 170, 8))
                            screen.blit(text_welcome, (100, 420))
                        if not arrows_flag:
                            pygame.draw.rect(screen, 'red', (590, 320, 170, 8))
                            screen.blit(text_welcome, (100, 420))

                        pygame.display.update()

                    sound = pygame.mixer.Sound('sounds/shot.wav')
                    sound.set_volume(0.7)
                    sound.play()

                    time.sleep(0.2)

            elif 50 < mouse[0] < 200 < mouse[1] < 300:
                pygame.mouse.set_cursor(PALM)

                screen.blit(text_start_game, (300, 530))
                screen.blit(text_welcome, (100, 420))

                if any(click):
                    wasd_flag = True

                    text_q = font3.render('Q', True, (100, 45, 45))
                    image_of_wasd = pygame.image.load('buttons/wasd2.0_red.png')

                    screen.blit(pygame.transform.scale(image_of_wasd, (150, 100)), (50, 200))
                    screen.blit(text_q, (55, 205))

                    sound = pygame.mixer.Sound('sounds/shot.wav')
                    sound.set_volume(0.7)
                    sound.play()

                    time.sleep(0.2)

            elif 600 < mouse[0] < 750 and 200 < mouse[1] < 300:
                pygame.mouse.set_cursor(PALM)

                screen.blit(text_start_game, (300, 530))
                screen.blit(text_welcome, (100, 420))

                if any(click):
                    arrows_flag = True

                    image_of_arrows = pygame.image.load('buttons/arrows_red.png')
                    text_m = font3.render('M', True, (100, 45, 45))
                    screen.blit(pygame.transform.scale(image_of_arrows, (150, 100)), (600, 200))
                    screen.blit(text_m, (605, 205))

                    sound = pygame.mixer.Sound('sounds/shot.wav')
                    sound.set_volume(0.7)
                    sound.play()

                    time.sleep(0.2)

            elif 280 < mouse[0] < 530 and 130 < mouse[1] < 390:
                pygame.mouse.set_cursor(PALM)
                screen.blit(text_welcome, (100, 420))

                screen.blit(text_start_game, (300, 530))

                if any(click):
                    pygame.mixer.music.load('music/music1.mp3')
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play()

            elif 70 < mouse[1] < 102 and (70 < mouse[0] < 107 or 700 < mouse[0] < 737):
                pygame.mouse.set_cursor(PALM)

                screen.blit(text_start_game, (300, 530))
                screen.blit(text_welcome, (100, 420))

                if any(click):
                    sound = pygame.mixer.Sound('sounds/shot.wav')
                    sound.set_volume(0.7)
                    sound.play()

                    images(screen, score)
            else:
                pygame.draw.rect(screen, 'black', (100, 520, 200, 60))
                screen.blit(text_start_game, (300, 530))
                screen.blit(text_welcome, (100, 420))

                pygame.mouse.set_cursor(CURSOR)

            screen.blit(SURF, (70, 60))
            screen.blit(IMAGES_OF_BANGS[int(count % 3)], (70, 60))

            screen.blit(SURF, (700, 60))
            screen.blit(IMAGES_OF_BANGS[int(count % 3)], (700, 60))

            if not pygame.mixer.music.get_busy():
                if score == 0:
                    pygame.mixer.music.load('sounds/background_music.mp3')
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.load(f'music/music{str(randint(2, 10))}.mp3')
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play()
            pygame.display.update()

    score = 1

    screen.fill('black')
    pygame.display.set_caption(f'Favorite Tanks       {score_of_blue} : {score_of_red}')
    draw_blocks(list_of_objects)

    return score, score_of_red, score_of_blue, list_of_objects
