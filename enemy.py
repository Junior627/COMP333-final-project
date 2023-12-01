'''This is the skeleton code for the enemy-related code

This file will contain all enemy class instances

Since there are three distinct versions of the common enemy

Shooter: Keeps their distance from the player and tries to shoot from afar

Chaser: Tries to crash into the player any moment after a few seconds spawning

Bomber: Similiar to Shooter, they send a different type of projectile and is stagnant


'''
from pygame import *
from constants import *
from math import *
from random import *
class Shooter:
    ''' This creates an instance of the Shooter enemy
    '''
    def __init__(self, x,y ):
        '''
        This will initilize the Shooter Enemy and store information
        such as:
            Sprites needed for all animations ( each animation will have a list of their appropiate images)
            Position Values needed to determine where they are in the screen
            Time value to determine how long to shoot their next bullets ( cooldown)
            Values such as movement speed 
        '''
        self.pos = Vector2(x,y)# Keeps track of the enemy's position on screen
        self.destination_pos = [x + 0,y] # The destination x,y coordinates where the enemy wants to go
        
        self.idle_sprites = ['Sprites\shooter_idle.png'] # Will keep a string of the file path for the idle sprites ( could be an array to easily loop if the idle animation is more than 1 frame)
        self.shoot_sprites = ['..\shooter_shoot_1.png','..\shooter_shoot_2.png' ]
        self.speed = 1
        self.bullet_speed = 1
        self.bullet_cooldown = 150
        self.movement_cooldown = 40
                
        self.entity = image.load(self.idle_sprites[0]) # Loads into the actual sprite as an image
        self.entity_collider = self.entity.get_rect() # Creates a rectangle collider for the image, which will be perfect for handling collisions
        pass
    
    def movement(self):
        '''
        For the shooter, we want the enemy to move side to side, just changing the x position
        This function will also check the level bounds to make sure the enemy doesn't go off screen
        This function should not be called again until it has completed its path, this next path will be made when movement_cooldown is 0
        
        This will update the Shooter.pos using the Shooter.speed
        
        '''
        self.movement_cooldown  = 350 + randint(-25 , 150)
        pass
    def shootBullet(self, target_pos):
        '''When called, this will shoot a bullet instance towards the player's position when self.bullet_cooldown is 0
        
        Args : target_pos, the x , y coordinates of the player's position  
        
        Returns : Returns nothing as it is creating a new instance of the class EnemyBullet
        Ideally, we would add this to a bullet array that is updated in the game framework (so when the enemy dies, the bullet doesn't disappear)
        
        '''
        self.bullet_cooldown = 150 + randint(-50 , 50)
        return EnemyBullet(Vector2(self.pos.x + (self.entity_collider.width / 2),self.pos.y+ self.entity_collider.height/2), target_pos)
        
    def update(self):
        ''' This will hold all of the Shooter's functions and be the logic the Shooter will follow
        
        For example, the Shooter will stop in their tracks to shoot three bullets at once.
        Once done, it moves again. 
        All cooldown variables should be used here
        
        If the enemy collides with a player bullet, it calls destroy()
        
        '''
        
        if self.bullet_cooldown >0 or self.movement_cooldown >0 :
            self.bullet_cooldown -= 1
            self.movement_cooldown -= 1
            

        if self.movement_cooldown == 0 :
            self.movement()
        pass
            
        self.entity_collider = self.entity_collider.move(self.pos.x - self.entity_collider.x, self.pos.y - self.entity_collider.y)    
        # Replace this with the pygame.display from the main gameloop!    
        # display.set_mode(10).blit(self.entity , self.entity_collider) 
    def destroy(self):
        ''' Occurs when the enemy is hit by the player's bullets.
        This destroys the enemy instance and plays an explosion sprite over the gone enemy 
        
        '''
        
         
        pass
    
    def __del__(self):
        print('Shooter Destroyed!')
    
