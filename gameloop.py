import pygame
import constants

'''The main game loop. Includes the following attributes:
done- used to determine if the game should continue in the current state.
screen- the current game screen
clock- the current game clock
fps- the current game frames per second
total_states- a dictionary containing all of the game state names and their corresponding objects
state_name- the current game state name
state- the current game state object
'''
class Game:
    def __init__(self, screen, total_states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = constants.FRAMES_PER_SECOND

        self.total_states = total_states
        self.state_name = start_state
        self.state = self.total_states[self.state_name]

    def state_change(self):
        '''Placeholder code for changing states
        '''
        pass

    def update(self, dt):
        '''Placeholder code for state specific updates
        '''
        pass

    def draw(self):
        '''Code for screen display throughout all gamestates
        '''
        self.screen.fill((0, 0, 0))
        self.state.draw(self.screen)

    def run(self):
        '''Code for the full pygame loop
        '''
        while not self.done:
            self.draw()
            pygame.display.update()
            pygame.time.delay(1000)