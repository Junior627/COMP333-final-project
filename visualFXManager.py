from pygame import *

'''Code used to manage visual effects within the game.
Specific attributes:
explosion_list- a list of all current explosions.
bullet_explosion_list- a list of all current bullet explosions.
'''

class visualFXManager:
    def __init__(self):
        self.explosion_list = []
        self.bullet_explosion_list = []
        
    def update_lists(self):
        '''Updates the list of explosions.
        '''
        self.update_fx_list(self.explosion_list)
        
    def update_fx_list(self, list):
        '''Updates a given list of visual effects.
        Args: fx_list- a list of visual effects to update.
        '''
        for fx in list:
            fx.draw()
            if fx.endOfAnim():
                list.remove(fx)
                
    def add_explosion_fx(self, x , y, fx_arg):
        '''Adds an explosion effect to the list of explosion effects.
        Args: x- the x coordinate of the explosion.
        y- the y coordinate of the explosion.
        fx_arg- the type of explosion effect to add.
        '''
        self.explosion_list.append(fx_arg(x,y))
    

'''An instance of a ship explosion visual effect.
Specific attributes:
pos- the position of the explosion.
anim_index- the index of the current sprite corresponding to the
current frame of the explosion.
explode- a list containing all sprites of the explosion.
rect- the dimensions of the explosion effect.
anim_counter- the current frame of the explosion.
'''
    
class Explosion:
    def __init__(self, x,y):
        self.pos = Vector2(x , y)
        self.anim_index = 0
        self.explode = [
            image.load("Sprites\explosion1.png"),
            image.load("Sprites\explosion2.png"),
            image.load("Sprites\explosion3.png"),
            image.load("Sprites\explosion4.png"),
            image.load("Sprites\explosion5.png")
            ]
        self.explode = [transform.scale(image,(image.get_width()*4,image.get_height()*4)) for image in self.explode]
        self.rect = Rect(x,y,self.explode[0].get_width() , self.explode[0].get_height())
        self.anim_counter = 0
        
    def endOfAnim(self):
        '''Checks if the animation has finished.
        Returns: true if the animation has finished, false otherwise
        '''
        if self.anim_index >= len(self.explode):
            return True
        return False
    def draw(self):
        '''Updates the required attributes to advance the explosion to its next frame.
        '''
        self.rect.center = (self.pos.x , self.pos.y) 
        self.anim_counter +=1       
        self.anim_index = (self.anim_counter + 1) // 3
    
    def __del__(self):
        pass


'''An instance of a vullet explosion visual effect.
Specific attributes:
pos- the position of the explosion.
anim_index- the index of the current sprite corresponding to the
current frame of the explosion.
explode- a list containing all sprites of the explosion.
rect- the dimensions of the explosion effect.
anim_counter- the current frame of the explosion.
'''

class BulletExplosion:
    def __init__(self, x ,y):
        self.pos = Vector2(x , y)
        self.anim_index = 0
        self.explode = [
            image.load(r"Sprites\bullet_explosion1.png"),
            image.load(r"Sprites\bullet_explosion2.png"),
            image.load(r"Sprites\bullet_explosion3.png"),
            image.load(r"Sprites\bullet_explosion4.png")
            ]
        self.explode = [transform.scale(image,(image.get_width()*4,image.get_height()*4)) for image in self.explode]
        self.rect = Rect(x,y,self.explode[0].get_width() , self.explode[0].get_height())
        self.anim_counter = 0
    def endOfAnim(self):
        '''Checks if the animation has finished.
        Returns: true if the animation has finished, false otherwise
        '''
        if self.anim_index >= len(self.explode):
            return True
        return False
    def draw(self):
        '''Updates the required attributes to advance the explosion to its next frame.
        '''
        self.rect.center = (self.pos.x , self.pos.y) 
        self.anim_counter +=1       
        self.anim_index = (self.anim_counter + 1) // 3
    
    def __del__(self):
        pass