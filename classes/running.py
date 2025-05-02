import sys
import sqlite3

import pygame

from functions.hashing import *
from functions.topics import *
from assets.constants import *
from userinterface.frontPage import *
from userinterface.lesson import *
from userinterface.login import *
from userinterface.signup import *
from userinterface.teacher import *
from userinterface.timeline import *
from functions.events import *


class running:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("LingPro")
        self.surface = pygame.display.set_mode((width, height))
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()
        self.table = hashTable(tablesize)
        self.topicList = getTopics(self.cursor)
        self.username = None
        self.currentLesson = None
        self.nextFunct = "frontPage"
        self.textBoxes = []
        self.popUp = None
        self.question = None
        self.importing = None

        self.functionMap = {
            "frontPage": frontPage,
            "signup1": signup1,
            "signup2": signup2,
            "login": login,
            "timeline": timeline,
            "lesson": lesson,
            "teacher": teacher
        }

    def eventsHandle(self):
        events(self.textBoxes)
    def currentFunction(self):
        funct = self.functionMap.get(self.nextFunct, None)
        if funct == None:
            print(f"invalid function {self.nextFunct}")
            pygame.quit()
            sys.exit()
        if self.nextFunct == "frontPage":
            self.nextFunct = funct(self.surface)
        elif self.nextFunct == "signup1":
            self.nextFunct, self.table, self.username, self.textBoxes = funct(self.table, self.textBoxes, self.surface, self.cursor)
        elif self.nextFunct == "signup2":
            self.nextFunct, self.table, self.textBoxes, self.popUp = funct(self.table, self.textBoxes, self.popUp, self.username, self.surface, self.cursor)
            # if self.popUp is not None:                 
            #     self.textBoxes[5] = self.popUp[0]
            #     self.popUp = self.popUp[1]
        elif self.nextFunct == "login":
            self.nextFunct, self.username, self.textBoxes = funct(self.table, self.textBoxes, self.surface, self.cursor)
        elif self.nextFunct == "timeline":
            self.nextFunct, self.topicList, self.topic = funct(self.username, self.topicList, self.surface, self.cursor)
        elif self.nextFunct == "lesson":
            self.nextFunct, self.currentLesson, self.question = funct(self.topic, self.username, self.currentLesson, self.question, self.surface, self.cursor, self.connection)
        elif self.nextFunct == "teacher":
            self.nextFunct, self.table, self.importing = funct(self.username, self.table, self.importing, self.surface, self.cursor)
    def run(self):
        while True:
            self.eventsHandle()
            self.currentFunction()
            pygame.display.flip()
            self.connection.commit()