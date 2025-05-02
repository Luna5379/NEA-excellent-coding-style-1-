from functions.teachers import *
from functions.texts import *
from assets.constants import *
from functions.buttons import *

def tablePage(importer, username, surface, cursor):
    if not importer.active:
        code = getCode(username, cursor)
        createText([surface, pygame.font.Font(headingFont, 30), str('Admin for class: ' + code), (243,241,251), (5,10)])
        drawTable(int(code), pygame.font.Font(textFont, 13), surface)
        importer.active = not createButton([(119,73,248), (38,32,54), (37.5, 755), 'IMPORT EXTERNAL USERS', surface, pygame.font.Font(buttonFont, 18), (85,24,214), width, (318,42)])
def teacher(username, table, importer, surface, cursor):
    surface.fill(color=bgColour)
    if importer == None:
        importer = importing(pygame.font.Font(textFont, 13), surface)
    tablePage(importer, username, surface, cursor)
    table = importRules(importer, table)
    return 'teacher', table, importer