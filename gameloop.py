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

    def change_state(self):
        '''Code for changing the gamestate
        '''
        self.state_name = self.state.next_state
        self.state = self.total_states[self.state_name]
        
        self.state.done = False

        self.state.startup()

    def update(self, dt):
        '''Code for updating the gamestate
        '''
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.change_state()
        self.state.update(dt)

    def draw(self):
        '''Code for screen display throughout all gamestates
        '''
        self.screen.fill((0, 0, 0))
        self.state.draw(self.screen)

    def run(self):
        '''Code for the full pygame loop
        '''
        while not self.done:
            dt = self.clock.tick(self.fps)
            
            for event in pygame.event.get():
                self.state.get_event(event)

            self.update(dt)
            self.draw()
            pygame.display.update()
