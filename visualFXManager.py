from pygame import *



class visualFXManager:
    def __init__(self):
        self.explosion_list = []
        self.bullet_explosion_list = []
        
    def update_lists(self):
        self.update_fx_list(self.explosion_list)
        
    def update_fx_list(self, list):
        
        for fx in list:
            fx.draw()
            if fx.endOfAnim():
                print("End of Animatin")
                list.remove(fx)
                
    def add_explosion_fx(self, x , y, fx_arg):
        self.explosion_list.append(fx_arg(x,y))
    
    
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
        if self.anim_index >= len(self.explode):
            print(len(self.explode))
            return True
        return False
    def draw(self):
        self.rect.topleft = (self.pos.x , self.pos.y) 
        self.anim_counter +=1       
        self.anim_index = (self.anim_counter + 1) // 3
        print(self.anim_index)
    
    def __del__(self):
        print("Effect Ended")

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
        if self.anim_index >= len(self.explode):
            print(len(self.explode))
            return True
        return False
    def draw(self):
        self.rect.topleft = (self.pos.x , self.pos.y) 
        self.anim_counter +=1       
        self.anim_index = (self.anim_counter + 1) // 3
        print(self.anim_index)
    
    def __del__(self):
        print("Effect Ended")