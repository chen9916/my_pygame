
#grapgical functions    

import pygame


#function to multiple two images by each pixel
def multiply_images(image1, image2):
    #get the size of the images
    width = image1.get_width()
    height = image1.get_height()
    #create a new image
    new_image = pygame.Surface((width, height))
    #loop through the pixels
    for x in range(width):
        for y in range(height):
            #get the color of the pixel
            color1 = image1.get_at((x, y))
            color2 = image2.get_at((x, y))
            #multiply the colors
            color = (color1[0] * color2[0] // 255, color1[1] * color2[1] // 255, color1[2] * color2[2] // 255)
            #set the color of the pixel
            new_image.set_at((x, y), color)
    #return the new image
    return new_image