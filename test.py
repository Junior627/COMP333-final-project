import pygame
from player import *
from enemy import *
from bulletManager import *
from visualFXManager import *
from GameStates.customization import*
from constants import *
import sys

init()
size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

player = Player()
enemyList = []
x = 0
while x < 10:
    enemyList.append(Shooter((SCREEN_WIDTH / 10) * x, 10))
    x +=1
    
y = 0
while y < 4:
    enemyList.append(Bomber((SCREEN_WIDTH / 4) * (y + .5) , 30))
    y+=1

clock=  time.Clock()
bulletManager = BulletManager()
fxManager = visualFXManager()

def main():
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        dir = Vector2(0,0)
        keys = key.get_pressed()
        if keys[K_w]:
            dir.y = -1
        if keys[K_s]:
            dir.y = 1
        if keys[K_a]:
            dir.x = -1
        if keys[K_d]:
            dir.x = 1

        
        if keys[K_p]:
            bullet = player.shoot()
            if bullet != None:
                bulletManager.add_player_bullet(bullet)

                    
        if enemyList != []:
            for enemy in enemyList:
                
                enemy.update()
                
                if(enemy.bullet_cooldown == 0 and enemy.__class__.__name__ == "Shooter"):
                    bulletManager.add_enemy_bullet(enemy.shootBullet(Vector2(player.entity_collider.centerx,player.pos.y)))
                elif (enemy.bullet_cooldown == 0 and enemy.__class__.__name__ == "Bomber"):
                    bulletManager.add_enemy_bomb(enemy.shootBomb(Vector2(player.entity_collider.centerx , player.pos.y)))
                screen.blit(enemy.entity, enemy.pos)
                
        screen.blit(player.entity, player.pos)
        
        
        bulletManager.update_bullets()                    
        for bullet in bulletManager.player_bullets:
            screen.blit(bullet.bullet , bullet.pos)
        for bullet in bulletManager.enemy_bullets:
            screen.blit(bullet.bullet , bullet.pos)
        for bomb in bulletManager.enemy_bombs:
            screen.blit(bomb.bomb , bomb.pos)
            
        enemy_to_remove = []
        for enemy in enemyList:
            if bulletManager.check_for_collision(bulletManager.player_bullets,enemy):
                fxManager.add_explosion_fx(enemy.pos.x , enemy.pos.y)
                enemy_to_remove.append(enemy)
        
        for enemy in enemy_to_remove:
            enemyList.remove(enemy)
        
        fxManager.update_lists()
        for explosion in fxManager.explosion_list:
            screen.blit(explosion.explode[explosion.anim_index], explosion.pos)
            
        player.update(dir)
        
        if bulletManager.check_for_collision(bulletManager.enemy_bullets, player):
            print("HIT!")
        
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()