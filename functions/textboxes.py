from classes.textBox import textBox

def createTextBox(textBoxDetails, box, password):
    print(box)
    if box is None:
        print("box is None")
        box = textBox(textBoxDetails[0], textBoxDetails[1], textBoxDetails[2], textBoxDetails[3], textBoxDetails[4], textBoxDetails[5], textBoxDetails[6], textBoxDetails[7], password)
    box.drawOutline()
    box.drawBox()
    box.checkClicked()
    print("no problems?")
    return box

# def clickTextBox(box, boxBase, boxID):
#     clicked = box.checkClicked(boxBase)
#     if clicked:
#         typeCheck[str('type'+boxID)] = True
#         keys = [key for key, val in textBools.items() if val == True]
#         for i in range(len(keys)):
#             textBools[keys[i]] = False
#         textBools['getText'+boxID] = True

def typeTextBox(box): 
    box.drawText()

def fullTextBox(textBoxDetails, box, password=False, placeholder = ''):
    #print("you are in fullTextBox")
    box = createTextBox(textBoxDetails, box, password)
    box.placeholder = placeholder
    #clickTextBox(box,boxBase, boxID)
    typeTextBox(box)
    print("no more problems?")
    return box

# def runTextBox(textBoxDetails, placeholder): ### if time left over/feel like it
#     box, boxBase = createTextBox([(38,32,54), (189,174,232), (62,453), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)])
#     clickTextBox(s21,s21b)
#     typeTextBox('Username', s21)