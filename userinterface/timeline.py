from assets.constants import *
from functions.topics import *

def timeline(username, topicList, surface, cursor):
    surface.fill(color=bgColour)
    for i in range(len(topicList)):
        nextFunct, topic, topicList[i][1] = createTopic(topicList[i][0], topicColours, topicList[i][1], username, surface, cursor)
    return nextFunct, topicList, topic