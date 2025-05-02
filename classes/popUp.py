import pygame
class popUp:
    def __init__(self, popUpColour, surface, font, outline, width, popUpSize, inputColour, codeFont, teacher):
        self.popUpColour = popUpColour
        self.surface = surface
        self.font = font
        self.outline = outline
        self.width = width
        self.popUpSize = popUpSize
        self.inputColour = inputColour
        self.codeFont = codeFont
        self.popped = False
        self.teacher = teacher
    def drawPopUpBase(self):
      if self.popped:
        popUpBase = pygame.Rect(196.5-self.popUpSize[0]/2, 183+self.popUpSize[1]/4,self.popUpSize[0],self.popUpSize[1])
        pygame.draw.rect(self.surface,self.popUpColour,popUpBase, border_radius = 5)
    def drawPopUpOutline(self):
      if self.popped:
        outlineBase = pygame.Rect(196.5-self.popUpSize[0]/2-2, 183+self.popUpSize[1]/4-2,self.popUpSize[0]+4,self.popUpSize[1]+4)
        pygame.draw.rect(self.surface,self.outline,outlineBase, border_radius = 5)
    def displayPopUpData(self, text, position):
      if self.popped:
        if position == None:
          popText = self.font.render(str(text), False, self.outline)
          popRect = popText.get_rect()
          popRect.topleft = (196.5-self.popUpSize[0]/2+3, 183+self.popUpSize[1]/4+6)
          self.surface.blit(popText, popRect)
        else:
          popText = self.font.render(str(text), False, self.outline)
          popRect = popText.get_rect()
          popRect.topleft = (196.5-self.popUpSize[0]/2+3, 183+self.popUpSize[1]/4+6+35*(position-1))
          self.surface.blit(popText, popRect)
    def userInput(self, code):
      outline = ['' for j in range(4)]
      box = ['' for b in range(4)]
      codeText = ['' for c in range(4)]
      cRect = ['' for d in range(4)]
      if self.popped:
        for i in range(4):
          outline[i] = pygame.Rect(196.5-(self.popUpSize[0]/2)+22.5+75*(i), 183+self.popUpSize[1]/4+77.5,70,125)
          pygame.draw.rect(self.surface,self.outline,outline[i],border_radius = 5)
          box[i] = pygame.Rect(196.5-(self.popUpSize[0]/2)+25+(75*(i)), 183+self.popUpSize[1]/4+80,65,120)
          pygame.draw.rect(self.surface,self.inputColour,box[i],border_radius = 5)
          codeText[i] = self.codeFont.render(str(code[i]), False, self.outline)
          cRect[i] = codeText[i].get_rect()
          cRect[i].topleft = (196.5-(self.popUpSize[0]/2)+30+(75*(i)), 183+self.popUpSize[1]/4+100)
          self.surface.blit(codeText[i], cRect[i])
    def openPopUp(self):
      self.popped = True
    def closePopUp(self):
      self.popped = False 