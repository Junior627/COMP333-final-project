from pygame import *
from constants import *
'''
This file will contain all logic for the player and how the player controls their ship

Currently using a test.py file to incorporate this stuff. Once the gameloop is figured out, i will convert the stuff to the main file
'''

class Player:
    def __init__(self ):
        ''' This will be used to instantiate the Player class. There should only be one at a time
                
        '''
        
        self.pos = Vector2(SCREEN_WIDTH / 2 , (SCREEN_HEIGHT * 3) / 4)
        self.pos.x = SCREEN_WIDTH / 2 
        self.pos.y = (SCREEN_HEIGHT * 3) / 4
        
        idle = "Sprites\player_idle.png"
        # This will hold all arrays of sprites animations, important ones are the idle, shoot, and moving. A single animation may need more than one sprite so we use arrays
        self.idle_sprites = [idle]
        
        self.entity = image.load(self.idle_sprites[0])
        self.entity_collider  = self.entity.get_rect()
        self.dir = Vector2()
        self.dir.x = 0
        self.dir.y = 0
        
        # Parameters for pygame interactivity        
        pass
    def initStats(self, weapon_choice, engine_choice):
        
        self.entity = image.load("Sprites\player_weapon"+str(weapon_choice)+"_engine"+str(engine_choice)+".png")
        self.entity_collider  = self.entity.get_rect()
        
        # Player Stats Constants ( used to hold all information that gets updated such as invincibility window and bullet cooldown)
        
        # Weapon 0 -> Faster Shootout, Lower Damage
        # Weapon 1 -> Average Shootout and Damage
        # Weapon 2 -> Slower Shootout, Higher Damage
        
        if weapon_choice == 0:
            self.bullet_damage = 1
            self.bullet_speed = 8
            self.BULLET_CONSTANT = 25
        
        elif weapon_choice == 1:
            self.bullet_damage = 2
            self.bullet_speed = 6
            self.BULLET_CONSTANT = 45
            
        elif weapon_choice == 2:
            self.bullet_damage = 3
            self.bullet_speed = 4
            self.BULLET_CONSTANT = 65
        
        # Engine 0 -> Faster Movement, Lower Health
        # Engine 1 -> Average Movement and Health
        # Engine 2 -> Slower Movement, Higher Health
        
        if engine_choice == 0:
            self.health = 2
            self.speed = 5
            self.INVIN_CONSTANT = 45
        
        elif engine_choice == 1:
            self.health = 3
            self.speed = 3
            self.INVIN_CONSTANT = 55
            
        elif engine_choice == 2:
            self.health = 5
            self.speed = 2.5
            self.INVIN_CONSTANT = 65
        
        self.bullet_cooldown = self.BULLET_CONSTANT
        self.invincibility_window = self.INVIN_CONSTANT
    def takeDamage(self) :
        ''' If the player's invincibility window is over
        
        '''
        
        if self.invincibility_window == 0:
            self.health -= 1
            self.invincibility_window = self.INVIN_CONSTANT
        
    def shoot(self):
        ''' During the main gameplay loop, if the shoot button is pressed, this function will be called
        
        If the bullet_cooldown is 0, then we create a new instance of PlayerBullet
        
        '''
        if self.bullet_cooldown == 0:
            self.bullet_cooldown = self.BULLET_CONSTANT
            return PlayerBullet(Vector2(self.entity_collider.centerx, self.pos.y), self.bullet_speed )
    
    def update(self, dir):
        '''
        Holds the logic to update the player based on whats happening around them
        
        For instance, this will countdown the self.bullet_cooldown to 0 and stopping there
        '''
        if self.invincibility_window > 0 :
            self.invincibility_window -= 1
        
        if(self.bullet_cooldown >0):
            self.bullet_cooldown -= 1

        self.entity_collider = self.entity_collider.move(self.movement(dir))
    
    def movement(self, dir):
        ''' Called when the player touches a directional key or WASD
        Args: dir : An array of 2 elements we add to self.pos       
        
        Include some logic to prevent the player from leaving the player bounds 
        '''
        if dir.x !=0 and dir.y != 0:
            dir.normalize_ip()
        temp_pos = self.speed * dir
        # Update player position
        new_pos = self.pos + temp_pos
        # Check if the new position is within the bounds of the screen
        if 0 > self.entity_collider.left:
            self.pos.x = 0
        elif SCREEN_WIDTH < self.entity_collider.right:
            self.pos.x = SCREEN_WIDTH - self.entity_collider.width
        else:
            self.pos.x = new_pos.x
            
        if SCREEN_HEIGHT / 2 > self.entity_collider.top :
            self.pos.y = SCREEN_HEIGHT / 2
        elif SCREEN_HEIGHT < self.entity_collider.bottom :
            self.pos.y = SCREEN_HEIGHT - self.entity_collider.height
        else:
            self.pos.y = new_pos.y
            
            

        # Update player collider based on the new position
        return(self.pos.x - self.entity_collider.x, self.pos.y - self.entity_collider.y)
    
class PlayerBullet:
    def __init__(self, initial_pos , bullet_speed):
        ''' Create an instance
        
        '''
        self.pos = Vector2(initial_pos )
        self.bullet_speed = bullet_speed
        self.bullet = image.load('Sprites\player_bullet.png') # Make sure this is the appropiate filepath for player's bullet
        self.bullet_collider = self.bullet.get_rect()
        self.bullet_dir = Vector2()
        self.bullet_dir.x = 0
        self.bullet_dir.y = 1
        pass
    def update(self):
        '''
        Updates the PlayerBullet's position
        '''
        
        self.pos.y -=  ( self.bullet_speed) # It takes away 1 since we want the bullet to go straight up
        self.bullet_collider = self.bullet_collider.move(self.pos.x - self.bullet_collider.x, self.pos.y - self.bullet_collider.y)
    def out_of_bounds(self):
        return self.pos[0] < 0 or self.pos[0] > SCREEN_WIDTH or self.pos[1] <0 or self.pos[1] > SCREEN_HEIGHT
    def __del__(self):
        '''The bullet will destroy itself if it hits an enemy or an edge of the screen.'''

        
    
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