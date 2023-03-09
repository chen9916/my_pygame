#classes for defining objects in the game

import pygame
import random
import math
from pygame import mixer


class Player(pygame.sprite.Sprite):
    #define parameters for the player
    def __init__(self):
        #sprite class parameters for the player to be used later
        super().__init__()
        #load the image for the player
        self.image = pygame.image.load("image/player.png")
        #set the size of the player by using the image

        
        
        self.image = pygame.transform.scale(self.image, (64, 64))   
        self.rect = self.image.get_rect()
      #position of the player
        self.rect.center = (320, 240)



        #set the size of the player by using the image
        self.rect = self.image.get_rect()   
        self.rect.center = (320, 240)
        


    
        
        

