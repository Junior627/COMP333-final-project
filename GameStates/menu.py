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
        Args: index- used to determine the text being colored.
        Returns: a surface containing the text after coloration.
        '''
        if index == self.current_option:
            text_color = pygame.Color("yellow")
        else:
            text_color = pygame.Color("white")
        return self.regularfont.render(self.options[index], True, text_color)
    
    def color_title_text(self, index):
        '''Code for title text coloration
        Args: index- used to determine the title text being colored.
        Returns: a surface containing the title text after coloration.
        '''
        return self.titlefont.render(self.title[index], True, pygame.Color("white"))
    
    def color_instruction_text(self):
        '''Code for instruction text coloration
        Returns: a surface containing the instruction text after coloration.
        '''
        return self.captionfont.render("Arrow keys to move, space to select/shoot, esc to quit", True, pygame.Color("white"))
    
    def place_text(self, text, index):
        '''Code for text placement
        Args: text- a surface containing the colored text.
        index- used to determine the text being placed.
        Returns: a surface containing the colored text in the correct position.
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + (50 * (index + 2)))
        return text.get_rect(center = center_location)
    
    def place_title_text(self, text, index):
        '''Code for title text placement
        Args: text- a surface containing the colored title text.
        index- used to determine the title text being placed.
        Returns: a surface containing the colored title text in the correct position.
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + (50 * (index + 2)) - 150)
        return text.get_rect(center = center_location)
    
    def place_instruction_text(self, text):
        '''Code for instruction text placement
        Args: text- a surface containing the colored instruction text.
        Returns: a surface containing the colored instruction text in the correct position.
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + 300)
        return text.get_rect(center = center_location)
    
    def get_event(self, event):
        '''Code for handling events in the outer menu game state
        Args: event- the event to be handled.
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
        Args: surface- the current surface.
        '''
        surface.fill(pygame.Color("black"))
        for index in range(len(self.options)):
            text_display = self.color_text(index)
            surface.blit(text_display, self.place_text(text_display, index))
        for index in range(len(self.title)):
            title_text_display = self.color_title_text(index)
            surface.blit(title_text_display, self.place_title_text(title_text_display, index))
        instruction_text_display = self.color_instruction_text()
        surface.blit(instruction_text_display, self.place_instruction_text(instruction_text_display))
