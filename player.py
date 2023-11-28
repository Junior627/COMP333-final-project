from pygame import *
from GameStates import customization

'''
This file will contain all logic for the player and how the player controls their ship

Currently using a test.py file to incorporate this stuff. Once the gameloop is figured out, i will convert the stuff to the main file
'''

class Player:
    def __init__(self , size):
        ''' This will be used to instantiate the Player class. There should only be one at a time
        
        Args: customizationInfo , this will be the declared instance of customization() to get parameters such as current_engine and current_weapon
        
        '''
        
        self.pos = [1,1]
        
        # idle = "player"+customizationInfo.options_engine[customizationInfo.current_engine]+"_"+customizationInfo.options_weapon[customizationInfo.current_weapon]+"idle.png"
        idle = "Sprites\player_idle.png"
        # This will hold all arrays of sprites animations, important ones are the idle, shoot, and moving. A single animation may need more than one sprite so we use arrays
        self.idle_sprites = [idle]
        self.shoot_sprites = ['Sprites\player_shoot.png']
        self.shoot_move = ['Sprites\player_move.png']
        
        self.speed =  3 # This value will change depending on customizationInfo.current_engine ( we can use if-else for this )
        self.bullet_speed = 5 # These values will change depending on customizationInfo.current_weapon ( we can use if-else for this )
        self.bullet_cooldown = 25 # These values will change depending on customizationInfo.current_weapon ( we can use if-else for this )
        
        self.player = image.load(self.idle_sprites[0])
        self.player_collider  = self.player.get_rect()
        self.dir= [0,0]
        
        # Parameters for pygame interactivity
        self.size = size # Used to draw the character on screen
        
        pass
    
    def shoot(self):
        ''' During the main gameplay loop, if the shoot button is pressed, this function will be called
        
        If the bullet_cooldown is 0, then we create a new instance of PlayerBullet
        
        '''
        if self.bullet_cooldown == 0:
            self.bullet_cooldown = 25
            print(self.pos)
            return PlayerBullet([self.pos[0]+ (self.player_collider.width / 2), self.pos[1]], self.bullet_speed , self.size)
    
    def update(self, dir):
        '''
        Holds the logic to update the player based on whats happening around them
        
        For instance, this will countdown the self.bullet_cooldown to 0 and stopping there
        '''
        if(self.bullet_cooldown >0):
            self.bullet_cooldown-= 1

        
    
        self.movement(dir)
        
    def movement(self, dir):
        ''' Called when the player touches a directional key or WASD
        Args: dir : An array of 2 elements we add to self.pos       
        
        Include some logic to prevent the player from leaving the player bounds 
        '''
        x_pos = self.speed * dir[0]
        y_pos = self.speed * dir[1]

        # Update player position
        new_x = self.pos[0] + x_pos
        new_y = self.pos[1] + y_pos

        # Check if the new position is within the bounds of the screen
        if 0 > self.player_collider.left:
            self.pos[0] = 0
        elif self.size[0] < self.player_collider.right:
            self.pos[0] = self.size[0] - self.player_collider.width
        else:
            self.pos[0] = new_x
            
        if 0 > self.player_collider.top :
            self.pos[1] = 0
        elif self.size[1] < self.player_collider.bottom :
            self.pos[1] = self.size[1] - self.player_collider.height
        else:
            self.pos[1] = new_y
            
            

        # Update player collider based on the new position
        self.player_collider = self.player_collider.move(self.pos[0] - self.player_collider.x, self.pos[1] - self.player_collider.y)

        pass

        
    
class PlayerBullet:
    def __init__(self, initial_pos , bullet_speed, size):
        ''' Create an instance
        
        '''
        self.size = size
        self.pos = initial_pos 
        self.bullet_speed = bullet_speed
        self.bullet = image.load('Sprites\player_bullet.png') # Make sure this is the appropiate filepath for player's bullet
        self.bullet_collider = self.bullet.get_rect()
        print("Created at", self.pos)
        pass
    def update(self):
        '''
        Updates the PlayerBullet's position
        '''
        
        self.pos = [self.pos[0], (self.pos[1] - self.bullet_speed)] # It takes away 1 since we want the bullet to go straight up
        self.bullet_collider = self.bullet_collider.move(self.pos[0] - self.bullet_collider.x, self.pos[1] - self.bullet_collider.y)
    def __del__(self):
        '''The bullet will destroy itself if it hits an enemy or an edge of the screen.'''
        print('Bullet Gone!')
        
    
def unit_tests():
    
    ''' Unit tests for player.py would include:
    
    Hold one direction for the player and check if they don't leave the screen
        If they do not, we pass
        If so, we fail
    
    Press the shoot button and check if a new PlayerBullet instance is created
        If so, pass
    
    We can also test to see if the appropiate files are retrieved when the player class is initialized
        If so, pass
    '''
    
    pass