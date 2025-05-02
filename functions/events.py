import pygame
import sys

def events(textBoxes):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if textBoxes is not None:
        for box in textBoxes:
          if box is not None:
            box.checkClicked()
            box.handleTyping(event)