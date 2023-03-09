import pygame
from object import Player

#funcions for loading the assets and initializing the classes for the game 

#function for initializing the player
def init_player():
    player = Player()
    return player

#function for loading the background
def load_background():
    background = pygame.image.load("image/background.png")
    background = pygame.transform.scale(background, (640, 480))
    #put the background in the center of the screen
    background_rect = background.get_rect()
    background_rect.center = (320, 240)

    return background

#function to put everything together
def load_game():
    #initialize the player
    player = init_player()
    #load the background
    
    return player