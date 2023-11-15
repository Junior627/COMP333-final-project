import pygame
from .generic_state import generic_state

'''Skeleton code for the ship customization game state.
Specific attributes:
current_engine- the index of the current engine the user has selected.
current_weapon- the index of the current weapon the user has selected.
options_engine- a list of the total engine options.
options_weapon- a list of the total weapon options.
'''

class customization(generic_state):
    def __init__(self):
        super(customization, self).__init__()
        self.current_engine = 1
        self.current_weapon = 1
        self.options_engine = ["engine 1", "engine 2", "engine 3"]
        self.options_weapon = ["weapon 1", "weapon 2", "weapon 3"]
        self.next_state = "shipgame"
    
    def color_text(self, index):
        '''Placeholder code for text coloration
        '''
        return self.font.render(self.options[index], True, "white")
    
    def get_event(self, event):
        '''Placeholder code for handling events
        '''
        pass

    def customization_selection(self):
        '''Placeholder code for engine/weapon selection
        Each engine should have a different movement speed
        Each weapon should have a different bullet speed 
        '''
        self.quit = True

    def draw(self, surface):
        '''Placeholder code for screen display
        Depending on the combination of engine and weapon, we pull the appropiate sprite from the files
        '''
        pass