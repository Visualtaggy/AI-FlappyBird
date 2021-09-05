from Files.Constants import *
import pygame


class FlappyBird:
    max_rotation = 25
    imgs = bird_animation
    rotation_speed = 20
    animation_time = 5

    def __init__(self, x, y):
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
        self.speed = -10.5
        self.tick = 0
        self.height = self.y

    def move(self):
        self.tick += 1        
        #calculating displacement here with use of tick count so that the position of the bird every second can be found
        displacement = self.speed * self.tick + 1.5 * self.tick ** 2

        if (displacement) >= 15:
            displacement = (displacement/abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        #calculating arc of bird aka tilt 
        #checking if bird is going up 

        if displacement < 0 or self.y < self.height + 50:  
            if self.tilt < self.max_rotation:
                self.tilt = self.max_rotation
        else: 
            if self.tilt > -90:
                self.tilt -= self.rotation_speed

    def draw(self, win):
        # For animation of bird, loop through three images

        self.img_counter += 1

        if self.img_counter <= self.animation_time:
            self.img = self.imgs[0]
        elif self.img_counter <= self.animation_time*2:
            self.img = self.imgs[1]
        elif self.img_counter <= self.animation_time*3:
            self.img = self.imgs[2]
        elif self.img_counter <= self.animation_time*4:
            self.img = self.imgs[1]
        elif self.img_counter == self.animation_time*4 + 1:
            self.img = self.imgs[0]
            self.img_counter = 0
         # so when bird is nose diving it isn't flapping
        if self.tilt <= -80:
            self.img = self.imgs[1]
            self.img_counter = self.animation_time*2

        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_coll(self):
        return pygame.mask.from_surface(self.img)

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)