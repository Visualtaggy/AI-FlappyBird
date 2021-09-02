import time
import os
import random
import pygame
import neat

#setting up dimensions for game window
window_width = 500
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

    def jump(self):
        # x,y = 0,0 so -15 speed will make the bird jump down aka negative velocity 
        self.speed = -15;
        self.tick = 0
        self.height = self.y

    def move(self):
        self.tick += 1
        #calculating displacement here with use of tick count so that the position of the bird every second can be found
        displacement = self.speed * self.tick + 1.5 * self.tick ** 2
        
        if(displacement >= 15):
            displacement =  15

        if(displacement < 0):
            displacement -= 3

        self.y = self.y + displacement

        #calculating arc of bird aka tilt 
        #checking if bird is going up 
        if(displacement < 0 or self.y < self.height + 50):
            if self.tilt < self.max_rotation:
                self.tilt = self.max_rotation
        else:
            if self.tilt > -90:
                self.tilt -= self.rotation_speed

    


    