class Chaser:
    ''' This creates an instance of the Chaser enemy
    
    '''
    def __init__(self , x , y):
        '''
        This will initilize the Chaser Enemy and store information
        such as:
            Sprites needed for all animations ( each animation will have a list of their appropiate images)
            Position Values needed to determine where they are in the screen
            Time value to determine how long to attack again ( cooldown)
            Values such as movement speed 
        '''
        self.pos = [x , y] # Keeps track of the enemy's position on screen
        self.original_pos [self.pos[0], self.pos[1]]
        self.path_arr = [] # Used to keep the pathfinding values for the enemy
        
        self.idle_sprites = ['..\chaser_idle.png'] # Will keep a string of the file path for the idle sprites ( could be an array to easily loop if the idle animation is more than 1 frame)
        self.shoot_sprites = ['..\shooter_shoot_1.png','..\shooter_shoot_2.png' ]
        self.speed = 2
        self.movement_cooldown = 50
        
        self.entity = image.load(self.idle_sprites[0]) # Loads into the actual sprite as an image
        self.entity_collider = self.entity.get_rect() # Creates a rectangle collider for the image, which will be perfect for handling collisions
        pass
    def createPath(self, target_pos):
        ''' Creates an array of position values for the enemy to follow 
        The target_pos is the Player's position
        
        Returns an array of x,y coordinates
        
        Visualize Path
            Once Chaser begins to attack,
                They will make a curve upwards ( this should be fixed)
                    *
                *       *
                - - - - V - - - -
                |               |
                |               |
                |               |
                |               |
                - - - - ^ - - - -
                
                Once they finish this curve, they will charge at the player's position 
                ( this will be static and not update if the player moves after the chaser goes on the chase)
        '''
        
        
        pass
    
    def movement(self, target_pos):
        '''
        For the chaser, we want the enemy to swoop to attack the player. ( This path will be created using createPath())
        This function will loop over the path made from createPath
        Each element in the createPath array should be visited

        Within the loop, we will update the self.pos using the self.speed
        
        '''
        
        [(target_pos[0]-self.pos[0] ) / (max(self.pos) - min(self.pos)) , ((target_pos[1]-self.pos[1] ) / (max(self.pos) - min(self.pos)))] 
        
        
        pass
        
    def update(self):
        ''' This will hold all of the Chaser's functions and be the logic the Chaser will follow
        
        For example, the Chaser will stay still for 
        Once done, it moves again. 
        
        If the enemy collides with a player bullet, it calls destroy()
        
        '''
        
        if self.movement_cooldown >0:
            self.movement_cooldown -=1
            
        if self.movement_cooldown == 0:
            self.createPath()
            
        
        # Replace this with the pygame.display from the main gameloop!    
        display.set_mode(10).blit(self.entity , self.entity_collider) 
        pass
    
    def destroy(self):
        ''' Occurs when the enemy is hit by the player's bullets.
        This destroys the enemy instance and plays an explosion sprite over the gone enemy 
        
        '''
        pass

