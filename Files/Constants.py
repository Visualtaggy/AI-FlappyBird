#setting up dimensions for game window
import os
import pygame
pygame.font.init()

window_width = 500
window_height = 800

bird_animation = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird" + str(x) + ".png"))) for x in range(1,4)]
obs_img  = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","obs.png")))
sky_img = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","sky.png")))
land_img = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","land.png")))


score_font = pygame.font.Font(os.path.join("Files","custom-font.TTF"), 50)