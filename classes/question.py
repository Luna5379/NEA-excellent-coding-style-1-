import pygame
import random

from assets.constants import *

class q1: #first type, what does this command do?
    def __init__(self, surface, params, order, questionFont, optionFont, connection, cursor):
        self.surface = surface
        self.params = params
        self.order = order
        self.questionFont = questionFont
        self.optionFont = optionFont
        self.nextQ = False
        self.selected = [False,False,False,False]
        self.submitted = True
        self.firstRound = True
        self.q = 0
        self.connection = connection
        self.cursor = cursor
    def reset(self):
        self.nextQ = False
        self.selected = [False,False,False,False]
        self.submitted = True
        self.firstRound = True
        self.q = 0
    def nextQuestion(self):
        self.q += 1
        self.selected = [False,False,False,False]
        self.submitted = True
        self.firstRound = False
        self.nextQ = True
    def getOrder(self):
        self.order = random.sample(range(1,5), 4)
    def getQuestion(self):
        print(self.params)
        self.cursor.execute("""SELECT Question, Example FROM questions WHERE QuestionID = ?;""",self.params)
        question = self.cursor.fetchone()
        print(question)
        self.connection.commit()
        return question[0], question[1]
    def getOptions(self):
        self.cursor.execute("""SELECT questions.Answer, options.Option FROM questions INNER JOIN options ON questions.QuestionID = options.QuestionID WHERE questions.QuestionID = ?;""",self.params)
        options = self.cursor.fetchall()
        answerOptions = [options[0][1],options[1][1],options[2][1]]
        return options[0][0], answerOptions
    def drawQuestion(self, question): #print question onto page
        qText = self.questionFont.render(question, False, (255,0,0))
        qRect = qText.get_rect()
        qRect.topleft = (10, 10)
        self.surface.blit(qText, qRect)
    def drawExample(self, example):
        eText = self.questionFont.render("eg. " + str(example), False, (0,255,0))
        eRect = eText.get_rect()
        eRect.topleft = (10, 30)
        self.surface.blit(eText, eRect)
    def getOptionsPositions(self, answer, options): #print options onto page
        allOps = [answer, options[0], options[1], options[2]]
        allOpsOrdered = ['' for i in range(4)]
        coords = [[] for i in range(4)]
        for i in range(4):
            allOpsOrdered[i] = allOps[self.order[i]-1]
            coords[i] = [6, 200+i*120]
        return coords, allOpsOrdered
    def selectedOption(self, coords):
        for i in range(4):
            if self.selected[i]:
                    shadowBase = pygame.Rect(coords[i][0]-2.5,coords[i][1]-2.5, 385, 105)
                    pygame.draw.rect(self.surface, (132,132,132), shadowBase, border_radius = 10)
    def drawOptionBase(self, coords):
        optionBase = ['' for i in range(4)]
        for i in range(4):
            optionBase[i] = pygame.Rect(coords[i][0],coords[i][1], 380, 100)
            pygame.draw.rect(self.surface, (255,255,255), optionBase[i], border_radius = 10)
        return optionBase
    def drawOptionText(self, coords, allOpsOrdered):
        optionText = ['' for i in range(4)]
        optionRect = ['' for i in range(4)]
        for i in range(4):
            optionText[i] = self.optionFont.render(str(allOpsOrdered[i]), False, (0,0,255))
            optionRect[i] = optionText[i].get_rect()
            optionRect[i].topleft = (coords[i][0] + 10, coords[i][1] + 10)
            self.surface.blit(optionText[i], optionRect[i])
    def selectOptions(self, optionBase): #check if the user clicked the right answer, show result
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and (optionBase[0].collidepoint(pos) or optionBase[1].collidepoint(pos) or optionBase[2].collidepoint(pos) or optionBase[3].collidepoint(pos)):
            for i in range(len(optionBase)):
                if optionBase[i].collidepoint(pos):
                    self.selected[i] = True
                    for j in range(len(self.selected)):
                        if j!=i:
                            self.selected[j] = False
    def checkSubmitted(self, optionText, answer):
        if True in self.selected:
            for i in range(len(self.selected)):
                if self.selected[i]:
                    selectedIndex = i
            if optionText[selectedIndex] == answer:
                return True
            else:
                return False
        else:
            return False
    def resultPopUp(self, correct):
        if correct:
            colour = (0,255,0)
            text = str('Correct!')
        else:
            colour = (255,0,0)
            text = str('Incorrect!')
        result = pygame.Rect(37.5,525, 318, 200)
        pygame.draw.rect(self.surface, colour, result, border_radius = 10)
        resultText = self.questionFont.render(text, False, (0,0,255))
        resultRect = resultText.get_rect()
        resultRect.topleft = (196.5/2 + 52.5 - self.questionFont.size('Correct!')[0]/2, 525 + (100+3.75-self.questionFont.size('Correct!')[1])/4)
        self.surface.blit(resultText, resultRect)
        return colour