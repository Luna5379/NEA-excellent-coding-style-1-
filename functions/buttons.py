from classes.button import buttonNextPage

def createButton(buttonDetails):
   button = buttonNextPage(buttonDetails[0], buttonDetails[1],buttonDetails[2],buttonDetails[3], buttonDetails[4], buttonDetails[5],buttonDetails[6], buttonDetails[7], buttonDetails[8])
   bbs = button.drawShadow()
   bb = button.drawButton()
   button.drawText()
   click = button.checkClicked(bb,bbs)
   return click