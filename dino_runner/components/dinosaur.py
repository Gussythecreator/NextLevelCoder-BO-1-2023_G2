import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    RUNNING, 
    DUCKING, JUMPING, 
    DEFAULT_TYPE, SHIELD_TYPE,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD, HAMMER_TYPE,
    RUNNING_HAMMER, JUMPING_HAMMER,
    DUCKING_HAMMER, 
)

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    POS_Y_DUCKING = 347
    JUMP_VEL = 8.5

    def __init__(self):
        
        self.run_img = {
            DEFAULT_TYPE: RUNNING,
            SHIELD_TYPE: RUNNING_SHIELD,
            HAMMER_TYPE: RUNNING_HAMMER
            
        }
        self.duck_img = {
            DEFAULT_TYPE: DUCKING,
            SHIELD_TYPE: DUCKING_SHIELD,
            HAMMER_TYPE: DUCKING_HAMMER
        }
        self.jump_img = {
            DEFAULT_TYPE: JUMPING,
            SHIELD_TYPE: JUMPING_SHIELD,
            HAMMER_TYPE: JUMPING_HAMMER
        }
        self.type = DEFAULT_TYPE
        
        self.image = self.run_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index = 0
        self.dino_running = True
        self.dino_ducking = False
        self.dino_jumping = False
        self.jump_vel = self.JUMP_VEL
        self.setup_state_booleans()


    def setup_state_booleans(self):
        self.has_powerup = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input):
        if self.dino_running:
            self.run()
        elif self.dino_ducking:
            self.duck()
        elif self.dino_jumping:
            self.jump()

        if user_input[pygame.K_DOWN] and not self.dino_jumping:
            self.dino_running = False
            self.dino_ducking = True
            self.dino_jumping = False
        elif user_input[pygame.K_UP] and not self.dino_jumping:
            self.dino_running = False
            self.dino_ducking = False
            self.dino_jumping = True
        elif not self.dino_jumping:
            self.dino_running = True
            self.dino_ducking = False
            self.dino_jumping = False


        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)

    def run(self):
        self.image = self.run_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y_DUCKING
        self.step_index += 1    


    def jump(self):
        self.image = self.jump_img[self.type]    
        if self.dino_jumping:
            self.dino_rect.y -= self.jump_vel * 4  # Salto            
            self.jump_vel -= 0.8 # Salto, cuando llega a negativo, baja        
        if self.jump_vel < -self.JUMP_VEL: # Cuando llega a JUMP_VEL en negativo, este se detiene         
            self.dino_rect.y = self.POS_Y         
            self.dino_jumping = False          
            self.jump_vel = self.JUMP_VEL

    def check_invincibility(self):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks())/1000, 2)             # REVISAR
            if time_to_show >= 0:
                #show remaining time
                pass
            else:
                self.shield = False
                self.type = DEFAULT_TYPE

    def update_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE
   


#Crear clase Dinosaur, metodo constructor, metodo update, draw pass (entregar)
# Investigar que son los sprites
# Investigar herencia en programacion 