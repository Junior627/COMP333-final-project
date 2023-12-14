import pygame
import math
from .generic_state import generic_state
import levelcontrolparameters

'''Code for the menu game state upon level selection.
Specific attributes:
current_level- the index of the current level the user is hovering over.
unlocked_level- the final level the user has unlocked.
ASSUMES A TOTAL LEVEL NUMBER OF 15.
'''

class levels(generic_state):
    def __init__(self):
        super(levels, self).__init__()
        self.current_level = 0
        self.unlocked_level = levelcontrolparameters.unlocked_level

        self.total_rows = 5
        self.total_columns = 3
        self.total_levels = self.total_rows * self.total_columns

        self.next_state = "customization"
    
    def color_text(self, index):
        '''Code for text coloration
        Args: index- used to determine the text being colored.
        Returns: a surface containing the text after coloration.
        '''
        level_number = index + 1
        if index == self.current_level:
            text_color = pygame.Color("yellow")
        elif level_number > self.unlocked_level:
            text_color = pygame.Color("darkgray")
        else:
            text_color = pygame.Color("white")
        return self.regularfont.render(str(level_number), True, text_color)
    
    def color_instruction_text(self):
        '''Code for instruction text coloration
        Returns: a surface containing the instruction text after coloration.
        '''
        return self.captionfont.render("Arrow keys to move, space to select/shoot, esc to go back", True, pygame.Color("white"))
    
    def place_text(self, text, index):
        '''Code for text placement
        Args: text- a surface containing the colored text.
        index- used to determine the text being placed.
        Returns: a surface containing the colored text in the correct position.
        ''' 
        row = index % self.total_rows
        col = index // self.total_rows
        center_location_x = self.screen_rect.center[0] + (100 * (row - math.floor(self.total_rows / 2)))
        center_location_y = self.screen_rect.center[1] + (50 * (col - math.floor(self.total_columns / 2)))
        return text.get_rect(center = (center_location_x, center_location_y))
    
    def place_instruction_text(self, text):
        '''Code for instruction text placement
        Args: text- a surface containing the colored instruction text.
        Returns: a surface containing the colored instruction text in the correct position.
        '''
        center_location = (self.screen_rect.center[0], self.screen_rect.center[1] + 300)
        return text.get_rect(center = center_location)
    
    def find_new_level(self, key):
        '''Code for handling the response to user navigation in the level selection menu game state
        Args: the key being pressed
        Returns: the theoretical new level to be navigated to, based on the key being pressed and the
        user's current level
        '''
        if key == pygame.K_UP:
            return (self.current_level - self.total_rows) % self.total_levels
        if key == pygame.K_DOWN:
            return (self.current_level + self.total_rows) % self.total_levels
        if key == pygame.K_RIGHT:
            level = self.current_level + 1
            if level % self.total_rows == 0:
                level -= self.total_rows
            return level
        if key == pygame.K_LEFT:
            level = self.current_level
            if level % self.total_rows == 0:
                level += self.total_rows
            level -= 1
            return level
        return self.current_level

    def get_event(self, event):
        '''Code for handling events in the level selection menu game state
        Args: event- the event to be handled.
        '''
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            new_level = self.find_new_level(event.key)
            if new_level < self.unlocked_level:
                self.current_level = new_level
            if event.key == pygame.K_SPACE:
                self.select_level()
            if event.key == pygame.K_ESCAPE:
                self.next_state = "menu"
                self.done = True

    def select_level(self):
        '''Code for level selection
        '''
        levelcontrolparameters.current_level = self.current_level
        self.done = True     

    def startup(self):
        '''Code for level selection state specific initialization.
        Updates the user's unlocked levels.
        '''
        self.next_state = "customization"
        self.unlocked_level = levelcontrolparameters.unlocked_level

    def draw(self, surface):
        '''Code for screen display in the level selection menu game state
        Args: surface- the current surface.
        '''
        surface.fill(pygame.Color("black"))
        for index in range(self.total_levels):
            text_display = self.color_text(index)
            surface.blit(text_display, self.place_text(text_display, index))
        instruction_text_display = self.color_instruction_text()
        surface.blit(instruction_text_display, self.place_instruction_text(instruction_text_display))
