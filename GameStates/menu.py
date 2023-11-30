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
        self.options = ["Fight!", "Quit"]
        self.next_state = "levels"
    
    def color_text(self, index):
        '''Code for text coloration
        '''
        if index == self.current_option:
            text_color = pygame.Color("cyan2")
        else:
            text_color = pygame.Color("white")
        return self.regularfont.render(self.options[index], True, text_color)
    
    def place_text(self, text, index):
        '''Code for text placement
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + (50 * (index + 1)))
        return text.get_rect(center = center_location)
    
    def get_event(self, event):
        '''Code for handling events in the outer menu game state
        '''
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.current_option = (self.current_option - 1) % len(self.options)
            if event.key == pygame.K_DOWN:
                self.current_option = (self.current_option + 1) % len(self.options)
            if event.key == pygame.K_SPACE:
                self.select_option()
            if event.key == pygame.K_ESCAPE:
                self.quit = True

    def select_option(self):
        '''Code for option selection in the outer menu game state
        '''
        if self.current_option == 1:
            self.quit = True
        elif self.current_option == 0:
            self.done = True

    def draw(self, surface):
        '''Code for screen display in the outer menu game state
        '''
        surface.fill(pygame.Color("midnightblue"))
        for index in range(len(self.options)):
            text_display = self.color_text(index)
            surface.blit(text_display, self.place_text(text_display, index))
