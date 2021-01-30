import pygame, sys


class Game():
    runners = ()
    __startline = 20
    __finishline = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("images/background.jpg")
        pygame.display.set_caption("Carrera de Bichos")
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            self.__screen.blit(self.__background, (0,0))
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    
    
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()