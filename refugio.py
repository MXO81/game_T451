import pygame

class Refugio(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('fondo_salvo.png')
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

        #self.speed = 0
    
    #def center(self):
        #self.rect.x = 0#+= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    
