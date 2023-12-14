import pygame
from .generic_state import generic_state

'''Code for the menu game state upon initialization.
Specific attributes:
current_option- the index of the current menu option the user is hovering over.
options- a list of the total menu options.
title- a list of the title of the game.
'''

class menu(generic_state):
    def __init__(self):
        super(menu, self).__init__()
        self.current_option = 0
        self.options = ["Fight!", "Quit"]
        self.title = ["THE AURORA", "ARMADA"]
        self.next_state = "levels"
    
    def color_text(self, index):
        '''Code for text coloration
        '''
        if index == self.current_option:
            text_color = pygame.Color("yellow")
        else:
            text_color = pygame.Color("white")
        return self.regularfont.render(self.options[index], True, text_color)
    
    def color_title_text(self, index):
        '''Code for title text coloration
        '''
        return self.titlefont.render(self.title[index], True, pygame.Color("white"))
    
    def color_instruction_text(self):
        '''Code for instruction text coloration
        '''
        return self.captionfont.render("Arrow keys to move, space to select/shoot, esc to quit", True, pygame.Color("white"))
    
    def place_text(self, text, index):
        '''Code for text placement
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + (50 * (index + 2)))
        return text.get_rect(center = center_location)
    
    def place_title_text(self, text, index):
        '''Code for title text placement
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + (50 * (index + 2)) - 150)
        return text.get_rect(center = center_location)
    
    def place_instruction_text(self, text):
        '''Code for instruction text placement
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + 300)
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
        surface.fill(pygame.Color("black"))
        for index in range(len(self.options)):
            text_display = self.color_text(index)
            surface.blit(text_display, self.place_text(text_display, index))
        for index in range(len(self.title)):
            text_display = self.color_title_text(index)
            surface.blit(text_display, self.place_title_text(text_display, index))
        text_display = self.color_instruction_text()
        surface.blit(text_display, self.place_instruction_text(text_display))
