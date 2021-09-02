import time
import os
import random
import pygame
import neat

#setting up dimensions for game window
window_width = 600
windows_height = 800

bird_animation = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird3.png")))]

