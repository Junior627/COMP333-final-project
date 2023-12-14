from pygame import *
from constants import *

'''Code used to manage bullets within the game.
Specific attributes:
player_bullets- a list of all current player bullets.
enemy_bullets- a list of all enemy bullets.
enemy_bombs- a list of all enemy bombs.
'''

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.enemy_bombs = []

    def update_bullets(self):
        '''Updates the list of bullets for each type of bullet.
        '''
        self.update_bullet_list(self.player_bullets)
        self.update_bullet_list(self.enemy_bullets)
        self.update_bomb_list(self.enemy_bombs)

    def update_bomb_list(self, bombs):
        '''Updates the list of enemy bombs.
        Args: bombs- a list of enemy bombs.
        '''
        for bomb in bombs:
            bomb.update()
            if bomb.ready_to_explode:
                new_bullets = bomb.explode()
                
                for bullet in new_bullets:
                    self.add_enemy_bullet(bullet)
                bombs.remove(bomb)
                

    def update_bullet_list(self, bullets):
        '''Updates a list of bullets, player or enemy.
        Args: bullets- a list of bullets.
        '''
        for bullet in bullets:
            bullet.update()
            # Check for collisions or screen boundaries and handle accordingly
            if bullet.out_of_bounds():
                bullets.remove(bullet)

    def check_for_collision(self, bulletList, target):
        '''Checks for collisions between bullets and a given target (ie. a player or enemy).
        Args: bulletList- the list of bullets we are checking for collisions with.
        target- the target we are checking for collisions with.
        Returns: true if a collision occurred, false otherwise
        '''
        bullets_to_remove = []
        if_collide = False

        for bullet in bulletList:
            if bullet.bullet_collider.colliderect(target.entity_collider):
                print('Collision detected!')
                bullets_to_remove.append(bullet)
                if_collide = True
        # Remove bullets outside the loop
        for bullet in bullets_to_remove:
            bulletList.remove(bullet)

        return if_collide



    def add_player_bullet(self, bullet):
        '''Adds a bullet to the list of player bullets.
        Args: bullet- the player bullet to be added.
        '''
        self.player_bullets.append(bullet)

    def add_enemy_bullet(self, bullet):
        '''Adds a bullet to the list of enemy bullets.
        Args: bullet- the enemy bullet to be added.
        '''
        self.enemy_bullets.append(bullet)

    def add_enemy_bomb(self, bomb):
        '''Adds a bomb to the list of enemy bombs.
        Args: bomb- the enemy bomb to be added.
        '''
        self.enemy_bombs.append(bomb)