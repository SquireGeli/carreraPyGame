import pygame, sys
import random

class Runner():
    __customes = ('corredorred','corredorblue','corredorgreen','corredoryellow','corredorpink')
    def __init__(self, x=0 , y=0, custome= 'corredorred'):
        self.custome = pygame.image.load ("images/{}.jpg".format(custome))
        self.position = [x,y]
        self.name = custome
        
        
        
        
        
    def avanzar(self):
        self.position[0] += random.randint(1,6)
     
    
    
class Game():
    runners = []
    __posY = (160, 200, 240, 280, 320)
    __names = ('red', 'blue', 'green', 'yellow', 'mario')
    __startline = -15
    __finishline = 800
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((840,480))
        self.__background = pygame.image.load("images/background.jpg")
        
        pygame.display.set_caption("Carrera de Enanitos")
        
        for i in range(5):
            
            theRunner = Runner(self.__startline,self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append (theRunner)
            
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishline:
                    print("{} HA GANADO!!!".format(activeRunner.name))
                    gameOver= True
                    
            self.__screen.blit(self.__background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome,runner.position)
            
            
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
       
    
    
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()