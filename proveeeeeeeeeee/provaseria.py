import pygame, sys, random
from pygame.locals import *

ALTEZZA = 1000
LARGHEZZA= 1850
FINESTRA = (LARGHEZZA, ALTEZZA)
CELLA = (50, 50)
NERO = (0,0,0)
velocita = 5
mossefantasmi = ['sopra', 'sotto', 'sinistra', 'destra']
# flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.OPENGL
screen = pygame.display.set_mode(FINESTRA) #flags
pygame.display.set_caption('Zambrotta prime')

clock = pygame.time.Clock()
fps = 30

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

pacman_image = pygame.image.load('pacman.png')
pacman_image = pygame.transform.scale(pacman_image, CELLA)
pacman_rect = pacman_image.get_rect()
pacman_rect.x = 50
pacman_rect.y = 50
punti_image = pygame.image.load('pixil-frame-0.png')
punti_image = pygame.transform.scale(punti_image, (20, 20))
cella_image = pygame.image.load('blocco.png')
cella_image = pygame.transform.scale(cella_image, CELLA)
fantasma_image = pygame.image.load('pacman.png')
fantasma_image = pygame.transform.scale(fantasma_image, CELLA)
labirinto_rect = []
punti_rect = []
fantasmi_rect = []
movefantasma = 'sopra'
mossepossibili = ['sopra', 'sotto', 'destra', 'sinistra']

mossa = ''
mossavoluta = ''

pygame.display.flip()

def collisione(pacman_rect, labirinto_rect):
    for cellaa in labirinto_rect:
        if pacman_rect.colliderect(cellaa):
            return True
    return False

def disegnalabirinto(labirinto_rect, punti_rect):
    for j in range(0, len(labirinto_rect)):
        screen.blit(cella_image, labirinto_rect[j])
    for i in range(0, len(punti_rect)):
        screen.blit(punti_image, punti_rect[i])

def disegnafantasmi(fantasmi_rect):
    for s in range(0, len(fantasmi_rect)):
        screen.blit(fantasma_image, fantasmi_rect[s]) 

def controllopunti(punti_rect, pacman_rect):
    controllo = ''
    for z in range(0, len(punti_rect)):
        if pacman_rect.colliderect(punti_rect[z]) == True:
            dacontrollare = z
            controllo = 'g'
    if len(controllo) != 0:
        punti_rect.pop(dacontrollare)  

