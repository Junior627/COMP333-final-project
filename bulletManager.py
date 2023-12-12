from pygame import *
from constants import *
class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.enemy_bombs = []

    def update_bullets(self):
        self.update_bullet_list(self.player_bullets)
        self.update_bullet_list(self.enemy_bullets)
        self.update_bomb_list(self.enemy_bombs)

    def update_bomb_list(self, bombs):
        for bomb in bombs:
            bomb.update()
            if bomb.ready_to_explode:
                new_bullets = bomb.explode()
                
                for bullet in new_bullets:
                    self.add_enemy_bullet(bullet)
                bombs.remove(bomb)
                

    def update_bullet_list(self, bullets):
        for bullet in bullets:
            bullet.update()
            # Check for collisions or screen boundaries and handle accordingly
            if bullet.out_of_bounds(): #or bullet.collides_with_enemy():
                bullets.remove(bullet)

    def check_for_collision(self, bulletList, target):
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
        self.player_bullets.append(bullet)

    def add_enemy_bullet(self, bullet):
        self.enemy_bullets.append(bullet)

    def add_enemy_bomb(self, bomb):
        self.enemy_bombs.append(bomb)