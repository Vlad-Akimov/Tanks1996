import pygame
from random import randint
from Tank import Tank
from Global import IMAGE_OF_BLUE_TANK, IMAGE_OF_RED_TANK, WIDTH, HEIGHT, TILE
from Blocks import BlockBrick, BlockWater, BlockArmor, BlockBushes


def draw_blocks(
	list_of_objects: list
) -> None:

	"""
	Создаёт синий танк, красный танк, 20 блоков воды, 20 блоков брони, 50 блоков кирпича, 30 блоков кустов
	:param list_of_objects: массив блоков и танков
	:return: None
	"""

	Tank('blue', 100, 50, 2, (
		pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_q), IMAGE_OF_BLUE_TANK, list_of_objects)

	Tank('red', 650, 500, 0, (
		pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_m), IMAGE_OF_RED_TANK, list_of_objects)

	for _ in range(20):
		while True:
			while True:
				x = randint(0, WIDTH // TILE) * TILE
				if x != 96 and x != 640:
					break

			while True:
				y = randint(0, HEIGHT // TILE) * TILE
				if y != 64 and y != 512:
					break
			rect = pygame.Rect(x, y, TILE, TILE)

			fined = False
			for _object in list_of_objects:
				if rect.colliderect(_object.rect):
					fined = True
			if not fined:
				break
		BlockWater(x, y, list_of_objects, TILE)

	for _ in range(20):
		while True:
			while True:
				x = randint(0, WIDTH // TILE) * TILE
				if x != 96 and x != 640:
					break

			while True:
				y = randint(0, HEIGHT // TILE) * TILE
				if y != 64 and y != 512:
					break
			rect = pygame.Rect(x, y, TILE, TILE)

			fined = False
			for _object in list_of_objects:
				if rect.colliderect(_object.rect):
					fined = True
			if not fined:
				break
		BlockArmor(x, y, list_of_objects, TILE)

	for _ in range(50):
		while True:
			x = randint(0, WIDTH // TILE) * TILE
			y = randint(0, HEIGHT // TILE) * TILE
			rect = pygame.Rect(x, y, TILE, TILE)

			fined = False
			for _object in list_of_objects:
				if rect.colliderect(_object.rect):
					fined = True
			if not fined:
				break
		BlockBrick(x, y, list_of_objects, TILE)

	for _ in range(30):
		while True:
			x = randint(0, WIDTH // TILE) * TILE
			y = randint(0, HEIGHT // TILE) * TILE
			rect = pygame.Rect(x, y, TILE, TILE)

			fined = False
			for _object in list_of_objects:
				if rect.colliderect(_object.rect):
					fined = True
			if not fined:
				break
		BlockBushes(x, y, list_of_objects, TILE)
