import pygame
import math
from pygame.locals import *
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, contenedor):
        self.puntos = 0
        self.angulo = 0
        self.vida = 100
        self.velocidad = [0, 0]
        self.contenedor = contenedor
        self.imagen_base = pygame.image.load("imagenes/naveuwu.png")
        self.imagen = self.imagen_base
        self.rect = self.imagen.get_rect()
        self.rect.move_ip(contenedor[0]/2, contenedor[1]/2)

    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_LEFT]:
            self.rotar(2)
        elif teclas[K_RIGHT]:
            self.rotar(-2)
        elif teclas[K_UP]:
            self.acelerar()
        elif teclas[K_DOWN]:
            pass

        self.velocidad[0] *= 0.99
        self.velocidad[1] *= 0.99


        self.rect = self.rect.move(self.velocidad)
        self.rect.x %= self.contenedor [0]
        self.rect.y %= self.contenedor [1]

    def acelerar(self):
        self.velocidad[1] += math.cos(math.radians((self.angulo)%360))
        self.velocidad[0] -=math.sin(math.radians((self.angulo)%360))

    def rotar(self, angulo):
        self.angulo += angulo
        centro_x = self.rect.centerx
        centro_y = self.rect.centery
        self.imagen = pygame.transform.rotate(self.imagen_base, self.angulo)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = centro_x
        self.rect.centery = centro_y
        