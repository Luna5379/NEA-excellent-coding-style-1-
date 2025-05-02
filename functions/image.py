import pygame
from assets.constants import *

def transparentImage(image):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            if image.get_at((x, y)) == (255, 255, 255, 255):
                image.set_at((x,y)), ((255, 255, 255, 0))  
    pygame.image.save(image, os.path.join(assetsPath, 'transparent.png'))
    return image