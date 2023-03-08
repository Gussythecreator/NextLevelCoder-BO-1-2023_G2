from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS
import pygame
import random

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        index = random.randint(0, 2)
    
        if len(self.obstacles) == 0:
            if index == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif index == 1:
                self.obstacles.append(Bird(BIRD))
            elif index == 2:
                self.obstacles.append(Cactus(LARGE_CACTUS))

           # self.obstacles.append(Cactus(SMALL_CACTUS))
           # self.obstacles.append(Cactus(LARGE_CACTUS))
           # self.obstacles.append(Bird(BIRD))



        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []