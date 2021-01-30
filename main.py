import pygame
import sys

class Runner():
    pass

class Game():
    corredores = []
    def __init__(self):
        
        self.screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de Bichos")
        self.background = pygame.image.load("images/background.jpg")
        
        
        self.runner = pygame.image.load("images/corredor.png")
    
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
            #Comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
             
            #Renderizar(refrescar) la pantalla
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.runner, (x,240))
            pygame.display.flip()
            
            x += 3
            if x >= 250:
                hayGanador= True
                
                
        pygame.quit()
        sys.exit()
    
if __name__ == '__main__':
    pygame.init()
    game= Game()
    game.competir()