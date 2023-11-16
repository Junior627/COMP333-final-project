from pygame import *
from GameStates import customization

'''
This file will contain all logic for the player and how the player controls their ship
'''

class Player:
    def __init__(self , customizationInfo):
        ''' This will be used to instantiate the Player class. There should only be one at a time
        
        Args: customizationInfo , this will be the declared instance of customization() to get parameters such as current_engine and current_weapon
        
        '''
        
        self.pos = [1,1]
        
        # This will hold all arrays of sprites animations, important ones are the idle, shoot, and moving. A single animation may need more than one sprite so we use arrays
        self.idle_sprites = ['..\player_idle.png']
        self.shoot_sprites = ['..\player_shoot.png']
        self.shoot_move = ['..\player_move.png']
        
        self.speed =  1 # This value will change depending on customizationInfo.current_engine ( we can use if-else for this )
        self.bullet_speed = 1 # These values will change depending on customizationInfo.current_weapon ( we can use if-else for this )
        self.bullet_cooldown = 100 # These values will change depending on customizationInfo.current_weapon ( we can use if-else for this )
        
        self.player = image.load(self.idle_sprites[0])
        self.player_collider  = self.player.get_rect()
        
        pass
    
    def shoot(self):
        ''' During the main gameplay loop, if the shoot button is pressed, this function will be called
        
        If the bullet_cooldown is 0, then we create a new instance of playerBullet
        
        '''
        if self.bullet_cooldown == 0:
            playerBullet(self.pos)
            self.bullet_cooldown = 100
        pass
    
    def update(self):
        '''
        Holds the logic to update the player based on whats happening around them
        
        For instance, this will countdown the self.bullet_cooldown to 0 and stopping there
        '''
    def movement(self, dir):
        ''' Called when the player touches a directional key or WASD
        Args: dir : An array of 2 elements we add to self.pos       
        
        Include some logic to prevent the player to leave the player bounds 
        '''
        self.pos = self.pos + (self.speed * dir)
        pass
        
    
class playerBullet:
    def __init__(self, initial_pos , bullet_speed):
        ''' Create an instance
        
        '''
        
        self.pos = initial_pos 
        self.bullet_speed = bullet_speed
        self.bullet = image.load('bullet.png') # Make sure this is the appropiate filepath for player's bullet
        self.bullet_collider = self.bullet.get_rect()
        pass
    def update(self):
        '''
        Updates the playerBullet's position
        '''
        self.pos -= [0, 1] # It takes away 1 since we want the bullet to go straight up
        pass
    def destroy(self):
        '''The bullet will destroy itself if it hits an enemy or an edge of the screen.'''
        pass
    
def unit_tests():
    
    ''' Unit tests for player.py would include:
    
    Hold one direction for the player and check if they don't leave the screen
        If they do not, we pass
        If so, we fail
    
    Press the shoot button and check if a new playerBullet instance is created
        If so, pass
    
    We can also test to see if the appropiate files are retrieved when the player class is initialized
        If so, pass
    '''
    
    pass