import os
import sys

import pygame
import random

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 500)
        self.rect.y = random.randint(0, 500)
        self.rect.move(self.rect.x,
                       self.rect.y)

    def update(self):
        self.rect = self.rect.move(self.rect.x,
                                   self.rect.y)


all_sprites = pygame.sprite.Group()

# создадим спрайт
for i in range(20):
    sprite = pygame.sprite.Sprite()
    # определим его вид
    sprite.image = load_image("bomb.png")
    # и размеры
    sprite.rect = sprite.image.get_rect()
    print(sprite.rect.x)
    # добавим спрайт в группу
    all_sprites.add(sprite)

running = True

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
