import time
import os
import random
import pygame
import neat

#setting up dimensions for game window
window_width = 600
windows_height = 800

bird_animation = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird3.png")))]
obs_img = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","obs.png")))
sky_img = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","sky.png")))
land_img = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","land.png")))


class FlappyBird:
    imgs  = bird_animation
    max_rotation  = 25
    rotation_speed = 20
    animation_time = 5

    def __init__(self ,x,y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick = 0
        self.speed = 0
        self.height = self.y
        self.img_counter = 0
        self.img = self.imgs[0]
