import pygame

class Auto_izq(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('4x4Izq.png')
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
                
        self.speed = 1
    
    def left(self):
        self.rect.x -= self.speed
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def stop(self):
        self.speed = 0

