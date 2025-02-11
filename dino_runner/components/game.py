from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.text_utils import TextUtils
import pygame, os
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, COLORS, RUNNING, BIRD, BGMENU, FONDOP, HEART, FONDOP2, FONDOP3, FONDOP4
from dino_runner.components.dinosaur import Dinosaur



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.lifes = 3
        self.text_utils = TextUtils()
        self.game_running = True
        self.is_playing_music = False
        self.powerup_manager = PowerUpManager()

    def run(self):
        pygame.mixer.music.load(os.path.join("fondo.mp3")) 
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.is_playing_music = True
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.points = 0
        self.lifes = 3
        while self.playing:
            self.events()
            self.update()
            self.draw()

        pygame.mixer.music.stop()
        self.is_playing_music = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.update(pygame.key.get_pressed()) #tambien se podia poner self.player.update(user_input) 
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points, self.game_speed, self.player)


    def draw(self):
        
        self.clock.tick(FPS)
        if self.points >= 0:
            self.screen.blit(FONDOP, (0, 0))
        if self.points >= 500:
            self.screen.blit(FONDOP2,(0, 0))
        if self.points >= 1000:
            self.screen.blit(FONDOP3,(0, 0))
        if self.points >= 1500:
            self.screen.blit(FONDOP4,(0, 0))

        self.draw_background()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.score()
        self.Hearts()

        if self.is_playing_music:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1
        text, text_rect = self.text_utils.get_score(self.points)
        self.player.check_invincibility()
        self.screen.blit(text, text_rect)

    def Hearts(self):
        lifesUI = self.lifes
        x = 50
        for i in range(lifesUI):
            self.screen.blit(HEART, (x, 10))
            x += 40 
            
        

    def show_menu(self, death_count = 0):
        self.game_running = True
        self.screen.blit(BGMENU,(0, 0))

        self.print_menu_elements(death_count)

        pygame.display.update()
        self.handle_key_events()

    def print_menu_elements(self, deat_count = 0):
        text, text_rect = self.text_utils.get_centered_message("Press any key to Start")
        self.screen.blit(text, text_rect)
        if deat_count > 0:
            score, score_rect = self.text_utils.get_centered_message(
                "Your Score: " + str(self.points),
                height= SCREEN_HEIGHT//2 + 50)
            self.screen.blit(score, score_rect)

        message, message_rect = self.text_utils.get_menu_message("Use the up arrow key to jump over obstacles")
        self.screen.blit(message, message_rect)
        self.screen.blit(RUNNING[0], (SCREEN_WIDTH//2 - 20, SCREEN_HEIGHT//2 - 140))
        self.screen.blit(BIRD[1], (SCREEN_WIDTH - 150, SCREEN_HEIGHT//2 - 240))


    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()

#agregarle 1 power up
#agregarle 1 obstaculo
#agregarle si se puede un fondo diferente
#agregarle nubes
#agregaarle lo que queremos a nuestra creatividad