class Bomber:
    ''' This creates an instance of the Bomber enemy
    
    '''
    def __init__(self, x, y):
        '''
        This will initilize the Bomber Enemy and store information
        such as:
            Sprites needed for all animations ( each animation will have a list of their appropiate images)
            Position Values needed to determine where they are in the screen
            Time value to determine how long to shoot their next bullets ( cooldown)
            Values such as movement speed 
        '''
        self.pos = Vector2(x,y)# Keeps track of the enemy's position on screen
        self.idle_sprites = [r"Sprites\bomber_idle.png"] # Will keep a string of the file path for the idle sprites ( could be an array to easily loop if the idle animation is more than 1 frame)
        self.shoot_sprites = [r'Sprites\bomber_shoot_1.png',r'Sprites\bomber_shoot_2.png' ]
        self.speed = 0 
        self.bullet_speed = 1
        self.bullet_cooldown = 200
        
        self.entity = image.load(self.idle_sprites[0]) # Loads into the actual sprite as an image
        self.entity_collider = self.entity.get_rect() # Creates a rectangle collider for the image, which will be perfect for handling collisions
        pass
     
    def shootBomb(self, target_pos):
        '''When called, this will shoot a bomb instance towards the player's position
        
        Args : target_pos, the x , y coordinates of the player's position  
        
        Returns : Returns nothing as it is creating a new instance of the class EnemyBomb
        
        '''
        self.bullet_cooldown = 200 + randint(-25 , 100)
        og_pos = Vector2(self.pos.x + (self.entity_collider.width / 2),self.pos.y+ self.entity_collider.height/2)
        return EnemyBomb( og_pos , target_pos)
    def update(self):
        ''' This will hold all of the Bomber's functions and be the logic the Shooter will follow
        
        If the enemy collides with a player bullet, it calls destroy()
        
        '''
        if self.bullet_cooldown >0:
            self.bullet_cooldown -= 1
        
        self.entity_collider = self.entity_collider.move(self.pos.x - self.entity_collider.x, self.pos.y - self.entity_collider.y)    
        # Replace this with the pygame.display from the main gameloop!        
    def destroy(self):
        ''' Occurs when the enemy is hit by the player's bullets.
        This destroys the enemy instance and plays an explosion sprite over the gone enemy 
        
        When called, we spawn bullets around the enemy in this formation:
        
        *  *  *
        *  □  *
        *  *  *
        
        The bullet's target_pos would be 
        
        [self.pos[0] - 1 , self.pos[1] - 1]  [self.pos[0], self.pos[1] - 1]  [self.pos[0] + 1 , self.pos[1] - 1]
        [self.pos[0] - 1 , self.pos[1]]                                      [self.pos[0] + 1 , self.pos[1]]
        [self.pos[0] - 1 , self.pos[1] + 1]  [self.pos[0], self.pos[1] + 1]  [self.pos[0] + 1 , self.pos[1] + 1]
        
        After this logic is done, we finally destroy this Bomber instance
        '''
        
        
        self.kill()
        pass
    
class EnemyBullet:
    def __init__(self, initial_pos, target_pos):
        ''' Creates a Bullet instance using the following parameters
        Args: 
            sprite: A string value holding the directory path for the image
            initial_pos: An array of integer values that will be taken from Shooter's position
            target_pos: An array of integer values that will be ideally the position of the player ( the value is static )
            
        '''
        self.sprite = 'Sprites\enemy_bullet.png' # Given a string, the bullet will load as the sprite image
        self.speed = 3 # An Integer value used to dictate how fast the bullet should move
        # Math to figure out what direction the bullet should go
        self.pos = Vector2()
        self.pos.x = initial_pos[0] + randint(-10,10)
        self.pos.y = initial_pos[1]
        
        self.bullet = image.load(self.sprite)
        
        self.bullet_dir = Vector2()
        self.bullet_dir.x = (target_pos[0]-initial_pos[0] ) / sqrt(initial_pos[0]*initial_pos[0] + initial_pos[1]*initial_pos[1]) 
        self.bullet_dir.y = (target_pos[1]-initial_pos[1] ) / sqrt(initial_pos[0]*initial_pos[0] + initial_pos[1]*initial_pos[1])
        self.bullet_dir = Vector2.normalize(self.bullet_dir)
        self.bullet_collider = self.bullet.get_rect()
        pass
    def update(self):
        ''' This will update the bullet's position as it heads towards the self.target_pos 
        by multiplying self.bullet_dir and self.speed and adding it to self.pos
        
        '''
        self.pos = Vector2(self.pos.x + (self.bullet_dir.x * self.speed) , self.pos.y + (self.bullet_dir.y * self.speed))
        self.bullet_collider = self.bullet_collider.move(self.pos.x - self.bullet_collider.x, self.pos.y- self.bullet_collider.y )
    def out_of_bounds(self):
        return self.pos[0] < 0 or self.pos[0] > SCREEN_WIDTH or self.pos[1] <0 or self.pos[1] > SCREEN_HEIGHT
    
    def destroy(self):
        '''The bullet will destroy itself if it hits the player or the edge of the screen.'''
        pass
    
