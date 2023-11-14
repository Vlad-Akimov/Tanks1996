import pygame

pygame.init()

WIDTH = 800
"""Ширина окна"""
HEIGHT = 608
"""Высота окна"""
FPS = 60
"""Частота кадров в секунду"""
TILE = 32
"""Размер стороны блоков"""

CLOCK = pygame.time.Clock()

pygame.display.set_caption('Favorite Tanks')
"""Установленное название окна игры"""
pygame.display.set_icon(pygame.image.load("images/block_brick.png"))
"""Установленная иконка окна игры"""

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
"""Экран с размерами ширины и высоты"""

IMAGE_OF_CURSOR = pygame.image.load('images/arrow.png')
CURSOR = pygame.cursors.Cursor((16, 16), IMAGE_OF_CURSOR)
"""Стандартный курсор мыши"""
IMAGE_OF_PALM = pygame.image.load('images/palm.png')
PALM = pygame.cursors.Cursor((16, 16), IMAGE_OF_PALM)
"""Курсор мыши при наведения на объекты, на которые можно кликнуть"""

IMAGES_OF_BLOCKS = [
    pygame.image.load('images/block_armor2.0.png'),
    pygame.image.load('images/block_brick2.0.png'),
    pygame.image.load('images/block_bushes2.0.png'),
    pygame.image.load('images/block_water.png')
]
"""Список с загруженными картинками блоков"""
IMAGE_OF_BLUE_TANK = pygame.image.load('images/tank1.png')
"""Картинка синего танка"""
IMAGE_OF_RED_TANK = pygame.image.load('images/tank2.png')
"""Картинка красного танка"""
IMAGE_OF_INTRO_TANK = pygame.image.load('images/intro_tank2.0.png')
"""Картинка танка для главного экрана"""
IMAGES_OF_BANGS = [
    pygame.image.load('images/bang1.png'),
    pygame.image.load('images/bang2.png'),
    pygame.image.load('images/bang3.png')
]
"""Список картинок взрывов"""

SURF = pygame.Surface((TILE, TILE))

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
"""Список списков, со значениями для определения направления полёта снарядов"""

BULLETS = list()
"""Список снарядом"""
OBJECTS = list()
"""Список блоков и танков"""

SCORE = 0
"""Количество заходов в игру"""

WIN_FLAG = False
"""Флаг проверки произошла ли победа в целом"""

SCORE_BLUE = 0
"""количество очков у синего танка"""
SCORE_RED = 0
"""количество очков у красного танка"""
