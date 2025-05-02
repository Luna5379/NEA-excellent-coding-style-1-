class text:
  def __init__(self, surface, font, text, colour, coords):
      self.surface = surface
      self.font = font
      self.text = text
      self.colour = colour
      self.coords = coords

  def drawText(self):
      textText = self.font.render(str(self.text), False, self.colour)
      textRect = textText.get_rect()
      textRect.topleft = (self.coords[0],self.coords[1])
      self.surface.blit(textText, textRect)