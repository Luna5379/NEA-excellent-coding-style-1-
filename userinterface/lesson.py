import random

from classes.button import *
from assets.constants import *
from functions.questions import *

def generateLesson(Topic, cursor):
    lessonPercentage = 0
    qList = []
    cursor.execute("""SELECT MAX(LessonID) FROM lessonQuestions""")
    lastLesson = cursor.fetchone()[0]
    if lastLesson == None:
        currentLesson = 1
    else:
        currentLesson = lastLesson + 1
    cursor.execute("""INSERT INTO lessons VALUES (?,?)""", [currentLesson, None])
    while lessonPercentage < 1:
        cursor.execute("""SELECT MIN(QuestionID), MAX(QuestionID) FROM questions WHERE Topic = ?""", [Topic])
        minmaxQuestions = cursor.fetchone()
        minQuestions = minmaxQuestions[0]
        maxQuestions = minmaxQuestions[1]
        param1 = [random.randint(minQuestions,maxQuestions),Topic]
        cursor.execute("""SELECT QuestionID, LessonPercentage, Difficulty FROM questions WHERE QuestionID = ? AND Topic = ?""", param1)
        qidp = cursor.fetchone()
        if qidp[1] <= (1-lessonPercentage) and qidp[0] not in qList:
            lessonPercentage += qidp[1]
            print(lessonPercentage)
            qList.append(qidp[0])
            param2 = [currentLesson, qidp[0], qidp[2], None]
            cursor.execute("""INSERT INTO lessonQuestions VALUES(?,?,?,?)""",param2)
            lessonPercentage = round(lessonPercentage,2)
    cursor.execute("""SELECT SUM(DifficultyGroup) FROM lessonQuestions WHERE LessonID = ?""", [currentLesson])
    totalDifficulty = cursor.fetchone()[0]
    cursor.execute("""UPDATE lessons SET MaxPoints = ? WHERE lessonID = ?""", [totalDifficulty*5, currentLesson])
    return currentLesson

def lesson(Topic, username, currentLesson, question, surface, cursor, connection):
    print("wassa")
    currentQ = True
    if question is None:
        currentLesson = generateLesson(Topic, cursor)
    cursor.execute("""SELECT QuestionID FROM lessonQuestions WHERE LessonID = ? ORDER BY DifficultyGroup""", [currentLesson])
    qlist = [row[0] for row in cursor.fetchall()]
    print(qlist)
    if question is None:
        question = getQuestionClass(surface, qlist[0], [], pygame.font.Font(headingFont, 18), pygame.font.Font(textFont, 14), connection, cursor)
        question.reset()
    print(currentLesson)
    if question.firstRound:
        question.nextQuestion()
        question.getOrder()
        question.params = [qlist[question.q-1] if question.q-1 < len(qlist) else 0]
    if question.q > len(qlist):
        finished = True
        currentQ = False
    else:
        finished = False
    if currentQ:
        question.nextQ, currentQ = makeQuestion(currentQ, question.nextQ, question, qlist[question.q-1], surface, cursor)
        print("q made")
    if not question.nextQ:
        question.firstRound = True
    if finished:
        nextFunct, question = displayResultsPage(currentLesson, username, question, surface, cursor)
        
    else:
        nextFunct = 'lesson'
        #question = None
    return nextFunct, currentLesson, question