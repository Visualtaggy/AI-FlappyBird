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


def draw_window(window,bird,obstacles, land, score):
     window.blit(sky_img,(0,0))

     for obstacle in obstacles:
        obstacle.draw(window)


     text = score_font.render("Score: " + str(score),1,(255,255,255))
     window.blit(text,(window_width - 10 -text.get_width(),10))
    
     land.draw(window)

     bird.draw(window)
     pygame.display.update()   




def main():
    bird = FlappyBird(220,350)


    obstacles = [Obstacle(500)]
    land = Land(730)

    window = pygame.display.set_mode((window_width,window_height))

    score = 0
    #let's not make skyrim and keep fps seprate from speed of the system.
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #bird.move()
        add_obs = False
        rem = []
        for obs in obstacles:
            if obs.collide(bird):
                pass
            if obs.x + obs.obs_top.get_width() < 0:
                rem.append(obs)
            if not obs.bird_passed and obs.x < bird.x:
                obs.bird_passed  = True
                add_obs = True
            obs.move_obs()
            
        if add_obs:
            score += 1
            obstacles.append(Obstacle(500))
        
        for r in rem:
            obstacles.remove(r)

        if bird.y + bird.img.get_height() >= 730:
            pass

        land.move()
        draw_window(window,bird,obstacles,land,score)
    pygame.quit()
    quit()


main()