def movefantasmi(fantasmi_rect, movefantasma):
    for s in range(0, len(fantasmi_rect)):       
        if len(movefantasma) != 0:
            if movefantasma == 'sopra':
                fantasmi_rect[s].y -= velocita
                if collisione(fantasmi_rect[s], labirinto_rect):
                    fantasmi_rect[s].y += velocita
                    movefantasma = random.choice(mossepossibili)
                    if movefantasma == 'sopra':
                        fantasmi_rect[s].y -= velocita
                    elif movefantasma == 'destra':
                        fantasmi_rect[s].x += velocita
                    elif movefantasma == 'sotto':
                        fantasmi_rect[s].y += velocita
                    elif movefantasma == 'sinistra':
                        fantasmi_rect[s].x -= velocita

                    while collisione(fantasmi_rect[s], labirinto_rect):
                        if movefantasma == 'sopra':
                            fantasmi_rect[s].y += velocita
                        elif movefantasma == 'destra':
                            fantasmi_rect[s].x -= velocita
                        elif movefantasma == 'sotto':
                            fantasmi_rect[s].y -= velocita
                        elif movefantasma == 'sinistra':
                            fantasmi_rect[s].x += velocita
                        movefantasma = random.choice(mossepossibili)
                        if movefantasma == 'sopra':
                            fantasmi_rect[s].y -= velocita
                        elif movefantasma == 'destra':
                            fantasmi_rect[s].x += velocita
                        elif movefantasma == 'sotto':
                            fantasmi_rect[s].y += velocita
                        elif movefantasma == 'sinistra':
                            fantasmi_rect[s].x -= velocita
            elif movefantasma == 'destra':
                fantasmi_rect[s].x += velocita
                if collisione(fantasmi_rect[s], labirinto_rect):
                    fantasmi_rect[s].x -= velocita
                    movefantasma = random.choice(mossepossibili)
                    if movefantasma == 'sopra':
                        fantasmi_rect[s].y -= velocita
                    elif movefantasma == 'destra':
                        fantasmi_rect[s].x += velocita
                    elif movefantasma == 'sotto':
                        fantasmi_rect[s].y += velocita
                    elif movefantasma == 'sinistra':
                        fantasmi_rect[s].x -= velocita

                    while collisione(fantasmi_rect[s], labirinto_rect):
                        if movefantasma == 'sopra':
                            fantasmi_rect[s].y += velocita
                        elif movefantasma == 'destra':
                            fantasmi_rect[s].x -= velocita
                        elif movefantasma == 'sotto':
                            fantasmi_rect[s].y -= velocita
                        elif movefantasma == 'sinistra':
                            fantasmi_rect[s].x += velocita
                        movefantasma = random.choice(mossepossibili)
                        if movefantasma == 'sopra':
                            fantasmi_rect[s].y -= velocita
                        elif movefantasma == 'destra':
                            fantasmi_rect[s].x += velocita
                        elif movefantasma == 'sotto':
                            fantasmi_rect[s].y += velocita
                        elif movefantasma == 'sinistra':
                            fantasmi_rect[s].x -= velocita
            elif movefantasma == 'sotto':
                fantasmi_rect[s].y += velocita
                if collisione(fantasmi_rect[s], labirinto_rect):
                    fantasmi_rect[s].y -= velocita
                    movefantasma = random.choice(mossepossibili)
                    if movefantasma == 'sopra':
                        fantasmi_rect[s].y -= velocita
                    elif movefantasma == 'destra':
                        fantasmi_rect[s].x += velocita
                    elif movefantasma == 'sotto':
                        fantasmi_rect[s].y += velocita
                    elif movefantasma == 'sinistra':
                        fantasmi_rect[s].x -= velocita

                    while collisione(fantasmi_rect[s], labirinto_rect):
                        if movefantasma == 'sopra':
                            fantasmi_rect[s].y += velocita
                        elif movefantasma == 'destra':
                            fantasmi_rect[s].x -= velocita
                        elif movefantasma == 'sotto':
                            fantasmi_rect[s].y -= velocita
                        elif movefantasma == 'sinistra':
                            fantasmi_rect[s].x += velocita
                        movefantasma = random.choice(mossepossibili)
                        if movefantasma == 'sopra':
                            fantasmi_rect[s].y -= velocita
                        elif movefantasma == 'destra':
                            fantasmi_rect[s].x += velocita
                        elif movefantasma == 'sotto':
                            fantasmi_rect[s].y += velocita
                        elif movefantasma == 'sinistra':
                            fantasmi_rect[s].x -= velocita
            elif movefantasma == 'sinistra':
                fantasmi_rect[s].x -= velocita
                if collisione(fantasmi_rect[s], labirinto_rect):
                    fantasmi_rect[s].x += velocita
                    movefantasma = random.choice(mossepossibili)
                    if movefantasma == 'sopra':
                        fantasmi_rect[s].y -= velocita
                    elif movefantasma == 'destra':
                        fantasmi_rect[s].x += velocita
                    elif movefantasma == 'sotto':
                        fantasmi_rect[s].y += velocita
                    elif movefantasma == 'sinistra':
                        fantasmi_rect[s].x -= velocita

                    while collisione(fantasmi_rect[s], labirinto_rect):
                        if movefantasma == 'sopra':
                            fantasmi_rect[s].y += velocita
                        elif movefantasma == 'destra':
                            fantasmi_rect[s].x -= velocita
                        elif movefantasma == 'sotto':
                            fantasmi_rect[s].y -= velocita
                        elif movefantasma == 'sinistra':
                            fantasmi_rect[s].x += velocita
                        movefantasma = random.choice(mossepossibili)
                        if movefantasma == 'sopra':
                            fantasmi_rect[s].y -= velocita
                        elif movefantasma == 'destra':
                            fantasmi_rect[s].x += velocita
                        elif movefantasma == 'sotto':
                            fantasmi_rect[s].y += velocita
                        elif movefantasma == 'sinistra':
                            fantasmi_rect[s].x -= velocita
        


        

