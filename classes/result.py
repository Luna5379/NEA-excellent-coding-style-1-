import math

class result:
    def __init__(self, surface, resultFont):
         self.surface = surface
         self.resultFont = resultFont
    def resultsText(self, percentage, totalPoints):
        rText1 = self.resultFont.render('percentage correct = ' + str(math.floor(100*percentage)) + '%', False, (0,0,255))
        rRect1 = rText1.get_rect()
        rRect1.topleft = (10,10)
        self.surface.blit(rText1, rRect1)
        rText2 = self.resultFont.render('total points = ' + str(totalPoints), False, (0,0,255))
        rRect2 = rText2.get_rect()
        rRect2.topleft = (10,30)
        self.surface.blit(rText2, rRect2)
