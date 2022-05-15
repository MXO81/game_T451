import pygame
from constantes import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y): #pos_x , Pos_y
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('hombreF.png')
        
        self.rect = self.image.get_rect()
        #self.rect.left = left
        #self.rect.bottom = bottom
        
        self.rect.x = pos_x
        self.rect.y = pos_y
        
                
        self.speed = 3

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def left(self):
        self.rect.x -= self.speed #and self.rect.left < self.rect.x
        self.image = pygame.image.load("hombreIzq.png")

    def right(self):
        self.rect.x += self.speed
        self.image = pygame.image.load("hombreDer.png")
    
    def up(self):
        self.rect.y -= self.speed
        self.image = pygame.image.load('hombreF.png')


    def down(self):
        self.rect.y += self.speed
        self.image = pygame.image.load('hombreF.png')
    
    def fantasma(self):
        self.image = pygame.image.load('fantasma.png')

    def stop(self):
        self.speed = 0
    
      