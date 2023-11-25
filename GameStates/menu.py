import pygame
from .generic_state import generic_state

'''Code for the menu game state upon initialization.
Specific attributes:
current_option- the index of the current menu option the user is hovering over.
options- a list of the total menu options.
'''

class menu(generic_state):
    def __init__(self):
        super(menu, self).__init__()
        self.current_option = 0
        self.options = ["Fight!", "Quit Game"]
        self.next_state = "levels"
    
    def color_text(self, index):
        '''Code for text coloration
        '''
        if index == self.current_option:
            text_color = pygame.Color("cyan2")
        else:
            text_color = pygame.Color("white")
        return self.font.render(self.options[index], True, text_color)
    
    def get_event(self, event):
        '''Placeholder code for handling events
        '''
        pass

    def option_select(self):
        '''Placeholder code for option selection
        '''
        self.quit = True

    def draw(self, surface):
        '''Placeholder code for screen display
        '''
        pass