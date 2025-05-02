import pygame
from classes.popUp import popUp
from functions.textboxes import *
from functions.buttons import createButton
from assets.constants import *
from functions.texts import createText

def createProfilePopUpBase(teacher, popDetails, code, box, pop):
    print(pop)
    if pop is None:
        pop = popUp(popDetails[0], popDetails[1], popDetails[2], popDetails[3], popDetails[4], popDetails[5], popDetails[6], popDetails[7], teacher)
    pop.openPopUp()
    if pop.popped:
        pop.drawPopUpOutline()
        pop.drawPopUpBase()
        if teacher:
            pop.displayPopUpData("Find your classroom code below", None)
            pop.userInput(code)
        else:
            pop.displayPopUpData("Enter your classroom code below!", 1)
            pop.displayPopUpData("If you don't have a classroom", 2)
            pop.displayPopUpData("Enter 0000", 3)
            box = fullTextBox([popDetails[17], popDetails[18], popDetails[19], popDetails[20], popDetails[21], popDetails[22], popDetails[23], popDetails[24]], box)
            print("heeeey")
    print(pop)
    return box if box else None, pop
def createProfilePopUp(teacher, popDetails, dataParams, username, surface, cursor, code = None, box=None, popUp = None):
    print(popUp)
    box, popUp = createProfilePopUpBase(teacher,popDetails, code, box, popUp)
    print("all fine")
    submit = createButton([popDetails[8], popDetails[9], popDetails[10], popDetails[11], popDetails[12], popDetails[13], popDetails[14], popDetails[15], popDetails[16]])
    print(dataParams[4])
    cursor.execute("""SELECT Username FROM profile WHERE ClassroomCode = ?;""", [box.text])
    codeExists = cursor.fetchall()
    if not submit and teacher:
        params = [str(dataParams[0]), str(dataParams[1]), str(dataParams[2]), str(dataParams[3]), int(dataParams[4]), int(1), int(code), str(username)]
        nextFunct = 'teacher'
    elif not submit:
        if codeExists is not None:
            params = [str(dataParams[0]), str(dataParams[1]), str(dataParams[2]), str(dataParams[3]), int(dataParams[4]), int(0), int(box.text), str(username)]
            nextFunct = 'timeline'
        else:
            createText([surface, pygame.font.Font(textFont, 22), 'Code does not exist', (255,0,0), (45,637)])
    elif teacher:
        print(popUp)
        return 'signup2', None, popUp
    else:
        print(popUp)
        return 'signup2', box, popUp
    if not submit:
        popUp.closePopUp()
        cursor.execute("""UPDATE profile
                    SET Name = ?, Email = ?, Gender = ?, DateOfBirth = ?, Phone = ?, Teacher = ?, ClassroomCode = ?
                    WHERE Username = ?;""", params)
    if box:
        print(popUp)
        return nextFunct, box, popUp
    else:
        print(popUp)
        return nextFunct, None, popUp

    