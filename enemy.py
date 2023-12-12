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
    def __init__(self, x,y , bulletManager):
        '''
        This will initilize the Shooter Enemy and store information
        such as:
            Sprites needed for all animations ( each animation will have a list of their appropiate images)
            Position Values needed to determine where they are in the screen
            Time value to determine how long to shoot their next bullets ( cooldown)
            Values such as movement speed 
        '''
        self.pos = Vector2(x,y)# Keeps track of the enemy's position on screen
        self.destination_pos = Vector2(x,y) # The destination x,y coordinates where the enemy wants to go
        self.direction_x = 1
        
        self.animationIndex = 0
        self.idle_sprites = [image.load('Sprites\shooter_idle1.png'), 
                             image.load('Sprites\shooter_idle2.png') , 
                             image.load('Sprites\shooter_idle3.png')] # Will keep a string of the file path for the idle sprites ( could be an array to easily loop if the idle animation is more than 1 frame)
        self.idle_sprites = [transform.scale(image,(image.get_width()*2, image.get_height()*2)) for image in self.idle_sprites ]
        
        self.shoot_sprites = ['..\shooter_shoot_1.png','..\shooter_shoot_2.png' ]
        
        # Shooter Stats
        self.health  = 3
        self.speed = 1
        self.bullet_speed = 1
        self.bullet_cooldown = 150
        self.movement_cooldown = 40
        
        self.bulletManager = bulletManager
                
        self.entity = self.idle_sprites[0] # Loads into the actual sprite as an image
        self.entity_collider = self.entity.get_rect() # Creates a rectangle collider for the image, which will be perfect for handling collisions
        pass
    
    def animationLoop(self):
        if (self.animationIndex // 6) > len(self.idle_sprites) - 1:
            self.animationIndex = 0
        self.animationIndex+=1
        self.entity = self.idle_sprites[self.animationIndex // 6 % len(self.idle_sprites)]
        pass
    
    def takeDamage(self, damage):
        # Depending on player bullet strength, the enemy takes the appropiate damage
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False
    
    def createNewDestination(self):
        self.movement_cooldown  = 50
        self.destination_pos.x += (30 * self.direction_x)
        self.direction_x*= -1
        
        pass
    
    def movement(self):
        '''
        For the shooter, we want the enemy to move side to side, just changing the x position
        This function will also check the level bounds to make sure the enemy doesn't go off screen
        This function should not be called again until it has completed its path, this next path will be made when movement_cooldown is 0
        
        This will update the Shooter.pos using the Shooter.speed
        
        '''
        direction = Vector2.normalize(self.destination_pos - self.pos)
        distance = (self.destination_pos - self.pos).length()
        if distance > 0:
            direction.normalize_ip()
            
            movement = direction * self.speed
            self.pos += movement

            if distance < self.speed:
                self.entity_collider.center = [self.destination_pos.x , self.destination_pos.y]
        pass
    def shootBullet(self, target_pos):
        '''When called, this will shoot a bullet instance towards the player's position when self.bullet_cooldown is 0
        
        Args : target_pos, the x , y coordinates of the player's position  
        
        Returns : Returns nothing as it is creating a new instance of the class EnemyBullet
        Ideally, we would add this to a bullet array that is updated in the game framework (so when the enemy dies, the bullet doesn't disappear)
        
        '''
        self.bullet_cooldown = 150 + randint(-50 , 50)
        self.bulletManager.add_enemy_bullet(EnemyBullet(self.pos, target_pos))
    
    
    def update(self , target_pos):
        ''' This will hold all of the Shooter's functions and be the logic the Shooter will follow
        
        For example, the Shooter will stop in their tracks to shoot three bullets at once.
        Once done, it moves again. 
        All cooldown variables should be used here
        
        If the enemy collides with a player bullet, it calls destroy()
        
        '''
        self.animationLoop()
        if self.bullet_cooldown >0 or self.movement_cooldown >0 :
            self.bullet_cooldown -= 1
            self.movement_cooldown -= 1
            
        if self.bullet_cooldown == 0:
            self.shootBullet(target_pos)    
          
        if self.movement_cooldown == 0 :
            self.createNewDestination()
        if 0 > self.entity_collider.left:
            self.pos.x = 0
        elif SCREEN_WIDTH < self.entity_collider.right:
            self.pos.x = SCREEN_WIDTH - self.entity_collider.width
        if self.pos.x != self.destination_pos.x:
            self.movement()
        pass
            
        self.entity_collider = self.entity.get_rect(center = (round(self.pos.x), round(self.pos.y)))
        # Replace this with the pygame.display from the main gameloop!    
        # display.set_mode(10).blit(self.entity , self.entity_collider) 
    
    def __del__(self):
        print('Shooter Destroyed!')
    
class Chaser:
    ''' This creates an instance of the Chaser enemy
    
    '''
    def __init__(self , x , y , bulletManager , player):
        '''
        This will initilize the Chaser Enemy and store information
        such as:
            Sprites needed for all animations ( each animation will have a list of their appropiate images)
            Position Values needed to determine where they are in the screen
            Time value to determine how long to attack again ( cooldown)
            Values such as movement speed 
        '''
        self.pos = Vector2(x,y) # Keeps track of the enemy's position on screen
        self.return_pos = Vector2(x,y)
        self.destination_pos = Vector2(x,y)
        self.destination_index = 0
        self.path_arr = [] # Used to keep the pathfinding values for the enemy (holds vectors)
        
        
        self.animationIndex = 0
        self.idle_sprites = [image.load('Sprites\chaser_idle1.png'), 
                             image.load('Sprites\chaser_idle2.png') , 
                             image.load('Sprites\chaser_idle3.png'),
                             image.load('Sprites\chaser_idle4.png') ,
                             image.load('Sprites\chaser_idle5.png') ,
                             image.load('Sprites\chaser_idle6.png') ,
                             image.load('Sprites\chaser_idle7.png') ,
                             image.load('Sprites\chaser_idle8.png')] # Will keep a string of the file path for the idle sprites ( could be an array to easily loop if the idle animation is more than 1 frame)
        self.idle_sprites = [transform.scale(image,(image.get_width()*2, image.get_height()*2)) for image in self.idle_sprites ]

        self.shoot_sprites = ['Sprites\chaser_shoot_1.png','Sprites\chaser_shoot_2.png' ]
        
        # Chaser Stats
        self.health = 2
        self.speed = 3
        self.movement_cooldown = 150
        self.bullet_cooldown = 15
        
        self.original_image = self.idle_sprites[0]
        self.entity = (self.idle_sprites[0]) # Loads into the actual sprite as an image
        self.entity_collider = self.entity.get_rect() # Creates a rectangle collider for the image, which will be perfect for handling collisions
        
        self.playerInstance = player
        self.bulletManager = bulletManager
        
    def animationLoop(self):
        if (self.animationIndex // 4) > len(self.idle_sprites) - 1:
            self.animationIndex = 0
        self.animationIndex+=1
        
        self.entity = self.idle_sprites[self.animationIndex // 4 % len(self.idle_sprites)]
        self.original_image = self.entity
        pass
    
    def takeDamage(self, damage):
        # Depending on player bullet strength, the enemy takes the appropiate damage
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False
    
    def createPath(self, target_pos):
        ''' Creates an array of position values for the enemy to follow 
        The target_pos is the Player's position
        
        Returns an array of x,y coordinates
        
        Visualize Path
            Once Chaser begins to attack,
                We create a path array in the shape of a capsule
                         *        *
                    *                   *
                *                           *
                (topLeft) - - - V - - - (topRight)
                |                           |
                |                           |
                |                           |
                |                           |   
                (bottomLeft) - - - ^ - - - (bottomRight)
                *                           *
                       *             *
                            *     *
                
                We do this by creating a hypotenuse between the player and target.
                We calculate the rectangle area by using sin , cos 
                The radius for the semicircle will be the length between tl_b and tr_b
                ( this will be static and not update if the player moves after the chaser goes on the chase)
        
        '''
        self.destination_index = 0
        self.movement_cooldown = 5500000
        self.path_arr = []
        self.finished_path = False
        '''
        If the Chaser's x pos is less than (on the left of) the player's , Chaser is on the top left and player is bottomr right
        Else, chaser is on top right and player is bottom left
        
        '''
        
        if(target_pos.x > self.pos.x):
            topLeft = self.pos
            bottomRight = target_pos
            topRight = Vector2(self.pos.x + abs(target_pos.x - self.pos.x))
            bottomLeft = Vector2(self.pos.x,target_pos.y)
            
            # Points on upper semi-circle (when chaser is topLeft)
            theta = 360
            radius = abs(topLeft.x - topRight.x) //2
            origin = Vector2(topLeft.x - radius, topLeft.y)
            while theta > 180:
                theta -=30 
                pos_to_add = Vector2(radius * cos(radians(theta)) + origin.x , radius * sin(radians(theta)) + origin.y)
                self.path_arr.append(pos_to_add)
                
            self.path_arr.append(bottomRight)    
            
            # Points on bottom semi-circle (when chaser is topLeft)
            theta = 0
            radius = abs(bottomLeft.x - bottomRight.x) //2
            origin = Vector2(bottomRight.x - radius, bottomRight.y)
            while theta < 180:
                theta +=30 
                pos_to_add = Vector2(radius * cos(radians(theta)) + origin.x , radius * sin(radians(theta)) + origin.y)
                self.path_arr.append(pos_to_add)
            
            self.path_arr.append(self.return_pos)
            
        else:
            topRight = self.pos
            bottomLeft = target_pos
            topLeft = Vector2(self.pos.x - abs(target_pos.x - self.pos.x) , self.pos.y)
            bottomRight = Vector2(self.pos.x,target_pos.y)
            
            # Points on upper semi-circle (when chaser is topRight)
            theta = 180
            radius = abs(topLeft.x - topRight.x) //2
            origin = Vector2(radius + topRight.x , topRight.y)
            while theta < 360:
                theta +=30 
                pos_to_add = Vector2(radius * cos(radians(theta)) + origin.x , radius * sin(radians(theta)) + origin.y)
                self.path_arr.append(pos_to_add)
                
            self.path_arr.append(bottomLeft)    
            
            # Points on bottom semi-circle (when chaser is topRight)
            theta = 180
            radius = abs(bottomLeft.x - bottomRight.x) //2
            origin = Vector2(radius + bottomLeft.x , bottomLeft.y)
            while theta > 0:
                theta -=30 
                pos_to_add = Vector2(radius * cos(radians(theta)) + origin.x , radius * sin(radians(theta)) + origin.y)
                self.path_arr.append(pos_to_add)            
            self.path_arr.append(self.return_pos)
            
    def shootBullet(self):
        print("Dir : ", self.direction)
                
        rotateVector1 = self.direction.rotate(15)
        rotateVector2 = self.direction.rotate(-15)
        self.entity_collider = self.entity.get_rect(center = (round(self.pos.x), round(self.pos.y)))
        rotateVector1.normalize_ip()
        rotateVector2.normalize_ip()
        print(rotateVector1)
        print(Vector2(self.entity_collider.center))
        newBullet1 = EnemyBullet(Vector2(self.entity_collider.center) , Vector2(self.entity_collider.center) + rotateVector1)
        newBullet2 = EnemyBullet(Vector2(self.entity_collider.center) , Vector2(self.entity_collider.center) + rotateVector2)
        
        self.bullet_cooldown = 75
        self.bulletManager.add_enemy_bullet(newBullet1) 
        self.bulletManager.add_enemy_bullet(newBullet2)
    def movement(self):
        '''
        For the chaser, we want the enemy to swoop to attack the player. ( This path will be created using createPath())
        This function will loop over the path made from createPath
        Each element in the createPath array should be visited

        Within the loop, we will update the self.pos using the self.speed
        
        '''
        self.destination_pos = self.path_arr[self.destination_index]
        self.direction = (self.destination_pos - self.pos)
        distance = (self.destination_pos - self.pos).length()
        if distance > 0:
            
            # Rotates sprite on the unit vector to its next
            self.direction.normalize_ip()
        
            angle = degrees(atan2(-self.direction.y, self.direction.x))
            self.entity = transform.rotate(self.original_image, angle + 90 )

            self.entity_collider.center = [self.pos.x- self.entity_collider.x , self.pos.y- self.entity_collider.y]
            self.entity_collider = self.entity.get_rect( center=self.entity_collider.center)
    
            movement = self.direction * self.speed
            self.pos += movement
            
            
            if distance < self.speed or distance < 0.1:
                self.entity_collider = self.entity.get_rect(center = (round(self.pos.x), round(self.pos.y)))
                            
                self.destination_index +=1
                if self.destination_index == len(self.path_arr):
                    self.finished_path = True
                    self.destination_index = 0
                    self.movement_cooldown = 350
                    print("FINISHED PATH!")
                    self.direction = Vector2(0,1)
                    self.entity = transform.rotate(self.original_image, 0)
                    self.entity_collider.center = [self.return_pos.x , self.return_pos.y]

        
    def update(self , target_pos):
        ''' This will hold all of the Chaser's functions and be the logic the Chaser will follow
        
        For example, the Chaser will stay still for 
        Once done, it moves again. 
        
        If the enemy collides with a player bullet, it calls destroy()
        
        '''
        self.animationLoop()
        self.bullet_cooldown -=1
        
        if self.entity_collider.colliderect(self.playerInstance.entity_collider):
            self.playerInstance.takeDamage()
        
        if self.movement_cooldown >0:
            self.movement_cooldown -=1
        
        if(self.movement_cooldown == 0):
            self.createPath(target_pos)
        
        if self.path_arr !=[] and not self.finished_path:
            self.movement()
    
        if self.destination_index == 6 and self.bullet_cooldown <= 0:
            self.shootBullet()

        self.entity_collider = self.entity.get_rect(center = (round(self.pos.x), round(self.pos.y)))

    def destroy(self):
        ''' Occurs when the enemy is hit by the player's bullets.
        This destroys the enemy instance and plays an explosion sprite over the gone enemy 
        
        '''
        pass

class Bomber:
    ''' This creates an instance of the Bomber enemy
    
    '''
    def __init__(self, x, y, bulletManager):
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
        
        # Bomber Stats
        self.health  = 5
        self.speed = 0 
        self.bullet_speed = 1
        self.bullet_cooldown = 200
        
        self.bulletManager = bulletManager
        
        self.animationIndex = 0
        self.idle_sprites = [image.load(r'Sprites\bomber_idle1.png'), 
                             image.load(r'Sprites\bomber_idle2.png') , 
                             image.load(r'Sprites\bomber_idle3.png'),
                             image.load(r'Sprites\bomber_idle4.png')] # Will keep a string of the file path for the idle sprites ( could be an array to easily loop if the idle animation is more than 1 frame)
        self.idle_sprites = [transform.scale(image,(image.get_width()*2, image.get_height()*2)) for image in self.idle_sprites ]
        
        self.entity = (self.idle_sprites[0]) # Loads into the actual sprite as an image
        self.entity = transform.scale(self.entity,(self.entity.get_width()*2,self.entity.get_height()*2)) 
        self.entity_collider = self.entity.get_rect() # Creates a rectangle collider for the image, which will be perfect for handling collisions
        pass
    def animationLoop(self):
        if (self.animationIndex // 12) > len(self.idle_sprites) - 1:
            self.animationIndex = 0
        self.animationIndex+=1
        self.entity = self.idle_sprites[self.animationIndex // 12 % len(self.idle_sprites)]
        pass
    
    def takeDamage(self, damage):
        # Depending on player bullet strength, the enemy takes the appropiate damage
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False
        
    def shootBomb(self, target_pos):
        '''When called, this will shoot a bomb instance towards the player's position
        
        Args : target_pos, the x , y coordinates of the player's position  
        
        Returns : Returns nothing as it is creating a new instance of the class EnemyBomb
        
        '''
        self.bullet_cooldown = 200 + randint(-25 , 100)
        self.bulletManager.add_enemy_bomb(EnemyBomb( self.pos , target_pos))
    def update(self , target_pos):
        ''' This will hold all of the Bomber's functions and be the logic the Shooter will follow
        
        If the enemy collides with a player bullet, it calls destroy()
        
        '''
        
        self.animationLoop()
        if self.bullet_cooldown >0:
            self.bullet_cooldown -= 1
        
        if self.bullet_cooldown == 0:
            self.shootBomb(target_pos)    
            
        self.entity_collider = self.entity.get_rect(center = (round(self.pos.x), round(self.pos.y)))
        # Replace this with the pygame.display from the main gameloop!        
    def __del__(self):
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
        self.bullet_collider =self.bullet.get_rect(center = (round(self.pos.x), round(self.pos.y)))
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
        self.sprites = [image.load(r'Sprites\bomb1.png'), 
                        image.load(r'Sprites\bomb2.png'), 
                        image.load(r'Sprites\bomb3.png'),
                        image.load(r'Sprites\bomb4.png')] # Given a string, the bomb will load as the sprite image
        self.sprites = [transform.scale(image,(image.get_width()*2, image.get_height()*2)) for image in self.sprites ]
        self.speed = 2 # An Integer value used to dictate how fast the bomb should move
        self.pos = Vector2(initial_pos)
        self.target_pos = Vector2(target_pos) # Drops down to player's Y positiom
        # Math to figure out what direction the bullet should go
        
        self.animationIndex = 0
        self.bomb = self.sprites[0]
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
        if distance > 0:
            direction.normalize_ip()
            
            movement = direction * self.speed
            self.pos += movement
            self.bomb_collider = self.bomb.get_rect(center = (round(self.pos.x), round(self.pos.y)))

            if distance < self.speed:
                self.bomb_collider.center = [self.target_pos.x , self.target_pos.y]
                self.animateExplode()
                
        # Use level bounds to call explode()
        pass
    
    def animateExplode(self):
        if (self.animationIndex // 4) <= len(self.sprites) - 1:
            self.animationIndex+=1
            self.bomb = self.sprites[self.animationIndex // 4 % len(self.sprites)]
        else: 
            self.ready_to_explode = True
        
    def out_of_bounds(self):
        '''
        Define bounds for the bullet. If bullet goes beyond the parameters, it returns false
        '''
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