import pygame
from sys import exit
class GraphicInterface:
    def __init__(self):
        pygame.init()
        self.win_width=1200
        self.win_height=600
        self.window=pygame.display.set_mode((self.win_width,self.win_height))
        self.clock=pygame.time.Clock()
        pygame.display.set_caption("Draw Power Eletrical System")

    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
            self.window.fill("white")
            pygame.display.update()

GraphicInterface().run()




