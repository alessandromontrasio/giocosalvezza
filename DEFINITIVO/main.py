import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.font.init()

ALTEZZA = 1000
LARGHEZZA= 1850
FINESTRA = (LARGHEZZA, ALTEZZA)
CELLA = (50, 50)
NERO = (0,0,0)
BIANCO = (250, 250, 250)
velocita = 2
mossefantasmi = ['sopra', 'sotto', 'sinistra', 'destra']
# flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.OPENGL
screen = pygame.display.set_mode(FINESTRA) #flags
pygame.display.set_caption('PACMAN')
font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 100)

clock = pygame.time.Clock()
fps = 60

labirinto = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

pacman_image = pygame.image.load('pacman.png').convert_alpha()
pacman_image = pygame.transform.scale(pacman_image, CELLA)
pacman_rect = pacman_image.get_rect()
pacman_rect.x = 50
pacman_rect.y = 50
punti_image = pygame.image.load('pallino.png').convert_alpha()
punti_image = pygame.transform.scale(punti_image, (20, 20))
cella_image = pygame.image.load('blocco.png').convert_alpha()
cella_image = pygame.transform.scale(cella_image, CELLA)
fantasma_image = pygame.image.load('fantasma.png').convert_alpha()
fantasma_image = pygame.transform.scale(fantasma_image, CELLA)
labirinto_rect = []
punti_rect = []
fantasmi_rect = []
secondi = [0, 0, 0, 0]
movefantasma = 'sopra'
mossepossibili = ['sopra', 'sotto', 'destra', 'sinistra']
score = 0
mossepossibiliprima = 0

mossa = ''
mossavoluta = ''
mossavolutafantasma = ''

pygame.display.flip()

def collisione(pacman_rect, lista_da_controllare):
    for el in lista_da_controllare:
        if pacman_rect.colliderect(el):
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

def controllopunti(punti_rect, pacman_rect, score):
    controllo = ''
    for z in range(0, len(punti_rect)):
        if pacman_rect.colliderect(punti_rect[z]) == True:
            dacontrollare = z
            controllo = 'g'
            score += 10
    if len(controllo) != 0:
        punti_rect.pop(dacontrollare)
    return score

def stampapunteggio(score):
    score_testo = font.render("Punteggio: " + str(score), True, BIANCO)
    screen.blit(score_testo, (10, 10))

def controllovittoria(punti_rect, font2):
    if len(punti_rect) == 0:
        vittoria_testo = font2.render("Hai Vinto", True, BIANCO)
        vittoria_rect = vittoria_testo.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2))
        screen.blit(vittoria_testo, vittoria_rect)
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

def controllo_contatti_pacman_fantasmi(pacman_rect, fantasmi_rect):
    if collisione(pacman_rect, fantasmi_rect):
        game_over_text = font2.render("Game Over", True, BIANCO)
        game_over_rect = game_over_text.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2))
        screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()


def movimentofantasmi(fantasmi_rect, labirinto_rect, velocita, movefantasma, mossepossibiliprima):
    for s in range(0, len(fantasmi_rect)):
        ricordo = ''       
        mossepossibili = []
        fantasma = fantasmi_rect[s]
        fantasma.x -= velocita
        if collisione(fantasma, labirinto_rect) == False:
            mossepossibili.append('sinistra')
        fantasma.x += 2*velocita
        if collisione(fantasma, labirinto_rect) == False:
            mossepossibili.append('destra')
        fantasma.x -= velocita
        fantasma.y += velocita
        if collisione(fantasma, labirinto_rect) == False:
            mossepossibili.append('sotto')
        fantasma.y -= 2*velocita
        if collisione(fantasma, labirinto_rect) == False:
            mossepossibili.append('sopra')
        fantasma.y += velocita
        if len(mossepossibili) != mossepossibiliprima:
            movefantasma = random.choice(mossepossibili)
            if movefantasma == 'sopra':
                fantasma.y -= velocita
            elif movefantasma == 'destra':
                fantasma.x += velocita
            elif movefantasma == 'sinistra':
                fantasma.x -= velocita
            elif movefantasma == 'sotto':
                fantasma.y += velocita
        else:
            if movefantasma == 'sopra':
                if movefantasma in mossepossibili:
                    fantasma.y -= velocita
                else :
                    nuovamovefantasma = random.choice(mossepossibili)
                    ricordo = 'g'
                    if nuovamovefantasma == 'sopra':
                        fantasma.y -= velocita
                    elif nuovamovefantasma == 'destra':
                        fantasma.x += velocita
                    elif nuovamovefantasma == 'sinistra':
                        fantasma.x -= velocita
                    elif nuovamovefantasma == 'sotto':
                        fantasma.y += velocita
                    movefantasma = nuovamovefantasma

            elif movefantasma == 'sotto':
                if movefantasma in mossepossibili:
                    fantasma.y += velocita
                else :
                    nuovamovefantasma = random.choice(mossepossibili)
                    ricordo = 'g'
                    if nuovamovefantasma == 'sopra':
                        fantasma.y -= velocita
                    elif nuovamovefantasma == 'destra':
                        fantasma.x += velocita
                    elif nuovamovefantasma == 'sinistra':
                        fantasma.x -= velocita
                    elif nuovamovefantasma == 'sotto':
                        fantasma.y += velocita
                    movefantasma = nuovamovefantasma
            
            elif movefantasma == 'destra':
                if movefantasma in mossepossibili:
                    fantasma.x += velocita
                else :
                    nuovamovefantasma = random.choice(mossepossibili)
                    ricordo = 'g'
                    if nuovamovefantasma == 'sopra':
                        fantasma.y -= velocita
                    elif nuovamovefantasma == 'destra':
                        fantasma.x += velocita
                    elif nuovamovefantasma == 'sinistra':
                        fantasma.x -= velocita
                    elif nuovamovefantasma == 'sotto':
                        fantasma.y += velocita
                    movefantasma = nuovamovefantasma

            elif movefantasma == 'sinistra':
                if movefantasma in mossepossibili:
                    fantasma.x -= velocita
                else :
                    nuovamovefantasma = random.choice(mossepossibili)
                    ricordo = 'g'
                    if nuovamovefantasma == 'sopra':
                        fantasma.y -= velocita
                    elif nuovamovefantasma == 'destra':
                        fantasma.x += velocita
                    elif nuovamovefantasma == 'sinistra':
                        fantasma.x -= velocita
                    elif nuovamovefantasma == 'sotto':
                        fantasma.y += velocita 
                    movefantasma = nuovamovefantasma
        if ricordo == 'g':
            movefantasma = nuovamovefantasma
                    
        mossepossibiliprima = len(mossepossibili)
    
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

    movimentofantasmi(fantasmi_rect, labirinto_rect, velocita, movefantasma, mossepossibiliprima)
    
    score = controllopunti(punti_rect, pacman_rect, score)

    screen.fill(NERO) 
    disegnalabirinto(labirinto_rect, punti_rect)
    screen.blit(pacman_image, pacman_rect) 
    disegnafantasmi(fantasmi_rect)
    controllovittoria(punti_rect, font2)
    controllo_contatti_pacman_fantasmi(pacman_rect, fantasmi_rect)
    stampapunteggio(score)
    pygame.display.update()
    clock.tick(fps)