import pygame

from assets.constants import *
from functions.hashing import *
from functions.texts import *
from functions.textboxes import *
from functions.buttons import *

def checkPassword(table, tablesize, password, username, cursor):
    passw, i = msquare(tablesize, password)
    params = [username]
    cursor.execute("""SELECT Hash FROM profile WHERE Username = ?;""", params)
    hash = cursor.fetchone()
    if hash != None:
        matching, i = match(i, passw, table, tablesize)
        if matching and i == hash[0]:
            return True
        else:
            return False
    else:
        return False

def teacherTimeline(username, cursor):
    params = [username]
    cursor.execute("""SELECT Teacher FROM profile WHERE Username = ?;""", params)
    teacherBool = cursor.fetchone()
    if teacherBool != None:
        teacherBit = teacherBool[0]
        if teacherBit == 1:
            return 'teacher'
        else:
            return 'timeline'
    else:
        return 'login'

def login(table, textBoxes, surface, cursor):
    if textBoxes == []:
        textBoxes = [None, None]
    surface.fill(color=bgColour)
    createText([surface, pygame.font.Font(headingFont, 32), 'Welcome Back', (243,241,251), (45,98)])
    userBox = fullTextBox([(38,32,54),(189,174,232),(62,173),surface,pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[0], placeholder='Username')
    passBox = fullTextBox([(38,32,54), (189,174,232), (62,243), surface, pygame.font.Font(textFont, 22), (61,55,79), width, (298,47)], textBoxes[1], True, 'Password')
    entered = createButton([(119,73,248), (38,32,54), (52.5,317), 'CONTINUE', surface, pygame.font.Font(buttonFont, 18), (85,24,214), width, (318,42)])
    if userBox.text and passBox.text:
        loggedin = checkPassword(table, tablesize, passBox.text, userBox.text, cursor)
        cursor.execute("""SELECT Username FROM profile WHERE Username = ?""", [userBox.text])
        exists = cursor.fetchone()
        if exists != None and loggedin:
            if not entered:
                if loggedin:
                    nextFunct = teacherTimeline(userBox.text, cursor)
                    textBoxes = None
                    return nextFunct, userBox.text, textBoxes
                else:
                    nextFunct = 'login'
                    textBoxes = [userBox, passBox]
                    return nextFunct, userBox.text, textBoxes
        else:
            createText([surface, pygame.font.Font(textFont, 22), 'Username or password incorrect', (255,0,0), (45,450)])
    else:
        createText([surface, pygame.font.Font(textFont, 22), 'Please fill in all fields', (255,0,0), (45,450)])
    nextFunct = 'login'
    textBoxes = [userBox, passBox]
    return nextFunct, userBox.text, textBoxes