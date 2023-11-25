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
    
    def place_text(self, text, index):
        '''Code for text placement
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + (100 * index))
        return text.get_rect(center = center_location)
    
    def get_event(self, event):
        '''Placeholder code for handling events
        '''
        pass

    def option_select(self):
        '''Placeholder code for option selection
        '''
        self.quit = True

    def draw(self, surface):
        '''Code for screen display in the outer menu game state
        '''
        surface.fill(pygame.Color("midnightblue"))
        for index in range(len(self.options)):
            text_display = self.color_text(index)
            surface.blit(text_display, self.place_text(text_display, index))