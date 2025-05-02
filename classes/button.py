import pygame

class buttonNextPage:
  def __init__(self, boxcolour, textcolour, coords, text, surface, font, boxshadcolour, width, buttonsize):
    self.boxcolour = boxcolour
    self.textcolour = textcolour
    self.coords = coords
    self.text = text
    self.surface = surface
    self.font = font
    self.boxshadcolour = boxshadcolour
    self.width = width
    self.buttonsize = buttonsize

  def drawText(self):
    buttonText = self.font.render(str(self.text), False, self.textcolour)
    buttonRect = buttonText.get_rect()
    buttonRect.topleft = (self.width/2 - self.font.size(self.text)[0]/2, self.coords[1]+(self.buttonsize[1]+3.75-self.font.size(self.text)[1])/4)
    self.surface.blit(buttonText, buttonRect)
  
  def drawButton(self):
    buttonBase = pygame.Rect(self.coords[0]-15, self.coords[1]-3.75,self.buttonsize[0],self.buttonsize[1])
    pygame.draw.rect(self.surface,self.boxcolour,buttonBase, border_radius = 10)
    return buttonBase

  def drawShadow(self):
    buttonBaseShad = pygame.Rect(self.coords[0]-15, self.coords[1]+3.75,self.buttonsize[0],self.buttonsize[1])
    pygame.draw.rect(self.surface,self.boxshadcolour,buttonBaseShad, border_radius = 10)
    return buttonBaseShad

  def checkClicked(self,buttonBase,buttonBaseShad):
    pos = pygame.mouse.get_pos()
    click = True
    if pygame.mouse.get_pressed()[0] and (buttonBase.collidepoint(pos) or buttonBaseShad.collidepoint(pos)):
       click = False
    return click