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


def draw_window(window,birds,obstacles, land, score):
     window.blit(sky_img,(0,0))

     for obstacle in obstacles:
        obstacle.draw(window)


     text = score_font.render("Score: " + str(score),1,(255,255,255))
     window.blit(text,(window_width - 10 -text.get_width(),10))
     for bird in birds:
         bird.draw(window)


     land.draw(window)

     
     pygame.display.update()   




def main(genomes,config):
    nets = []
    ge = []
    # bird = FlappyBird(220,350)
    birds = []

    for _, gene in genomes:
        net = neat.nn.FeedForwardNetwork.create(gene,config)
        nets.append(net)
        birds.append(FlappyBird(220,350))
        gene.fitness = 0
        ge.append(gene)




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
                pygame.quit()
                quit()
        
        pipe_ind = 0
        if len(birds) > 0:
            if len(obstacles) > 1 and birds[0].x > obstacles[0].x + obstacles[0].obs_top.get_width():
                pipe_ind = 1
        else:
            run = False
            break
        
        for x,bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            output = nets[x].activate((bird.y,abs(bird.y - obstacles[pipe_ind].height),abs(bird.y - obstacles[pipe_ind].bottom)))


            if output[0] > 0.5:
                bird.jump()
             


           
        #bird.move()
        add_obs = False
        rem = []
        for obs in obstacles:
            for x, bird in enumerate(birds):
                if obs.collide(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                    

                if not obs.bird_passed and obs.x < bird.x:
                    obs.bird_passed  = True
                    add_obs = True

            if obs.x + obs.obs_top.get_width() < 0:
                rem.append(obs)

            obs.move_obs()
            
        if add_obs:
            score += 1
            for genes in ge:
                genes.fitness += 5
            obstacles.append(Obstacle(500))
        
        for r in rem:
            obstacles.remove(r)

        for x,bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        land.move()
        draw_window(window,birds,obstacles,land,score)
#    pygame.quit()
#    quit()



def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
    neat.DefaultSpeciesSet, neat.DefaultStagnation,config_file)

    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    winner = population.run(main,50)


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir,"Files","config.txt")
    run(config_path)