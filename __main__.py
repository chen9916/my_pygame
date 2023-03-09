import pygame
import loadgame
import graphicalfuncs

# initialize Pygame
pygame.init()

# set the window size
size = (640, 480)

# create the window
screen = pygame.display.set_mode(size)

# set the window title
pygame.display.set_caption("My Pygame Window")

#load   background
background = loadgame.load_background()

#load player
player = loadgame.init_player()


# run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#draw the background

    screen.blit(background, background.get_rect())

#draw the player
    screen.blit(player.image, player.rect)

    #if press space
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        #multiply the player image with the background image
        player.image = graphicalfuncs.multiply_images(player.image, background)
        
            
     #asdw to move the player
    if pygame.key.get_pressed()[pygame.K_a]:
            player.rect.x -= 1
    if pygame.key.get_pressed()[pygame.K_d]:
            player.rect.x += 1
    if pygame.key.get_pressed()[pygame.K_w]:
            player.rect.y -= 1
    if pygame.key.get_pressed()[pygame.K_s]:
            player.rect.y += 1
            
    

    # update the display
    pygame.display.flip()

# quit Pygame
pygame.quit()
