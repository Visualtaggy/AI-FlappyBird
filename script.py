import time
import os
import random
import pygame
import neat
from Files.Bird import FlappyBird
from Files.Constants import *



def draw_window(window,bird):
     window.blit(sky_img,(0,0))
     bird.draw(window)
     pygame.display.update()   




def main():
    bird = FlappyBird(200,200)
    window = pygame.display.set_mode((window_width,window_height))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(window,bird)
    pygame.quit()
    quit()


main()

    


    
