import pygame
import math
from .generic_state import generic_state

'''Code for the menu game state upon level selection.
Specific attributes:
current_level- the current level the user is hovering over.
unlocked_level- the final level the user has unlocked.
ASSUMES A TOTAL LEVEL NUMBER OF 15.
'''

class levels(generic_state):
    def __init__(self):
        super(levels, self).__init__()
        self.current_level = 1
        self.unlocked_level = 15

        self.total_rows = 5
        self.total_columns = 3
        self.total_levels = self.total_rows * self.total_columns

        self.next_state = "customization"
    
    def color_text(self, index):
        '''Code for text coloration
        '''
        level_number = index + 1
        if index == self.current_level:
            text_color = pygame.Color("cyan2")
        elif level_number > self.unlocked_level:
            text_color = pygame.Color("darkgray")
        else:
            text_color = pygame.Color("white")
        return self.font.render(str(level_number), True, text_color)
    
    def place_text(self, text, index):
        '''Code for text placement
        '''
        row = index % self.total_rows
        col = index // self.total_rows
        center_location_x = self.screen_rect.center[0] + (100 * (row - math.floor(self.total_rows / 2)))
        center_location_y = self.screen_rect.center[1] + (50 * (col - math.floor(self.total_columns / 2)))
        return text.get_rect(center = (center_location_x, center_location_y))

    def get_event(self, event):
        '''Code for handling events in the level selection menu game state
        '''
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.current_level = (self.current_level - self.total_rows) % self.total_levels
            if event.key == pygame.K_DOWN:
                self.current_level = (self.current_level + self.total_rows) % self.total_levels
            if event.key == pygame.K_RIGHT:
                self.current_level += 1
                if (self.current_level) % self.total_rows == 0:
                    self.current_level -= self.total_rows
            if event.key == pygame.K_LEFT:
                self.current_level -= 1
                if (self.current_level) % self.total_rows == 0:
                    self.current_level += self.total_rows
            if event.key == pygame.K_SPACE:
                self.select_level()
            if event.key == pygame.K_ESCAPE:
                self.next_state = "menu"
                self.done = True

    def select_level(self):
        '''Placeholder code for level selection
        '''
        self.quit = True

    def draw(self, surface):
        '''Code for screen display in the level selection menu game state
        '''
        surface.fill(pygame.Color("midnightblue"))
        for index in range(self.total_levels):
            text_display = self.color_text(index)
            surface.blit(text_display, self.place_text(text_display, index))
