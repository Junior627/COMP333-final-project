import pygame
from .generic_state import generic_state
import levelcontrolparameters
from player import Player
from enemy import Shooter, Bomber, Chaser
from bulletManager import BulletManager
from visualFXManager import visualFXManager, Explosion, BulletExplosion

'''Code for the game state upon level selection.
Specific attributes:
player- the ship the user should be able to control.
enemies- the list of enemies currently are currently on screen.
bullets- a class used to manage the bullets currently on screen.
fx- a class used to manage the visual effects currently on screen.
enemies_spawning- a list of lists, with each sublist representing
the total number of enemies that should spawn for the level corresponding
to its index.
'''

class shipgame(generic_state):
    def __init__(self):
        super(shipgame, self).__init__()
        self.player = Player()
        self.enemies = []
        self.bullets = BulletManager()
        self.fx = visualFXManager()
        self.enemies_spawning = [
            [1, 0, 0],
            [4, 0, 0],
            [6, 0, 0],
            [0, 2, 0],
            [2, 1, 0],
            [3, 3, 0],
            [6, 3, 0],
            [0, 0, 3],
            [2, 0, 2],
            [1, 3, 1],
            [5, 0, 3],
            [0, 0, 4],
            [0, 3, 4],
            [3, 3, 3],
            [6, 3, 4]]
        self.backdrops = [
            pygame.image.load(r'Sprites\fog_bg1.png'),
            pygame.image.load(r'Sprites\nova_bg1.png'),
            pygame.image.load(r'Sprites\spiral_bg1.png'),
            pygame.image.load(r'Sprites\fog_bg2.png'),
            pygame.image.load(r'Sprites\nova_bg2.png'),
            pygame.image.load(r'Sprites\spiral_bg2.png'),
            pygame.image.load(r'Sprites\fog_bg3.png'),
            pygame.image.load(r'Sprites\nova_bg3.png'),
            pygame.image.load(r'Sprites\spiral_bg3.png'),
            pygame.image.load(r'Sprites\fog_bg4.png'),
            pygame.image.load(r'Sprites\nova_bg4.png'),
            pygame.image.load(r'Sprites\spiral_bg4.png'),
            pygame.image.load(r'Sprites\fog_bg5.png'),
            pygame.image.load(r'Sprites\nova_bg5.png'),
            pygame.image.load(r'Sprites\spiral_bg5.png')]
        self.next_state = "gameover"

    def spawn_enemies(self, level):
        shooters, bombers, chasers = self.enemies_spawning[level]
        x = 0
        while x < shooters:
            self.enemies.append(Shooter((self.screen_rect.width / shooters) * (x + .33), 30 , self.bullets))
            x += 1
        y = 0
        while y < bombers:
            self.enemies.append(Bomber((self.screen_rect.width / bombers) * (y + .33) , 70 , self.bullets))
            y+= 1
        z = 0
        while z < chasers:
            self.enemies.append(Chaser((self.screen_rect.width / chasers) * (z + .5) , 120 , self.bullets, self.player))
            z+= 1

    def startup(self):
        self.player.initStats(levelcontrolparameters.weapon_choice, levelcontrolparameters.engine_choice)
        self.player.pos = pygame.Vector2(self.screen_rect.width / 2 , (self.screen_rect.height * 3) / 4)
        self.enemies = []
        self.bullets.player_bullets = []
        self.bullets.enemy_bullets = []
        self.bullets.enemy_bombs = []
        self.fx.explosion_list = []
        self.fx.bullet_explosion_list = []
        self.spawn_enemies(levelcontrolparameters.current_level)
        self.next_state = "gameover"
        
        self.healthPoints = []
        self.healthSprite = pygame.image.load(r'Sprites/health_point.png')
        self.healthSprite = pygame.transform.scale(self.healthSprite,(self.healthSprite.get_width()*2, self.healthSprite.get_height()*2))
        for x in range(self.player.health):
            self.healthPoints.append(self.healthSprite)
            
    
    def get_event(self, event):
        '''Code for handling events in the ship game state.
        '''
        if event.type == pygame.QUIT:
            self.quit = True

    def displayHealth(self, surface):
        x = 0
        for healthPoint in self.healthPoints:
            surface.blit(healthPoint, (x * 10, 500))
            x+=1

    def draw(self, surface):
        '''Code for screen display in the ship game state. Includes a bit of logic that was difficult
        to include elsewhere thanks to the use of get_pressed instead of keydown.
        Much of this code taken from test.py.
        '''
        surface.blit(self.backdrops[levelcontrolparameters.current_level], (0,0))

        dir = pygame.Vector2(0,0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dir.y = -1
        if keys[pygame.K_DOWN]:
            dir.y = 1
        if keys[pygame.K_LEFT]:
            dir.x = -1
        if keys[pygame.K_RIGHT]:
            dir.x = 1
        if keys[pygame.K_SPACE]:
            bullet = self.player.shoot()
            if bullet != None:
                self.bullets.add_player_bullet(bullet)
        
        if self.enemies != []:
            for enemy in self.enemies:
                enemy.update(pygame.Vector2(self.player.entity_collider.centerx,self.player.pos.y))
                surface.blit(enemy.entity, enemy.entity_collider)

        enemy_to_remove = []
        
        for enemy in self.enemies:
            if self.bullets.check_for_collision(self.bullets.player_bullets,enemy):
                self.fx.add_explosion_fx(enemy.pos.x , enemy.pos.y, BulletExplosion)
                if enemy.takeDamage(self.player.bullet_damage):
                    enemy_to_remove.append(enemy)
                    self.fx.add_explosion_fx(enemy.pos.x, enemy.pos.y, Explosion)
        
        for enemy in enemy_to_remove:
            self.enemies.remove(enemy)
            if self.enemies == []:
                self.next_state = "victory"
                self.done = True
        
        surface.blit(self.player.entity, self.player.pos)

        for bullet in self.bullets.player_bullets:
            surface.blit(bullet.bullet , bullet.pos)
        for bullet in self.bullets.enemy_bullets:
            surface.blit(bullet.bullet , bullet.pos)
            if self.bullets.check_for_collision([bullet], self.player):
                self.fx.add_explosion_fx(bullet.pos.x, bullet.pos.y , BulletExplosion)
                self.bullets.enemy_bullets.remove(bullet)
                del self.healthPoints[-1]
                self.player.takeDamage()
            if bullet.out_of_bounds():
                self.fx.add_explosion_fx(bullet.pos.x,bullet.pos.y, BulletExplosion)
        for bomb in self.bullets.enemy_bombs:
            surface.blit(bomb.bomb , bomb.pos)
        
        self.bullets.update_bullets()    
        self.fx.update_lists()
        
        for explosion in self.fx.explosion_list:
            surface.blit(explosion.explode[explosion.anim_index], explosion.rect)

        self.displayHealth(surface)
                            
        self.player.update(dir)
        print(levelcontrolparameters.weapon_choice)
  
        if self.player.health <= 0:
            self.done = True