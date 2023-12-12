import pygame
from .generic_state import generic_state
import levelcontrolparameters

'''Code for the game state upon winning in the ship game.
Specific parameters:
victory_text- the main text that appears upon a victory.
instruction_text- the instruction text that appears upon a victory.
victory_text_position, instruction_text_center, instruction_text_position-
all used for the pygame display of the above text.
'''

class victory(generic_state):
    def __init__(self):
        super(victory, self).__init__()
        self.next_state = "levels"
        self.victory_text = self.titlefont.render("YOU WIN", True, pygame.Color("yellow"))
        self.victory_text_position = self.victory_text.get_rect(center = self.screen_rect.center)
        self.instruction_text = self.captionfont.render("Press space to return to level selection", True, pygame.Color("white"))
        self.instruction_text_center = (self.screen_rect.center[0], self.screen_rect.center[1] + 100)
        self.instruction_text_position = self.instruction_text.get_rect(center = self.instruction_text_center)

    def startup(self):
        if levelcontrolparameters.current_level + 1 == levelcontrolparameters.unlocked_level and levelcontrolparameters.current_level != 14:
            self.instruction_text = self.captionfont.render("A new level has been unlocked. Press space to return to level selection", True, pygame.Color("white"))
        else:
            self.instruction_text = self.captionfont.render("Press space to return to level selection", True, pygame.Color("white"))
        self.instruction_text_center = (self.screen_rect.center[0], self.screen_rect.center[1] + 100)
        self.instruction_text_position = self.instruction_text.get_rect(center = self.instruction_text_center)


    def get_event(self, event):
        '''Code for handling events in the game over menu game state
        '''
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if levelcontrolparameters.current_level + 1 == levelcontrolparameters.unlocked_level and levelcontrolparameters.current_level != 14:
                    levelcontrolparameters.unlocked_level += 1
                self.done = True
            if event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        '''Code for screen display in the game over menu game state
        '''
        surface.fill(pygame.Color("black"))
        surface.blit(self.victory_text, self.victory_text_position)
        surface.blit(self.instruction_text, self.instruction_text_position)
