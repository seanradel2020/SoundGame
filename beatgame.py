### TODO:
#Beat circles should shrink in raidus
#When beat circles are clicked, another beat appears,
#as beat gets smaller, the pitch grows higher
#use .wav files for sounds , you can see how sounds are implemented in burgrerfight.py
#after beats hit 0 radius they should be deleted entirely 




import pygame,sys
from pygame.locals import *
import os
import random as rd
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)

class Beat(object):
    def __init__(self):
        self.radius = 50
        #self.positions = []
    def random_color(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        return (r, g, b)

    def draw(self,surf):

        pos = (rd.randint(50,400),rd.randint(50,750))
        #self.posistions.append(pos)
        pygame.draw.circle(g.screen,self.random_color(), pos, self.radius)


class game(object):

    def __init__(self):
        #WIDTH = 1200
        #HEIGHT = 600
        display_width = 450
        display_height = 800
        #self.bg = pygame.image.load("bcg.png")
        self.center = [0, 0]
        #gameDisplay = pygame.display.set_mode((display_width,display_height))
        self.screen = pygame.display.set_mode((display_width,display_height))
        self.clock = pygame.time.Clock()
        self.player = Beat()
        #self.enemy = BurgerEnemy()

    def drawStars(self,surf):
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        for i in range(250):
            pygame.draw.rect(self.screen,WHITE,(rd.randint(3,447),rd.randint(3,793),3,3))
            #pygame.draw.rect(self.screen,RED,(random.randint(3,447),random.randint(3,793),3,3))
            #pygame.draw.rect(self.screen,BLACK,(random.randint(3,447),random.randint(3,793),3,3))
            #pygame.draw.rect(self.screen,BLUE,(random.randint(3,447),random.randint(3,793),3,3))
            #pygame.draw.rect(self.screen,GREEN,(random.randint(3,447),random.randint(3,793),3,3))

    def draw(self, surf):
        surf.blit(self.bg, self.center)



    def run(self):



        #hitSound = pygame.mixer.Sound("hit.wav")

        pygame.init()
        #punchSound = [pygame.mixer.Sound("low_punch.wav"), pygame.mixer.Sound("normal_punch.wav"), pygame.mixer.Sound("high_punch.wav")]
        pygame.mixer.music.load('burgarena.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops = -1)
        running = 1

        self.drawStars(self.screen)
        self.player.draw(self.screen)

        while running:
            self.clock.tick(60)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                running = 0

            keys = pygame.key.get_pressed()

            pygame.display.update()


g = game()
g.run()
