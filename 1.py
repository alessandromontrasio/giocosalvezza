import pygame, sys
from pygame.locals import *
import random
ALTEZZA = 800
LARGHEZZA= 1500
FINESTRA = (LARGHEZZA, ALTEZZA)
CELLA = (50, 50)
NERO = (0,0,0)
velocita = 2
# flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.OPENGL
screen = pygame.display.set_mode(FINESTRA) #flags
pygame.display.set_caption('Zambrotta prime')

clock = pygame.time.Clock()
fps = 60

labirinto = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

pacman_image = pygame.image.load('marzaemote.png')
pacman_image = pygame.transform.scale(pacman_image, (40, 40))
pacman_rect = pacman_image.get_rect()
pacman_rect.x = 50
pacman_rect.y = 50

ghost_image = pygame.image.load('ghost.png')
ghost_image = pygame.transform.scale(pacman_image, (40, 40))
ghost_rect = pacman_image.get_rect()


labirinto_rect = []
punti_rect = []


mossa = ''


pygame.display.flip()

def collisione(pacman_rect, labirinto_rect):
    for cellaa in labirinto_rect:
        if pacman_rect.colliderect(cellaa):
            return True
    return False

def collisione_ghost(ghost_rect, labirinto_rect):
    for cellaa in labirinto_rect:
        if ghost_rect.colliderect(cellaa):
            return True
    return False

class Ghost:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])
        self.possible_directions = [(-5, 0), (5, 0), (0, -5), (0, 5)]
        

    def move(self):
        

        if random.randint(0, 100) < 5:
            if collisione_ghost(ghost_rect, labirinto_rect) == True:
                self.dx, self.dy = random.choice(self.possible_directions)
                self.x += self.dx
                self.y += self.dy
            else:
                self.x -= self.dx
                self.y -= self.dy
        # Aggiungi qui ulteriori controlli per evitare collisioni o restrizioni di movimento se necessario
ghosts = []
for _ in range(4):  # Numero di fantasmi desiderato
    ghosts.append(Ghost())


def disegnalabirinto(labirinto_rect):
    cella = pygame.Surface(CELLA)
    cella.fill('blue')
    for j in range(0, len(labirinto_rect)):
        screen.blit(cella, labirinto_rect[j] )

for j in range(0, 20):
        for i in range(0, 37):
            labirintocella = pygame.Surface(CELLA) 
            if labirinto[j][i] == 1:
                labirintocella.fill('blue')
                cella_labirinto = labirintocella.get_rect()
                cella_labirinto.x = 50*i
                cella_labirinto.y = 50*j
                labirinto_rect.append(cella_labirinto)
                screen.blit(labirintocella, cella_labirinto)                
            else:
                labirintocella = pygame.Surface((20,20))
                labirintocella.fill('yellow')
                punto_rect = labirintocella.get_rect()
                punto_rect.x = 15+50*i
                punto_rect.y = 15+50*j
                punti_rect.append(punto_rect)
                screen.blit(labirintocella, punto_rect)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pacman_rect.y -= velocita
                if collisione(pacman_rect, labirinto_rect) == True:
                    pacman_rect.y += velocita
                    if mossa == 'destra':
                        pacman_rect.x += velocita
                    elif mossa == 'sinistra':
                        pacman_rect.x -= velocita                    
                else:
                    mossa = 'sopra'
            elif event.key == pygame.K_a:
                pacman_rect.x -= velocita
                if collisione(pacman_rect, labirinto_rect) == True:
                    pacman_rect.x += velocita
                    if mossa == 'sopra':
                        pacman_rect.y -= velocita
                    elif mossa == 'sotto':
                        pacman_rect.y += velocita                    
                else:
                    mossa = 'sinistra'
            elif event.key == pygame.K_s:
                pacman_rect.y += velocita
                if collisione(pacman_rect, labirinto_rect) == True:
                    pacman_rect.y -= velocita
                    if mossa == 'destra':
                        pacman_rect.x += velocita
                    elif mossa == 'sinistra':
                        pacman_rect.x -= velocita                    
                else:
                    mossa = 'sotto'
            elif event.key == pygame.K_d:
                pacman_rect.x += velocita
                if collisione(pacman_rect, labirinto_rect) == True:
                    pacman_rect.x -= velocita
                    if mossa == 'sopra':
                        pacman_rect.y -= velocita
                    elif mossa == 'sotto':
                        pacman_rect.y += velocita                    
                else:
                    mossa = 'destra'
    if len(mossa) != 0:
        if mossa == 'sopra':
            pacman_rect.y += -velocita
            if collisione(pacman_rect, labirinto_rect) == True:
                pacman_rect.y += velocita
                mossa = ''            
        elif mossa == 'sinistra':
            pacman_rect.x += -velocita
            if collisione(pacman_rect, labirinto_rect) == True:
                pacman_rect.x += velocita
                mossa = ''
        elif mossa == 'sotto':
            pacman_rect.y += velocita
            if collisione(pacman_rect, labirinto_rect) == True:
                pacman_rect.y -= velocita
                mossa = ''
        elif mossa == 'destra':
            pacman_rect.x += velocita
            if collisione(pacman_rect, labirinto_rect) == True:
                pacman_rect.x -= velocita
                mossa = ''
    screen.fill(NERO) 
   
    
    disegnalabirinto(labirinto_rect)
    screen.blit(pacman_image, pacman_rect)  
    for ghost in ghosts:
        ghost.move()
        screen.blit(ghost_image, ghost_rect)  
    pygame.display.update()

    clock.tick(fps)