for j in range(0, 20):
        for i in range(0, 37):
            if labirinto[j][i] == 1:
                labirintocella = pygame.Surface(CELLA)
                cella_labirinto = labirintocella.get_rect()
                cella_labirinto.x = 50*i
                cella_labirinto.y = 50*j
                labirinto_rect.append(cella_labirinto)
                screen.blit(cella_image, cella_labirinto)                
            else:
                labirintocella = pygame.Surface((20,20))
                punto_rect = labirintocella.get_rect()
                punto_rect.x = 15+50*i
                punto_rect.y = 15+50*j
                punti_rect.append(punto_rect)
                screen.blit(punti_image, punto_rect)
for s in range(0, 4):
    fantasma = pygame.Surface(CELLA)
    fantasma_rect = fantasma.get_rect()
    fantasma_rect.y = 900
    fantasma_rect.x = 1750
    fantasmi_rect.append(fantasma_rect)
    screen.blit(fantasma_image, fantasma_rect)


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
                    mossavoluta = 'sopra'
                    if mossa == 'destra':
                        pacman_rect.x += velocita
                    elif mossa == 'sinistra':
                        pacman_rect.x -= velocita                    
                else:
                    if mossa == 'sotto':
                        mossavoluta = ''
                    mossa = 'sopra'
            elif event.key == pygame.K_a:
                pacman_rect.x -= velocita
                if collisione(pacman_rect, labirinto_rect) == True:
                    pacman_rect.x += velocita
                    mossavoluta = 'sinistra'
                    if mossa == 'sopra':
                        pacman_rect.y -= velocita
                    elif mossa == 'sotto':
                        pacman_rect.y += velocita                    
                else:
                    if mossa == 'destra':
                        mossavoluta = ''           
                    mossa = 'sinistra'
            elif event.key == pygame.K_s:
                pacman_rect.y += velocita
                if collisione(pacman_rect, labirinto_rect) == True:
                    pacman_rect.y -= velocita
                    mossavoluta = 'sotto'
                    if mossa == 'destra':
                        pacman_rect.x += velocita
                    elif mossa == 'sinistra':
                        pacman_rect.x -= velocita                    
                else:
                    if mossa == 'sopra':
                        mossavoluta = ''
                    mossa = 'sotto'
            elif event.key == pygame.K_d:
                pacman_rect.x += velocita
                if collisione(pacman_rect, labirinto_rect) == True:
                    pacman_rect.x -= velocita
                    mossavoluta = 'destra'
                    if mossa == 'sopra':
                        pacman_rect.y -= velocita
                    elif mossa == 'sotto':
                        pacman_rect.y += velocita                    
                else:
                    if mossa == 'sinistra':
                        mossavoluta = ''
                    mossa = 'destra'
    if len(mossavoluta) != 0:
        if mossavoluta == 'sopra':
            pacman_rect.y -= velocita
            if collisione (pacman_rect, labirinto_rect) == True:
                pacman_rect.y += velocita
            else:
                pacman_rect.y += velocita
                mossa = 'sopra'
                mossavoluta = ''
        elif mossavoluta == 'sotto':
            pacman_rect.y += velocita
            if collisione (pacman_rect, labirinto_rect) == True:
                pacman_rect.y -= velocita
            else:
                pacman_rect.y -= velocita
                mossa = 'sotto'
                mossavoluta = ''
        elif mossavoluta == 'sinistra':
            pacman_rect.x -= velocita
            if collisione (pacman_rect, labirinto_rect) == True:
                pacman_rect.x += velocita
            else:
                pacman_rect.x += velocita
                mossa = 'sinistra'
                mossavoluta = ''
        elif mossavoluta == 'destra':
            pacman_rect.x += velocita
            if collisione (pacman_rect, labirinto_rect) == True:
                pacman_rect.x -= velocita
            else:
                pacman_rect.x -= velocita
                mossa = 'destra'
                mossavoluta = ''
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

    movefantasmi(fantasmi_rect, movefantasma)
    
    controllopunti(punti_rect, pacman_rect)

    screen.fill(NERO) 
    disegnalabirinto(labirinto_rect, punti_rect)
    screen.blit(pacman_image, pacman_rect) 
    disegnafantasmi(fantasmi_rect)
    pygame.display.update()

    clock.tick(fps)