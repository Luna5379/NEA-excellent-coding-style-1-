import datetime
import random
import math

from classes.question import *
from functions.buttons import *
from assets.constants import *
from classes.result import *


def drawQ(questionClass, surface):
    surface.fill(color=bgColour)
    print("surface filled")
    q, ex = questionClass.getQuestion()
    print("question got")
    questionClass.drawQuestion(q)
    questionClass.drawExample(ex)
    print("question drawn")
    ans, ops = questionClass.getOptions()
    print("options got")
    coords, allOpsOrdered = questionClass.getOptionsPositions(ans, ops)
    print("options positions got")
    questionClass.selectedOption(coords)
    print("selected option")
    optionBase = questionClass.drawOptionBase(coords)
    questionClass.drawOptionText(coords, allOpsOrdered)
    print("option text drawn")
    questionClass.selectOptions(optionBase)
    if questionClass.submitted:
        questionClass.submitted = createButton([(0,255,0), (0,0,0), (52.5,725), 'SUBMIT', surface, pygame.font.Font(buttonFont, 18), (120,120,120), width, (318,42)])
    return allOpsOrdered, ans, questionClass

def drawResultsPopUp(questionClass, allOpsOrdered, answer, questionID, currentQ, surface, cursor):
    correct = questionClass.checkSubmitted(allOpsOrdered, answer)
    colour = questionClass.resultPopUp(correct)
    nextQ = createButton([colour, (0,0,0), (52.5,675), 'NEXT', surface, pygame.font.Font(buttonFont, 18), (120,120,120), width, (318,42)])
    if not nextQ:
        cursor.execute("""UPDATE lessonQuestions SET CORRECT = ? WHERE questionID = ?""", [1 if correct else 0, questionID])
        currentQ = False
        return False, currentQ
    else:
        return True, currentQ

def makeQuestion(currentQ, nextQ, questionClass, questionID, surface, cursor):
    print("wowzers")
    allOpsOrdered, answer, questionClass = drawQ(questionClass, surface)
    print("qdrawn")
    if not questionClass.submitted:
        nextQ, currentQ = drawResultsPopUp(questionClass, allOpsOrdered, answer, questionID, currentQ, surface, cursor)
    return nextQ, currentQ

def getResults(lessonID, username, cursor):
    dateCompleted=datetime.date.today()
    cursor.execute("""SELECT AVG(lessonQuestions.Correct), lessons.MaxPoints, SUM(lessonQuestions.Correct) FROM lessonQuestions INNER JOIN lessons ON lessonQuestions.LessonID = lessons.LessonID WHERE lessonQuestions.LessonID = ?""", [lessonID])
    results = cursor.fetchone()
    percentage = round(results[0], 2)
    totalPoints = math.floor((percentage)*results[1])
    totalCorrect = results[2]
    try:
        cursor.execute("""INSERT INTO lessonsCompleted VALUES(?,?,?,?,?,?)""", [lessonID, dateCompleted, totalPoints, percentage, totalCorrect, username])
    except:
        pass
    return percentage, totalPoints

def displayResultsPage(lessonID, username, questionClass, surface, cursor):
    surface.fill(color= bgColour)
    percentage, totalPoints = getResults(lessonID, username, cursor)
    drawResult(percentage, totalPoints, surface)
    returnTimeline = createButton([(255,255,0), (0,0,0), (52.5,725), 'RETURN TO TIMELINE', surface, pygame.font.Font(buttonFont, 18), (140,120,60), width, (318,42)])
    if not returnTimeline:
        return 'timeline', None
    else:
        return 'lesson', questionClass

def getQuestionClass(surface, questionID, order, questionFont, optionFont, connection, cursor):
    questionClass = q1(surface, [questionID], order, questionFont, optionFont, connection, cursor)
    return questionClass

def drawResult(percentage, totalPoints, surface):
    results = result(surface, pygame.font.Font(headingFont, 18))
    results.resultsText(percentage, totalPoints)