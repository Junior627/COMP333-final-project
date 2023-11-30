from pygame import *
from constants import *
class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []

    def update_bullets(self):
        self.update_bullet_list(self.player_bullets)
        self.update_bullet_list(self.enemy_bullets)

    def update_bullet_list(self, bullets):
        x = 0
        for bullet in bullets:
            print(x, " : ", bullet.bullet_dir )
            x+=1
            bullet.update()
            # Check for collisions or screen boundaries and handle accordingly
            if bullet.out_of_bounds(): #or bullet.collides_with_enemy():
                bullets.remove(bullet)

    def add_player_bullet(self, bullet):
        self.player_bullets.append(bullet)

    def add_enemy_bullet(self, bullet):
        self.enemy_bullets.append(bullet)
