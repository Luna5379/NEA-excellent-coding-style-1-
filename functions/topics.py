import math

import pygame

from assets.constants import *
from classes.topic import topic

def getTopics(cursor):
    cursor.execute("""SELECT Topic from topics""")
    topics = []
    for i in cursor.fetchall():
        topics.append([i[0],False])
    return topics

def TopicData(topicName, username, topicColours, cursor):
    param = [username, topicName]
    cursor.execute("""SELECT topics.Position, COUNT(DISTINCT questions.Question), COUNT(DISTINCT lessonsCompleted.LessonID) 
        FROM topics 
        JOIN questions ON topics.Topic = questions.Topic 
        LEFT JOIN lessonQuestions ON questions.QuestionID = lessonQuestions.QuestionID 
        LEFT JOIN lessons ON lessonQuestions.LessonID = lessons.LessonID 
        LEFT JOIN lessonsCompleted ON lessons.LessonID = lessonsCompleted.LessonID AND lessonsCompleted.Username = ? 
        WHERE topics.Topic = ? 
        GROUP BY topics.Position""", param)
    data = cursor.fetchone()
    index = data[0]
    lessonNumber = math.floor(data[1]/10)
    completed = data[2]
    colourIndex = index % len(topicColours)
    return index, lessonNumber, completed, colourIndex

def createTopic(topicName, topicColours, selected, username, surface, cursor):
    index, lessonNumber, completed, colourIndex = TopicData(topicName, username, topicColours, cursor)
    currentTopic = topic(topicName, index, lessonNumber, completed, (20, index*102 + (index-1)*70), topicColours[colourIndex], surface, pygame.font.Font(textFont, 64), pygame.font.Font(textFont, 14))
    currentBase = currentTopic.drawTopicCircle()
    currentTopic.drawTopicIcon()
    selected = currentTopic.maketopicPopUp(currentBase, selected)
    if selected:
        currentTopic.topicPopUpBase()
        currentTopic.topicPopUpText()
        lessonButton = currentTopic.topicPopUpButton()
        startLesson = currentTopic.makeLessonStart(lessonButton)
        if startLesson:
            nextFunct = 'lesson'
        else:
            nextFunct = 'timeline'
    else:
        nextFunct = 'timeline'
    return nextFunct, topicName, selected
