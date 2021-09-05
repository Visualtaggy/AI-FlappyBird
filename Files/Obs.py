import pygame
from Files.Constants import *
import random

class Obstacle():
    space = 200
    speed = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.obs_top = pygame.transform.flip(obs_img, False, True)
        self.obs_bottom = obs_img

        self.bird_passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.obs_top.get_height()
        self.bottom = self.height + self.space

    def move(self):
        self.x -= self.speed

    def draw(self, win):
        win.blit(self.obs_top, (self.x, self.top))
        win.blit(self.obs_bottom, (self.x, self.bottom))

    def collide(self, bird, win):

        
        bird_mask = bird.get_coll()
        top_mask = pygame.mask.from_surface(self.obs_top)
        bottom_mask = pygame.mask.from_surface(self.obs_bottom)
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True

        return False