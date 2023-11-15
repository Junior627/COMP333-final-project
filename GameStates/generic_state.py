import pygame

'''Skeleton code for a generic game state. Game states are implemented as
classes that share a number of common attributes, including:
done- used to determine if the game should continue in the current state.
quit- used to determine if the game should continue running.
next_state- used to determine the next state the game should transition to.
screen_rect- used to determine the dimensions of the current screen.
font- used to determine the font being used.
'''

class generic_state:
    def __init__(self):
        '''
        Font should be taken from the files directory       
        '''
        
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(None, 32)

    def startup(self):
        '''Placeholder code for state specific initialization
        '''
        pass

    def get_event(self, event):
        '''Placeholder code for handling events
        '''
        pass

    def update(self, dt):
        '''Placeholder code for state specific updates
        '''
        pass

    def draw(self, surface):
        '''Placeholder code for screen display
        '''
        pass