import pygame

class textBox:
  def __init__(self, boxColour, colour, coords, surface, font, outline, width, buttonsize, password):
    self.boxColour = boxColour
    self.colour = colour
    self.coords = coords
    self.surface = surface
    self.font = font
    self.outline = outline
    self.width = width
    self.buttonsize = buttonsize
    self.text = ''
    self.typing = False
    self.base = None
    self.placeholder = ''
    self.password = password
  
  def drawBox(self):
    self.base = pygame.Rect(self.coords[0]-15, self.coords[1]-3.75,self.buttonsize[0],self.buttonsize[1])
    pygame.draw.rect(self.surface,self.boxColour,self.base, border_radius = 5)
  
  def drawText(self):
    displayText = self.text if self.text or self.typing else self.placeholder
    if self.password and (self.text or self.typing):
      displayText = '*' * len(self.text)
    buttonText = self.font.render(str(displayText), False, self.colour)
    buttonRect = buttonText.get_rect()
    buttonRect.topleft = (self.coords[0]-7.5, self.coords[1]+6)
    self.surface.blit(buttonText, buttonRect)

  def drawOutline(self):
    buttonBase = pygame.Rect(self.coords[0]-17.25, self.coords[1]-7,self.buttonsize[0]+5,self.buttonsize[1]+5)
    pygame.draw.rect(self.surface,self.outline,buttonBase, border_radius = 5)
  
  def checkClicked(self):
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] and self.base.collidepoint(pos):
      self.typing = True
    elif pygame.mouse.get_pressed()[0] and not self.base.collidepoint(pos):
      self.typing = False

  def handleTyping(self, event):
    if self.typing:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
          self.text = self.text[:-1]
        else:
          self.text += event.unicode