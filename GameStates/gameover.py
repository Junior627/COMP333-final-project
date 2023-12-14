import pygame
from .generic_state import generic_state

'''Code for the game state upon dying in the ship game.
Specific parameters:
game_over_text- the main text that appears upon a game over.
instruction_text- the instruction text that appears upon a game over.
game_over_text_position, instruction_text_center, instruction_text_position-
all used for the pygame display of the above text.
'''

class gameover(generic_state):
    def __init__(self):
        super(gameover, self).__init__()
        self.next_state = "levels"
        self.game_over_text = self.titlefont.render("GAME OVER", True, pygame.Color("red"))
        self.game_over_text_position = self.game_over_text.get_rect(center = self.screen_rect.center)
        self.instruction_text = self.captionfont.render("Press R to try again, or space to return to level selection", True, pygame.Color("white"))
        self.instruction_text_center = (self.screen_rect.center[0], self.screen_rect.center[1] + 100)
        self.instruction_text_position = self.instruction_text.get_rect(center = self.instruction_text_center)

    def get_event(self, event):
        '''Code for handling events in the game over menu game state
        Args: event- the event to be handled.
        '''
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.next_state = "shipgame"
                self.done = True
            if event.key == pygame.K_SPACE:
                self.done = True
            if event.key == pygame.K_ESCAPE:
                self.quit = True

    def startup(self):
        self.next_state = "levels"

    def draw(self, surface):
        '''Code for screen display in the game over menu game state
        Args: surface- the current surface.
        '''
        surface.fill(pygame.Color("black"))
        surface.blit(self.game_over_text, self.game_over_text_position)
        surface.blit(self.instruction_text, self.instruction_text_position)
