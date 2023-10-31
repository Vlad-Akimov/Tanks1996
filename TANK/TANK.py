from __future__ import annotations
import pygame
from BULLET.BULLET import Bullet
from GLOBAL.GLOB import TILE, WIDTH, HEIGHT, DIRECTS


"""
==========
класс Tank: работа с танками
----------
init(): вызывается в draw_blocks, создаёт переменные-характеристики танков
----------
update(): вызывается в PLAYING, 
			возможно: изменение координат танка; "создание" снаряда; проигрывание звуков; поворот картинки танка.
----------
draw(): вызывается в PLAYING, отображает танк
----------
damage(): вызывается в Bullet, воспроизводит звуки,
			удаляет "танки" из списка объектов,
			возвращает булевую переменную, означающей победу
==========
"""


class Tank:
	def __init__(
		self: Tank,
		color: str,
		parent_x: int,
		parent_y: int,
		direct: int,
		list_of_keys: tuple,
		image: pygame.Surface,
		list_of_objects: list,
	) -> None:

		list_of_objects.append(self)
		self.type = 'tank'
		self.img = image
		self.color = color
		self.rect = pygame.Rect(parent_x, parent_y, TILE, TILE)

		self.direct = direct
		self.moveSpeed = 2

		self.shotTimer = 0
		self.shotDelay = 60

		self.bulletSpeed = 5

		self.keyLEFT = list_of_keys[0]
		self.keyRIGHT = list_of_keys[1]
		self.keyUP = list_of_keys[2]
		self.keyDOWN = list_of_keys[3]
		self.keySHOT = list_of_keys[4]

		self.name_of_bushes = ''

		self.image = pygame.transform.rotate(self.img, -self.direct * 90)

		self.rect = self.image.get_rect(center=self.rect.center)

	def update(
		self: Tank,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		self.image = pygame.transform.rotate(self.img, -self.direct * 90)
		self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))

		self.rect = self.image.get_rect(center=self.rect.center)

		old_x, old_y = self.rect.topleft

		if list_of_keys[self.keyLEFT]:
			if 0 < old_x:
				self.rect.x -= self.moveSpeed
				self.direct = 3

		elif list_of_keys[self.keyRIGHT]:
			if old_x < WIDTH - 30:
				self.rect.x += self.moveSpeed
				self.direct = 1

		elif list_of_keys[self.keyUP]:

			if 0 < old_y:
				self.rect.y -= self.moveSpeed
				self.direct = 0

		elif list_of_keys[self.keyDOWN]:
			if old_y < HEIGHT - 30:
				self.rect.y += self.moveSpeed
				self.direct = 2

		for _object in list_of_objects:
			if _object != self and \
					_object.type in ['water', 'block', 'tank', 'armor'] and \
					self.rect.colliderect(_object.rect):

				self.rect.topleft = old_x, old_y

			if _object != self and \
				_object.type == 'bushes' and \
				self.rect.colliderect(_object.rect) and \
				(list_of_keys[self.keyLEFT] or
				 list_of_keys[self.keyRIGHT] or
				 list_of_keys[self.keyUP] or
				 list_of_keys[self.keyDOWN]):

				if self.name_of_bushes != _object:

					sound = pygame.mixer.Sound('../sounds/bushes.mp3')
					sound.set_volume(0.1)
					sound.play()

					self.name_of_bushes = _object

		if list_of_keys[self.keySHOT] and self.shotTimer == 0:
			vector_x = DIRECTS[self.direct][0] * self.bulletSpeed
			vector_y = DIRECTS[self.direct][1] * self.bulletSpeed

			Bullet(self, self.rect.centerx, self.rect.centery, vector_x, vector_y, self.color, list_of_bullets)

			self.shotTimer = self.shotDelay

		if self.shotTimer > 0:
			self.shotTimer -= 1

	def draw(
		self: Tank,
		screen: pygame.Surface
	) -> None:

		screen.blit(self.image, self.rect)

	def damage(
		self: Tank,
		list_of_objects: list
	) -> bool:

		sound = pygame.mixer.Sound('../sounds/dead2.0.mp3')
		sound.set_volume(0.7)
		sound.play()

		sound1 = pygame.mixer.Sound('../sounds/dead3.0.mp3')
		sound1.set_volume(0.7)
		sound1.play()

		list_of_objects.remove(self)

		flag_of_win = True
		return flag_of_win
