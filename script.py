import time
import os
import random
import pygame
import neat
from Files.Bird import FlappyBird
from Files.Constants import *
from Files.Obs import Obstacle
from Files.Land import Land

pygame.display.set_caption("AI FlappyBird - Vishal Tyagi")


def draw_window(window,bird,obstacles, land):
     window.blit(sky_img,(0,0))

     for obstacle in obstacles:
        obstacle.draw(window)

     land.draw(window)

     bird.draw(window)
     pygame.display.update()   




def main():
    bird = FlappyBird(220,350)


    obstacles = [Obstacle(700)]
    land = Land(730)

    window = pygame.display.set_mode((window_width,window_height))

    #let's not make skyrim and keep fps seprate from speed of the system.
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #bird.move()
        for obs in obstacles:
            obs.move_obs()

        land.move()
        draw_window(window,bird,obstacles,land)
    pygame.quit()
    quit()


main()
