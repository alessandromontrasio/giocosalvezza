import pygame, sys
from pygame.locals import *
pygame.init()

marza = pygame.image.load('marzaemote.png')
gameover = pygame.image.load('gameover.png')
sfondo = pygame.image.load('sfondo.png')

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pacman")

clock = pygame.time.Clock()
marzaspeed = 10
width = 800
height = 600


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def inizializza():
    global marzax, marzay
    marzax, marzay = 0, 0

def draw_pacman(x, y):
    screen.blit(marza, (40, 40))


inizializza()

cell_size = 40
cols = 20
rows = 15

# Definizione della griglia del labirinto
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# Funzione per disegnare il labirinto
def draw_maze():
    for y in range(rows):
        for x in range(cols):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLUE, (x * cell_size, y * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, WHITE, (x * cell_size, y * cell_size, cell_size, cell_size))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()

    prev_marzax = marzax
    prev_marzay = marzay
    # Movimento del Pacman
    
    if keys[pygame.K_LEFT]:
        marzax -= marzaspeed
    if keys[pygame.K_RIGHT]:
        marzax += marzaspeed
    if keys[pygame.K_UP]:
        marzay -= marzaspeed
    if keys[pygame.K_DOWN]:
        marzay += marzaspeed
    if marzax == 0 and marzay == 0:
        marzax += prev_marzax
    # Disegno del labirinto
    draw_maze()
    # Disegno del Pacman
    draw_pacman(marzax, marzay)
    
    # screen.fill(BLACK)

    # Aggiornamento della finestra di gioco
    pygame.display.flip()
    

    pygame.display.update()
    clock.tick(30)