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
            [8, 0, 0],
            [0, 2, 0],
            [2, 1, 0],
            [3, 3, 0],
            [0, 4, 0],
            [0, 0, 3],
            [2, 0, 2],
            [1, 3, 1],
            [5, 0, 3],
            [0, 0, 6],
            [0, 3, 4],
            [3, 3, 3],
            [6, 3, 4]]
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
            self.enemies.append(Chaser((self.screen_rect.width / chasers) * (z + .5) , 120 , self.bullets))
            z+= 1

    def startup(self):
        self.spawn_enemies(levelcontrolparameters.current_level)
        self.player_hit = False
        self.next_state = "gameover"
    
    def get_event(self, event):
        '''Code for handling events in the ship game state.
        '''
        if event.type == pygame.QUIT:
            self.quit = True

    def draw(self, surface):
        '''Code for screen display in the ship game state. Includes a bit of logic that was difficult
        to include elsewhere thanks to the use of get_pressed instead of keydown.
        Much of this code taken from test.py.
        '''
        surface.fill(pygame.Color("black"))

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

        surface.blit(self.player.entity, self.player.pos)

        for bullet in self.bullets.player_bullets:
            surface.blit(bullet.bullet , bullet.pos)
        for bullet in self.bullets.enemy_bullets:
            surface.blit(bullet.bullet , bullet.pos)
            if bullet.out_of_bounds():
                self.fx.add_explosion_fx(bullet.pos.x,bullet.pos.y, BulletExplosion)
        for bomb in self.bullets.enemy_bombs:
            surface.blit(bomb.bomb , bomb.pos)
        self.bullets.update_bullets()     
        enemy_to_remove = []
        
        for enemy in self.enemies:
            if self.bullets.check_for_collision(self.bullets.player_bullets,enemy):
                self.fx.add_explosion_fx(enemy.pos.x , enemy.pos.y, Explosion)
                enemy_to_remove.append(enemy)
        
        for enemy in enemy_to_remove:
            self.enemies.remove(enemy)
        
        self.fx.update_lists()
        for explosion in self.fx.explosion_list:
            surface.blit(explosion.explode[explosion.anim_index], explosion.rect)

                            
        self.player.update(dir)
        
        if self.bullets.check_for_collision(self.bullets.enemy_bullets, self.player):
            self.fx.add_explosion_fx(bullet.pos.x,bullet.pos.y, BulletExplosion)