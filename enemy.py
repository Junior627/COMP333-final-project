'''This is the skeleton code for the enemy-related code

Since there are three distinct versions of the common enemy

Shooter: Keeps their distance from the player and tries to shoot from afar

Chaser: Tries to crash into the player any moment after a few seconds spawning

Dancer: Follows a pattern of shooting at the player then swooping into the player until defeat


'''
from pygame import *

class Shooter:
    ''' This creates an instance of the Shooter enemy
    '''
    def __init__(self):
        '''
        This will initilize the Shooter Enemy and store information
        such as:
            Sprites needed for all animations ( each animation will have a list of their appropiate images)
            Position Values needed to determine where they are in the screen
            Time value to determine how long to shoot their next bullets ( cooldown)
            Values such as movement speed 
        '''
        self.pos = [0 , 0] # Keeps track of the enemy's position on screen
        self.idle_sprites = ['..\shooter_idle.png'] # Will keep a string of the file path for the idle sprites ( could be an array to easily loop if the idle animation is more than 1 frame)
        self.shoot_sprites = ['..\shooter_shoot_1.png','..\shooter_shoot_2.png' ]
        self.speed = 1
        self.bullet_speed = 1
        self.bullet_cooldown = 100
        self.movement_cooldown = 40
        
        self.shooter = image.load(self.idle_sprites[0]) # Loads into the actual sprite as an image
        self.shooterCollider = self.shooter.get_rect() # Creates a rectangle collider for the image, which will be perfect for handling 
        pass
    
    def movement(self):
        '''
        For the shooter, we want the enemy to move side to side, just changing the x position
        This function will also check the level bounds to make sure the enemy doesn't go off screen
        This function should not be called again until it has completed its path, this next path will be made when movement_cooldown is 0
        
        This will update the Shooter.pos using the Shooter.speed
        
        '''
        pass
    def shootBullet(self, target_pos):
        '''When called, this will shoot a bullet instance towards the player's position when self.bullet_cooldown is 0
        
        Args : target_pos, the x , y coordinates of the player's position  
        
        Returns : Returns nothing as it is creating a new instance of the class enemyBullet
        
        '''
        
    def update(self):
        ''' This will hold all of the Shooter's functions and be the logic the Shooter will follow
        
        For example, the Shooter will stop in their tracks to shoot three bullets at once.
        Once done, it moves again. 
        All cooldown variables should be used here
        
        If the enemy collides with a player bullet, it calls destroy()
        
        '''
    
    def destroy(self):
        ''' Occurs when the enemy is hit by the player's bullets.
        This destroys the enemy instance and plays an explosion sprite over the gone enemy 
        
        '''
        pass
    
class Chaser:
    ''' This creates an instance of the Chaser enemy
    
    '''
    def __init__(self):
        '''
        This will initilize the Chaser Enemy and store information
        such as:
            Sprites needed for all animations ( each animation will have a list of their appropiate images)
            Position Values needed to determine where they are in the screen
            Time value to determine how long to attack again ( cooldown)
            Values such as movement speed 
        '''
        self.pos = [0 , 0] # Keeps track of the enemy's position on screen
        self.idle_sprites = ['..\chaser_idle.png'] # Will keep a string of the file path for the idle sprites ( could be an array to easily loop if the idle animation is more than 1 frame)
        self.shoot_sprites = ['..\shooter_shoot_1.png','..\shooter_shoot_2.png' ]
        self.speed = 2
        
        self.chaser = image.load(self.idle_sprites[0]) # Loads into the actual sprite as an image
        self.chaserCollider = self.chaser.get_rect() # Creates a rectangle collider for the image, which will be perfect for handling 
        pass
    def createPath(self, target_pos):
        ''' Creates an array of position values for the enemy to follow 
        The target_pos is the Player's position
        
        Returns an array of x,y coordinates
        '''
        pass
    
    def movement(self):
        '''
        For the chaser, we want the enemy to swoop to attack the player. ( This path will be created using createPath())
        This function will loop over the path made from createPath
        Each element in the createPath array should be visited

        Within the loop, we will update the self.pos using the self.speed
        
        '''
        pass
        
    def update(self):
        ''' This will hold all of the Chaser's functions and be the logic the Chaser will follow
        
        For example, the Chaser will stay still for 
        Once done, it moves again. 
        
        If the enemy collides with a player bullet, it calls destroy()
        
        '''
    
    def destroy(self):
        ''' Occurs when the enemy is hit by the player's bullets.
        This destroys the enemy instance and plays an explosion sprite over the gone enemy 
        
        '''
        pass
    
class enemyBullet:
    def __init__(self, sprite, initial_pos, target_pos):
        ''' Creates a Bullet instance using the following parameters
        Args: 
            sprite: A string value holding the directory path for the image
            initial_pos: An array of integer values that will be taken from Shooter's position
            target_pos: An array of integer values that will be ideally the position of the player ( the value is static )
            
        '''
        self.sprite = image.load(sprite) # Given a string, the bullet will load as the sprite image
        self.speed = 1 # An Integer value used to dictate how fast the bullet should move
        self.pos = [initial_pos[0], initial_pos[1]] 
        self.target_pos = [ target_pos[0],target_pos[1]]
        
        pass
    def update(self):
        ''' This will update the bullet's position as it heads towards the self.target_pos
        
        '''
        pass
    def destroy(self):
        '''The bullet will destroy itself if it hits the player or the edge of the screen.'''
        pass