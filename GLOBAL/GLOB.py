import pygame

pygame.init()

"""
==========
WIDTH - ширина, 
HEIGHT - высота
----------
FPS - частота кадров в секунду, используется в PLAYING			
----------
TILE - размер стороны блоков используется в: draw_blocks(), классе Tank
----------
CLOCK - экземпляр pygame, используется в PLAYING 
----------
Favorite Tanks - установленное название окна игры, изменяется в DRAW_INTRO
----------
block_brick.png - установленная иконка окна игры
----------
WINDOW - экран с размерами ширины и высоты, используется в: классах Bullet и UI, MAIN
----------
CURSOR - курсор, взятый из IMAGE_OF_CURSOR
PALM - тоже самое, что и CURSOR, но с другой картинкой (IMAGE_OF_PALM)

CURSOR и PALM - чередуются в зависимости от расположения курсора, используется в: draw_intro(), images(), rules()
----------
IMAGES_OF_BLOCKS - список с загруженными картинками блоков, используется в: images(), BLOCKS
----------
IMAGE_OF_BLUE_TANK - загруженная картинка синего танка, используется в: images(), draw_blocks()
----------
IMAGE_OF_RED_TANK - загруженная картинка красного танка, используется в: images(), draw_blocks()
----------
IMAGE_OF_INTRO_TANK - загруженная картинка танка для главного экрана, используется в: images(), draw_intro()
----------
IMAGES_OF_BANGS - список картинок взрывов, используется в: images(), draw_intro()
---------
SURF - объект класса pygame.Surface с размерами, равными стороне блоков (TILE), изменяется в DRAW_INTRO
----------
BULLETS - список снарядом, изменяется при "выстреле"
----------
OBJECTS - список экземпляров классов, используется везде каким-либо образом
----------
SCORE - количество загрузок в игру, изменяется в DRAW_INTRO,
            может равняться 0, если был заход в игру первый раз или 
                            1, если был заход в бой хотя бы один раз
----------
WIN_FLAG - флаг проверки в игровом цикле, произошла ли победа, изменяется в TANK, используется в PLAYING и UI
----------
SCORE_BLUE - счёт количества очков у "синего" игрока, изменяется в момент победы
----------
SCORE_RED - счёт количества очков у "красного" игрока, изменяется в момент победы
----------
DIRECTS - список списков, откуда берутся значения в TANK, для определения направления векторов полёта снарядов
==========
"""

WIDTH = 800
HEIGHT = 608
FPS = 60
TILE = 32

CLOCK = pygame.time.Clock()

pygame.display.set_caption('Favorite Tanks')
pygame.display.set_icon(pygame.image.load("../images/block_brick.png"))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

IMAGE_OF_CURSOR = pygame.image.load('../images/arrow.png')
CURSOR = pygame.cursors.Cursor((16, 16), IMAGE_OF_CURSOR)
IMAGE_OF_PALM = pygame.image.load('../images/palm.png')
PALM = pygame.cursors.Cursor((16, 16), IMAGE_OF_PALM)

IMAGES_OF_BLOCKS = [
    pygame.image.load('../images/block_armor2.0.png'),
    pygame.image.load('../images/block_brick2.0.png'),
    pygame.image.load('../images/block_bushes2.0.png'),
    pygame.image.load('../images/block_water.png')
]
IMAGE_OF_BLUE_TANK = pygame.image.load('../images/tank1.png')
IMAGE_OF_RED_TANK = pygame.image.load('../images/tank2.png')
IMAGE_OF_INTRO_TANK = pygame.image.load('../images/intro_tank2.0.png')
IMAGES_OF_BANGS = [
    pygame.image.load('../images/bang1.png'),
    pygame.image.load('../images/bang2.png'),
    pygame.image.load('../images/bang3.png')
]

SURF = pygame.Surface((TILE, TILE))

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

BULLETS = list()
OBJECTS = list()

SCORE = 0

WIN_FLAG = False

SCORE_BLUE = 0
SCORE_RED = 0
