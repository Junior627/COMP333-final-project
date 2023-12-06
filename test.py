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
while x < 6:
    enemyList.append(Shooter((SCREEN_WIDTH / 6) * x, 10))
    x +=1
    
y = 0
while y < 3:
    enemyList.append(Bomber((SCREEN_WIDTH / 3) * (y + .33) , 50))
    y+=1
z = 0
while z < 4:
    enemyList.append(Chaser((SCREEN_WIDTH / 4) * (z + .5) , 90))
    z+=1

clock=  time.Clock()
bulletManager = BulletManager()
fxManager = visualFXManager()

def main():
    while True:
        screen.fill((0,0,255))
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
                elif(enemy.__class__.__name__ == "Chaser"):
                    if(enemy.movement_cooldown == 0):
                        enemy.createPath(Vector2(player.entity_collider.centerx,player.pos.y))
                screen.blit(enemy.entity, enemy.entity_collider)
                
        screen.blit(player.entity, player.pos)
        
                           
        for bullet in bulletManager.player_bullets:
            screen.blit(bullet.bullet , bullet.pos)
        for bullet in bulletManager.enemy_bullets:
            screen.blit(bullet.bullet , bullet.pos)
            if bullet.out_of_bounds():
                fxManager.add_explosion_fx(bullet.pos.x,bullet.pos.y, BulletExplosion)
        for bomb in bulletManager.enemy_bombs:
            screen.blit(bomb.bomb , bomb.pos)
        bulletManager.update_bullets()     
        enemy_to_remove = []
        
        for enemy in enemyList:
            if bulletManager.check_for_collision(bulletManager.player_bullets,enemy):
                fxManager.add_explosion_fx(enemy.pos.x , enemy.pos.y, Explosion)
                enemy_to_remove.append(enemy)
        
        for enemy in enemy_to_remove:
            enemyList.remove(enemy)
        
        fxManager.update_lists()
        for explosion in fxManager.explosion_list:
            screen.blit(explosion.explode[explosion.anim_index], explosion.rect)

                            
        player.update(dir)
        
        if bulletManager.check_for_collision(bulletManager.enemy_bullets, player):
            fxManager.add_explosion_fx(bullet.pos.x,bullet.pos.y, BulletExplosion)
        
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()