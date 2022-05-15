### Importaciones ###
import pygame, sys,time

from constantes import *
from player import Player
from autoIzq import Auto_izq
from auto2Izq import Auto2_izq
from autoDer import Auto_der
from auto2Der import Auto_2der
from refugio import Refugio
from inicio import Inicio
from random import randint

### Inicializar ###
pygame.init()

### Creando pantalla ###
surface = pygame.display.set_mode(DIMENSION)
pygame.display.set_caption(TITLE)
### Fuentes ###
fuente1 = pygame.font.SysFont("Lucida Console", 15)
fuente2 = pygame.font.SysFont("verdana", 16)
fuente3 = pygame.font.SysFont("verdana", 26)
### Crear objetos ###
clock = pygame.time.Clock()
jugador = Player(WIDTH // 2, HEIGHT-100)
refugio = Refugio(0, 20)
inicio = Inicio (0, 700)
player = pygame.sprite.Group()
autos_izq = pygame.sprite.Group()
autos2_izq = pygame.sprite.Group()
autos_der = pygame.sprite.Group()
autos2_der = pygame.sprite.Group()
refugios = pygame.sprite.Group()
### Archivos y control de sonidos ###
pygame.mixer.music.load('sounds_music.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
sound = pygame.mixer.Sound('clank-car-crash-collision.wav')
sound2 = pygame.mixer.Sound('yeah.wav')
### Variables ###
message = ''
vidas = 3
nivel = 1
score = 0
CHOCAR = pygame.USEREVENT + 1

### Función para actualizar posición tras atropellamiento ###
def actualizar_pos_jugador():
    return (WIDTH // 2, HEIGHT-100)
posicion_jugador = actualizar_pos_jugador() 

### Bucle principal ### 
a_game = True
while a_game:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a_game = False

            if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RETURN:
                        a_game = True
                    
        surface.fill(NEGRO)

        historia = [
            "                      TESLA 451",
            "   Tras asumir la presidencia mundial, el tirano Elon Musk    ",
            "   impone el sistema autonomo de conducción a todo vehículo   ",
            "   en el planeta.                                             ",
            "   El software de los autos ante todo prepondera el traslado  ",
            "   de los ocupantes sin importar si algo cruza en su camino.  ",
            "   ",
            "       Corre, muevete, cruza el camino y ponte a salvo.        "
            
            "",
            "                Pulsa 'ENTER' para empezar"
            ]

        y = 60
        for frase in historia:
            texto = fuente1.render(frase, True, MAGENTA)
            surface.blit(texto, (10, y))
            y += 60

        pygame.display.update()

a_game = True
while a_game:

    clock.tick(60)

### Evaluar teclas ###
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_RIGHT]:
        jugador.right()

    if key_pressed[pygame.K_LEFT]:
        jugador.left()

    if key_pressed[pygame.K_UP]:
        jugador.up()

    if key_pressed[pygame.K_DOWN]:
        jugador.down()

    surface.fill((BACKGROUND_COLOR))

### Condicionando posición y repeticion de autos ###
    if len(autos_izq) == 0:
        for number in range (0, 1):
            pos_x = 600
            pos_y = 200
            auto_izq = Auto_izq(pos_x, pos_y)
            autos_izq.add(auto_izq)

    if len(autos2_izq) == 0:
        for number in range (0, 1):
            pos_x = 600 #randint (1200, 1200)
            pos_y = 400 #randint (10, 10)            
            auto2_izq = Auto2_izq(pos_x, pos_y)
            autos2_izq.add(auto2_izq)

    if len(autos_der) == 0:
        for number in range (0, 1):
            pos_x = 0 #randint (0, 1)
            pos_y = 300 #randint (200, 200)            
            auto_der = Auto_der(pos_x, pos_y)
            autos_der.add(auto_der)

    if len(autos2_der) == 0:
        for number in range (0, 1):
            pos_x = randint (0, 0)
            pos_y = randint (500, 500)            
            auto2_der = Auto_2der(pos_x, pos_y)
            autos2_der.add(auto2_der)

### Insertar autos ###
    for auto_izq in autos_izq:
        auto_izq.left()
        auto_izq.draw(surface)
    
    for auto2_izq in autos2_izq:
        auto2_izq.left()
        auto2_izq.draw(surface)

    for auto_der in autos_der:
        auto_der.rigth()
        auto_der.draw(surface)

    for auto2_der in autos2_der:
        auto2_der.rigth()
        auto2_der.draw(surface)

### Eliminar autos que desaparecen de la pantalla ###
    if auto_izq.rect.x < WIDTH-700:
        autos_izq.remove(auto_izq) 

    if auto2_izq.rect.x < WIDTH-700:
        autos2_izq.remove(auto2_izq)

    if auto_der.rect.x > WIDTH:
        autos_der.remove(auto_der)
    
    if auto2_der.rect.x > WIDTH:
        autos2_der.remove(auto2_der)

### Niveles (No pude generar la lógica)###
    #if jugador in refugio:
     #   nivel += 1

### Detección de colisiones, sonido y perdida de vidas por colision ###
    
    if pygame.sprite.collide_rect_ratio(.5)(jugador, auto_izq):
        message = 'intentalo de nuevo'
        vidas -= 1
        sound.play()        
        time.sleep(.05)
        auto_izq.stop()
        text = fuente2.render(message, True, MAGENTA)
        rect = text.get_rect()
        rect.topright = (WIDTH-400, 50)
        surface.blit(text, rect)
        print(vidas)    #solo para saber comportamiento
    if pygame.sprite.collide_rect_ratio(.5)(jugador, auto2_izq):
        message = 'intentalo de nuevo'
        vidas -= 1
        sound.play()
        time.sleep(0.05)
        auto2_izq.stop()
        text = fuente2.render(message, True, MAGENTA)
        rect = text.get_rect()
        rect.topright = (WIDTH-400, 50)
        surface.blit(text, rect)
        print(vidas) #solo para saber comportamiento
    if pygame.sprite.collide_rect_ratio(.5)(jugador, auto_der):
        message = 'intentalo de nuevo'
        vidas -= 1
        sound.play()
        time.sleep(0.05)
        auto_der.stop()
        text = fuente2.render(message, True, MAGENTA)
        rect = text.get_rect()
        rect.topright = (WIDTH-400, 50)
        surface.blit(text, rect)
        print(vidas)    #solo para saber comportamiento
    if pygame.sprite.collide_rect_ratio(.5)(jugador, auto2_der):
        message = 'intentalo de nuevo'
        vidas -= 1
        sound.play()
        time.sleep(0.05)
        actualizar_pos_jugador()
        auto2_der.stop()
        text = fuente2.render(message, True, MAGENTA)
        rect = text.get_rect()
        rect.topright = (WIDTH-400, 50)
        surface.blit(text, rect)
        print(vidas) #solo para saber comportamiento
### Detección de punto de salvamento (por colisión) ###
    if pygame.sprite.collide_rect_ratio(.5)(jugador, refugio):
        message = 'Estás a salvo!!!'
        sound2.play()
        text = fuente2.render(message, True, AZUL)
        rect = text.get_rect()
        rect.topright = (WIDTH-400 , 50)
        surface.blit(text, rect)
        time.sleep(2)
        nivel = False
        nivel =+1
        print(nivel) #solo para saber comportamiento
        auto_izq.stop()
        auto2_izq.stop()
        auto_der.stop()
        auto2_der.stop()
### Para actualizar posición de jugador tras atropellamiento (No me dio resultado)###       
    for event in pygame.event.get():
        if event.type == CHOCAR:
            vidas -=1
            actualizar_pos_jugador()

### Condición del Game Over ###                            
    if vidas <= 0:
        message = "GAME OVER"
        text = fuente3.render(message, True, NEGRO)
        rect = text.get_rect()
        rect.topright = (WIDTH-400 , 650)
        surface.blit(text, rect)
        time.sleep(.5)
        jugador.fantasma()        
        auto_izq.stop()
        auto2_izq.stop()
        auto_der.stop()
        auto2_der.stop()
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
# dibujando objetos en surface 
    refugio.draw(surface)
    jugador.draw(surface)
    inicio.draw(surface)
    
        
    pygame.display.update()


