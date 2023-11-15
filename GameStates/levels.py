import pygame
from .generic_state import generic_state

'''Skeleton code for the menu game state upon level selection.
Specific attributes:
current_level- the index of the current level the user is hovering over.
'''

class menu(generic_state):
    def __init__(self):
        super(menu, self).__init__()
        self.current_levels = 1
        self.next_state = "customization"
    
    def color_text(self, index):
        '''Placeholder code for text coloration
        '''
        return self.font.render(self.options[index], True, "white")
    
    def get_event(self, event):
        '''Placeholder code for handling events
        '''
        pass

    def level_select(self):
        '''Placeholder code for level selection
        '''
        self.quit = True

    def draw(self, surface):
        '''Placeholder code for screen display
        '''
        pass