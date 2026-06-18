import pygame

class Game:
    def __init__(self):
        self.window = None

    def run (self):
        pygame.init() #inicializa o pygame
        window = pygame.display.set_mode(size=(600, 480)) #cria a janela da aplicação

        while True: #mantem a janela aberta
            for event in pygame.event.get(): # Check for all events
                if event.type == pygame.QUIT:
                    pygame.quit() # Close Window
                    quit() # end pygame
