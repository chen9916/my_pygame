#physics implementation

import math
import pygame

#aabb collision detection
def aabb_collision(rect1, rect2):
    #check if the rectangles overlap
    if rect1.right < rect2.left:
        return False
    if rect1.left > rect2.right:
        return False
    if rect1.bottom < rect2.top:
        return False
    if rect1.top > rect2.bottom:
        return False
    #if they do overlap
    return True
