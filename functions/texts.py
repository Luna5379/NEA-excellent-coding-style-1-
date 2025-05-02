from classes.text import text

def createText(textDetails):
    texts = text(textDetails[0], textDetails[1], textDetails[2], textDetails[3], textDetails[4])
    texts.drawText()