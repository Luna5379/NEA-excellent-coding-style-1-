import pygame

from assets.constants import *
from functions.buttons import createButton
from functions.image import transparentImage

def frontPage(surface):
    surface.fill(color=bgColour)
    lingPro = transparentImage(logo.convert_alpha())
    surface.blit(lingPro, (0, 250))
    signup = createButton([(119,73,248), (38,32,54), (52.5,665), ('SIGN UP'), surface, (pygame.font.Font(buttonFont, 18)), (85,24,214), width, (318,42)])
    login = createButton([(119,73,248), (38,32,54), (52.5,725), ('LOG IN'), surface, (pygame.font.Font(buttonFont, 18)), (85,24,214), width, (318,42)])
    if not signup:
       return 'signup1'
    elif not login:
       return 'login'
    else:
       return 'frontPage'
