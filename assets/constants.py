import os
import pygame

bgColour = (22,19,36)
width = 393
height = 852
tablesize = 151
hashInterval = 3
basePath = os.path.dirname(os.path.dirname(__file__))
DBpath = os.path.join(basePath, 'nea.db')
uploadPath = os.path.join(basePath, 'upload')
assetsPath = os.path.join(basePath, 'assets')
hashPath = os.path.join(basePath, 'hashes.csv')
textFont = os.path.join(assetsPath, 'DIN Next Rounded LT W01 Regular.ttf')
buttonFont = os.path.join(assetsPath, 'din-next-rounded-lt-pro-bold.ttf')
headingFont = os.path.join(assetsPath, 'Feather Bold.ttf')
logoPath = os.path.join(assetsPath, 'lingpro logo no red line.png')
logo = pygame.image.load(logoPath)
topicColours = [(0,0,255), (255,0,0), (0,255,0), (255,255,0), (0,255,255), (255,0,255)]
