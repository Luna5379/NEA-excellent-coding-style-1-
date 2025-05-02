import re
import pygame

from assets.constants import *
from functions.texts import createText
from functions.textboxes import *
from functions.buttons import createButton
from functions.hashing import *
from functions.popups import *

def generateCode(cursor):
    cursor.execute("""SELECT MAX(ClassroomCode) FROM profile WHERE Teacher = 1""")
    codey = cursor.fetchone()
    if codey[0] == None:
        codeInt = 0
    else:
        codeInt = codey[0] + 1
    code = str(codeInt)
    while len(code) < 4: #exception handling, code not longer than 4
        code = '0' + code
    return code
def signup1(table, textBoxes,surface, cursor):
    if textBoxes == []:
        textBoxes = [None, None, None]
    surface.fill(color=bgColour)
    createText([surface, pygame.font.Font(headingFont, 32), 'Create your profile', (243,241,251), (45,98)])
    userBox = fullTextBox([(38,32,54), (189,174,232), (62,173), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[0], placeholder='Username')
    passBox = fullTextBox([(38,32,54), (189,174,232), (62,243), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[1],True,'Password')
    cpasBox = fullTextBox([(38,32,54), (189,174,232), (62,313), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[2], True, 'Confirm Password')
    next = createButton([(119,73,248), (38,32,54), (52.5, 387), 'CREATE ACCOUNT', surface, pygame.font.Font(buttonFont,18),(85,24,214), width, (318,42)])
    if userBox.text and passBox.text and cpasBox.text:
        cursor.execute("""SELECT Username FROM profile WHERE Username = ?""", [userBox.text])
        unique = cursor.fetchone()
        if unique == None:
            if passBox.text == cpasBox.text:
                if not next:
                    passw, i = msquare(tablesize, passBox.text)
                    i = hashStore(passw, i, table)
                    #exception handling usernames must be different
                    params = [str(userBox.text),None,None,None,None,None,i,None,None]
                    cursor.execute("""INSERT INTO profile
                                VALUES (?,?,?,?,?,?,?,?,?)""", params)
                    return 'signup2', table, userBox.text,[]
            else:
                createText([surface, pygame.font.Font(textFont, 22), 'Passwords do not match', (255,0,0), (45,450)])
        else:
            createText([surface, pygame.font.Font(textFont, 22), 'Username already exists', (255,0,0), (45,450)])
    else:
        createText([surface, pygame.font.Font(textFont, 22), 'Please fill in all fields', (255,0,0), (45,450)])
#elif passwords dont match
    return 'signup1', table, userBox.text,[userBox, passBox, cpasBox]
    
def signup2(table, textBoxes, popUp, username, surface, cursor):
    if textBoxes == []:
        textBoxes = [None, None, None,None,None, None]
    surface.fill(color=bgColour)
    createText([surface, pygame.font.Font(headingFont, 32), 'Fill in your details', (243,241,251), (45,98)])
    nameBox = fullTextBox([(38,32,54), (189,174,232), (62,173), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[0], placeholder='Name')
    mailBox = fullTextBox([(38,32,54), (189,174,232), (62,243), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[1], placeholder='Email')
    gendBox = fullTextBox([(38,32,54), (189,174,232), (62,313), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[2], placeholder='Gender')
    dateBox = fullTextBox([(38,32,54), (189,174,232), (62,383), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[3], placeholder='Date of Birth')
    phonBox = fullTextBox([(38,32,54), (189,174,232), (62,453), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[4], placeholder='Phone')
    student = createButton([(119,73,248), (38,32,54), (52.5,527), 'JOIN A CLASSROOM', surface, pygame.font.Font(buttonFont, 18), (85,24,214), width, (318,42)])
    teacher = createButton([(119,73,248), (38,32,54), (52.5,587), 'ARE YOU A TEACHER', surface, pygame.font.Font(buttonFont, 18), (85,24,214), width, (318,42)])
    if nameBox.text and mailBox.text and gendBox.text and dateBox.text and phonBox.text:
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', mailBox.text):
            createText([surface, pygame.font.Font(textFont, 22), 'Email must be valid', (255,0,0), (45,637)])
        else:
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', dateBox.text):
                createText([surface, pygame.font.Font(textFont, 22), 'Date must be in YYYY-MM-DD format', (255,0,0), (45,637)])
            else:
                if phonBox.text.isnumeric() == False:
                    createText([surface, pygame.font.Font(textFont, 22), 'Phone number must be a number', (255,0,0), (45,637)])
                else:
                    dataParams = [str(nameBox.text), str(mailBox.text), str(gendBox.text), str(dateBox.text), int(phonBox.text) if phonBox.text != '' else None]
                    if not teacher:
                        code = generateCode(cursor)
                        teacherPopUpData = [bgColour, surface, pygame.font.Font(textFont,24), (189,174,232), width, (343.875, 256.25), (28,32,54), pygame.font.Font(buttonFont, 96), (119,73,248), (38,32,54), (52.5,445), 'CONTINUE', surface, pygame.font.Font(buttonFont, 18), (85,24,214), width, (318,42)]
                        nextFunct, codeBox, popUp = createProfilePopUp(True,teacherPopUpData, dataParams, username,surface, cursor,code, popUp = None)
                    elif not student:
                        studentPopUpData = [bgColour, surface, pygame.font.Font(textFont, 22), (189,174,232), width, (343.875,256.25), (38,32,54), pygame.font.Font(buttonFont, 96), (119,73,248), (38,32,54), (52.5,445), 'CONTINUE', surface, pygame.font.Font(buttonFont, 18), (85,24,214), width, (318,42), (38,32,54), (189,174,232), (62.0625,363.3125), surface, pygame.font.Font(buttonFont, 80), (61,55,79), width, (298,80)]
                        nextFunct, codeBox, popUp = createProfilePopUp(False, studentPopUpData, dataParams, username,surface, cursor, box=textBoxes[5], popUp = None)
                    elif (popUp.popped if popUp is not None else False):
                        if popUp.teacher:
                            code = generateCode(cursor)
                            teacherPopUpData = [bgColour, surface, pygame.font.Font(textFont,24), (189,174,232), width, (343.875, 256.25), (28,32,54), pygame.font.Font(buttonFont, 96), (119,73,248), (38,32,54), (52.5,445), 'CONTINUE', surface, pygame.font.Font(buttonFont, 18), (85,24,214), width, (318,42)]
                            nextFunct, codeBox, popUp = createProfilePopUp(True,teacherPopUpData, dataParams, username,surface, cursor, code, popUp = popUp)
                        else:
                            studentPopUpData = [bgColour, surface, pygame.font.Font(textFont, 22), (189,174,232), width, (343.875,256.25), (38,32,54), pygame.font.Font(buttonFont, 96), (119,73,248), (38,32,54), (52.5,445), 'CONTINUE', surface, pygame.font.Font(buttonFont, 18), (85,24,214), width, (318,42), (38,32,54), (189,174,232), (62.0625,363.3125), surface, pygame.font.Font(buttonFont, 80), (61,55,79), width, (298,80)]
                            nextFunct, codeBox, popUp = createProfilePopUp(False, studentPopUpData, dataParams, username,surface, cursor, box=textBoxes[5], popUp = popUp)  
                    else:
                        nextFunct = 'signup2'
                        codeBox = None
                        popUp = None
                    if nextFunct == 'teacher' or nextFunct == 'timeline':
                        hashUpdate(table) 
                    if popUp is not None:
                        nameBox.typing = False
                        mailBox.typing = False
                        gendBox.typing = False
                        dateBox.typing = False
                        phonBox.typing = False
                    return nextFunct, table, [nameBox, mailBox, gendBox, dateBox, phonBox, codeBox], popUp
    else:
        createText([surface, pygame.font.Font(textFont, 22), 'Please fill in all fields', (255,0,0), (45,637)])
    return 'signup2', table, [nameBox, mailBox, gendBox, dateBox, phonBox, None], popUp