class EnemyBomb:
    def __init__(self, initial_pos ,target_pos):
        ''' Creates an EnemyBomb instance using the following parameters
        Args: 
            sprite: A string value holding the directory path for the image
            initial_pos: An array of integer values that will be taken from Bomber's position
            target_pos: An array of integer values that will be ideally the position of the player ( the value is static )
            
        '''
        self.sprite = r'Sprites\bomb.png' # Given a string, the bomb will load as the sprite image
        self.speed = 3 # An Integer value used to dictate how fast the bomb should move
        self.pos = Vector2(initial_pos)
        self.target_pos = Vector2(target_pos) # Drops down to player's Y positiom
        # Math to figure out what direction the bullet should go
        
        self.bomb = image.load(self.sprite)
        self.bomb_collider = self.bomb.get_rect()
        self.ready_to_explode = False
        pass
    
    def update(self):
        ''' This will update the bomb's position as it heads towards the self.target_pos 
        by multiplying self.bomb_dir and self.speed and adding it to self.pos
        
        Once the enemy has reached their destination or touched the border, we call self.explode()
        '''
        
        direction = Vector2.normalize(self.target_pos - self.pos)
        distance = (self.target_pos - self.pos).length()
        print(distance)
        if distance > 0:
            direction.normalize_ip()
            
            movement = direction * self.speed
            self.pos += movement
            self.bomb_collider = self.bomb_collider.move(self.pos)

            if distance < self.speed:
                self.bomb_collider.center = [self.target_pos.x , self.target_pos.y]
                self.ready_to_explode = True
                print("Destination Reached!")
                
        # Use level bounds to call explode()
        pass
    
    
    def out_of_bounds(self):
        return self.pos[0] < 0 or self.pos[0] > SCREEN_WIDTH or self.pos[1] <0 or self.pos[1] > SCREEN_HEIGHT
    def explode(self):
        '''
        When called, we spawn bullets around the enemy in this formation:
        
        *     *
           □  
        *     *
        
        The bullet's target_pos would be 
        [self.pos[0] - 1 , self.pos[1] - 1]     [self.pos[0] + 1 , self.pos[1] - 1]
                                             □
        [self.pos[0] - 1 , self.pos[1] + 1]     [self.pos[0] + 1 , self.pos[1] + 1]
        
        After this logic is done, we finally destroy this EnemyBomb instance
        '''
        spawnedBullet_0 = EnemyBullet(self.pos , Vector2(self.pos.x-1 , self.pos.y -1))
        spawnedBullet_1 = EnemyBullet(self.pos , Vector2(self.pos.x+1 , self.pos.y -1))
        spawnedBullet_2 = EnemyBullet(self.pos , Vector2(self.pos.x-1 , self.pos.y +1))
        spawnedBullet_3 = EnemyBullet(self.pos , Vector2(self.pos.x+1 , self.pos.y +1))
        
        
        return spawnedBullet_0 , spawnedBullet_1 , spawnedBullet_2 , spawnedBullet_3
        
    
def unit_tests():
    
    ''' Unit tests for enemy.py would include:
    
    When an enemy is created, we check to see if the enemy is on screen / in the enemy array
        If so, we passed
        Else, the enemy hasn't spawned and we don't things to shoot :/
        
    We can check if the bullets/ bombs are spawned and are on screen
        If so, we passed
    
    We can also do unit tests to check if the files being called by the classes exist.
        We run a test at the beginning to check if all files can be called / exist

    '''
    
    pass