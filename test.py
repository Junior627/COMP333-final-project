'''This code was initially used to test things in the ship game state
before the ship game state was completed. Now, it currently isn't used
for anything, and it should not be called anywhere upon the project being
run.
'''


import pygame
from player import *
from enemy import *
from bulletManager import *
from visualFXManager import *
from GameStates.customization import*
from constants import *
import sys

init()

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

player = Player()
enemyList = []

clock=  time.Clock()
bulletManager = BulletManager()
fxManager = visualFXManager()
backdrop = image.load(r'Sprites\bg_2.png')
backdrop = transform.scale(backdrop,(backdrop.get_width()*2, backdrop.get_height()*2))
x = 0
while x < 6:
    enemyList.append(Shooter((SCREEN_WIDTH / 6) * (x +.33), 30 , bulletManager))
    x +=1
    
y = 0
while y < 3:
    enemyList.append(Bomber((SCREEN_WIDTH / 3) * (y + .33) , 70 , bulletManager))
    y+=1
z = 0
while z < 4:
    enemyList.append(Chaser((SCREEN_WIDTH / 4) * (z + .5) , 120 , bulletManager, player))
    z+=1



def main():
    while True:
        screen.fill((0,0,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
        screen.blit(backdrop, (0,0))    
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
                
                enemy.update(Vector2(player.entity_collider.centerx,player.pos.y))
                screen.blit(enemy.entity, enemy.entity_collider)
                
        screen.blit(player.entity, player.pos)
        
        enemy_to_remove = []
        
        for enemy in enemyList:
            if bulletManager.check_for_collision(bulletManager.player_bullets,enemy):
                fxManager.add_explosion_fx(enemy.pos.x , enemy.pos.y, BulletExplosion)
                if enemy.takeDamage(player.bullet_damage):
                    enemy_to_remove.append(enemy)
                    fxManager.add_explosion_fx(enemy.pos.x , enemy.pos.y, Explosion)                   
        
        for enemy in enemy_to_remove:
            enemyList.remove(enemy)
        
        for bullet in bulletManager.player_bullets:
            screen.blit(bullet.bullet , bullet.pos)
            
        for bullet in bulletManager.enemy_bullets:
            screen.blit(bullet.bullet , bullet.pos)
            if bulletManager.check_for_collision([bullet], player):
                fxManager.add_explosion_fx(bullet.pos.x,bullet.pos.y, BulletExplosion)
                bulletManager.enemy_bullets.remove(bullet)
                player.takeDamage()
                
            if bullet.out_of_bounds():
                fxManager.add_explosion_fx(bullet.pos.x,bullet.pos.y, BulletExplosion)
                
        for bomb in bulletManager.enemy_bombs:
            screen.blit(bomb.bomb , bomb.pos)
        
        fxManager.update_lists() 
        bulletManager.update_bullets()     
        
        for explosion in fxManager.explosion_list:
            screen.blit(explosion.explode[explosion.anim_index], explosion.rect)

                           
        player.update(dir)
        
        
        text_surface = my_font.render(("Your health: %s" % player.health), 1, (255, 9, 12))
        screen.blit(text_surface, (0,0))
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()