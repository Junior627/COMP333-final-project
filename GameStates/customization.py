import pygame
from .generic_state import generic_state

'''Skeleton code for the ship customization game state.
Specific attributes:
current_engine- the index of the current engine the user has selected.
current_weapon- the index of the current weapon the user has selected.
options_engine- a list of the total engine options.
options_weapon- a list of the total weapon options.
options_menus- a list of the menus the user will be able to navigate.
current_menu- the index of the current menu the user is in.
current_choices- a list of the indices of the current components the user has selected.
position- the current option the user is hovering over within the current menu.
'''

class customization(generic_state):
    def __init__(self):
        super(customization, self).__init__()
        self.current_engine = 0
        self.current_weapon = 0
        self.options_engine = ["ENG1", "ENG2", "ENG3"]
        self.options_weapon = ["WPN1", "WPN2", "WPN3"]
        self.options_menus = [self.options_engine, self.options_weapon]
        self.current_menu = 0
        self.current_choices = [self.current_engine, self.current_weapon]
        self.position = 0
        self.next_state = "shipgame"
    
    def color_text(self, menu, index):
        '''Code for text coloration
        '''
        if (self.current_menu == menu) and (self.position == index):
            if self.position == self.current_choices[menu]:
                text_color = pygame.Color("chartreuse")
            else:
                text_color = pygame.Color("cyan2")
        else:
            if index == self.current_choices[menu]:
                text_color = pygame.Color("yellow")
            else:
                text_color = pygame.Color("white")
        return self.regularfont.render(self.options_menus[menu][index], True, text_color)
    
    def color_instruction_text(self):
        '''Code for instruction text coloration
        '''
        return self.captionfont.render("Use arrow keys to navigate, space bar to select, escape to go back", True, pygame.Color("white"))
    
    def place_text(self, text, menu, index):
        '''Code for text placement
        '''
        center_location_x = self.screen_rect.center[0] + (175 * (index - 1))
        center_location_y = self.screen_rect.center[1] + (100 * (menu - 1) - 150)
        return text.get_rect(center = (center_location_x, center_location_y))
    
    def place_instruction_text(self, text):
        '''Code for instruction text placement
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + 300)
        return text.get_rect(center = center_location)
    
    def get_event(self, event):
        '''Code for handling events in the ship customization menu game state
        '''
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.current_menu = (self.current_menu - 1) % len(self.options_menus)
            if event.key == pygame.K_DOWN:
                self.current_menu = (self.current_menu + 1) % len(self.options_menus)
            if event.key == pygame.K_RIGHT:
                self.position = (self.position + 1) % len(self.options_menus[0])
            if event.key == pygame.K_LEFT:
                self.position = (self.position - 1) % len(self.options_menus[0])
            if event.key == pygame.K_SPACE:
                self.current_choices[self.current_menu] = self.position
            if event.key == pygame.K_ESCAPE:
                self.next_state = "levels"
                self.done = True

    def customization_selection(self):
        '''Placeholder code for engine/weapon selection
        Each engine should have a different movement speed
        Each weapon should have a different bullet speed 
        '''
        self.quit = True

    def startup(self):
        self.next_state = "shipgame"

    def draw(self, surface):
        '''Code for screen display in the ship customization game state.
        Depending on the combination of engine and weapon, we pull the appropiate sprite from the files
        '''
        surface.fill(pygame.Color("black"))
        for menu in range(len(self.options_menus)):
            for index in range(len(self.options_menus[menu])):
                text_display = self.color_text(menu, index)
                surface.blit(text_display, self.place_text(text_display, menu, index))
        text_display = self.color_instruction_text()
        surface.blit(text_display, self.place_instruction_text(text_display))
