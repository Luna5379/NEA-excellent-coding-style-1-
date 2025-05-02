import pygame

from assets.constants import *

class table: #display table design with each column etc.
    def __init__(self, values, columns, font, surface):
        self.values = values
        self.columns = columns
        self.font = font
        self.surface = surface
    def drawColumnLines(self):
        columns = len(self.columns)
        splits = width / (columns)
        col = ['' for i in range(columns)]
        for j in range(len(col)):
            col[j] = pygame.Rect(splits*(j+1), 50, 1.5,700)
            pygame.draw.rect(self.surface, (255,255,255), col[j])
    def drawColumnNames(self):
        columns = len(self.columns)
        splits = width / (columns)
        for j in range(len(self.columns)):
            if '\n' not in self.columns[j]:
                colText = self.font.render(str(self.columns[j]), False, (255,255,255))
                colRect = colText.get_rect()
                colRect.topleft = (splits*j + 2, 50)
                self.surface.blit(colText, colRect)
            else:
                split = self.columns[j].split('\n')
                colText1 = self.font.render(str(split[0]), False, (255,255,255))
                colRect1 = colText1.get_rect()
                colRect1.topleft = (splits*j + 2, 50)
                self.surface.blit(colText1, colRect1)
                colText2 = self.font.render(str(split[1]), False, (255,255,255))
                colRect2 = colText2.get_rect()
                colRect2.topleft = (splits*j + 2, 62)
                self.surface.blit(colText2, colRect2)
    def drawRowLines(self):
        rows = len(self.values)
        row = [''for i in range(rows)]
        for z in range(rows):
            row[z] = pygame.Rect(0, 82+14*(z), width, 1.5)
            pygame.draw.rect(self.surface, (255,255,255), row[z])
    def drawRowText(self):
        splits = width / len(self.columns)
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                valueText = self.font.render(str(self.values[i][j]), False, (255,255,255))
                valueRect = valueText.get_rect()
                valueRect.topleft = (splits*j + 2, 82 + 13*(i))
                self.surface.blit(valueText, valueRect)