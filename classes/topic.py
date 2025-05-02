import pygame

class topic:
    def __init__(self, topicName, topicNumber, lessons, completed, coords, topicColour, surface, font1, font2):
        self.topicName = topicName
        self.topicNumber = topicNumber
        self.lessons = lessons
        self.completed = completed
        self.coords = coords
        self.topicColour = topicColour
        self.surface = surface
        self.font1 = font1
        self.font2 = font2
    def drawTopicCircle(self):
        topicBase = pygame.Rect(self.coords[0], self.coords[1],150,150)
        pygame.draw.rect(self.surface,self.topicColour,topicBase, border_radius = 100)
        return topicBase
    def drawTopicIcon(self):
        iconText = self.font1.render(str(self.topicNumber), False, (255,255,255))
        iconRect = iconText.get_rect()
        iconRect.center = (self.coords[0]+75, self.coords[1]+75)
        self.surface.blit(iconText, iconRect)
    def maketopicPopUp(self, topicBase, selected):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and topicBase.collidepoint(pos):
            selected = True
        return selected
    def topicPopUpBase(self):
        tPop = pygame.Rect(self.coords[0]+155, self.coords[1], 180, 150)
        pygame.draw.rect(self.surface,self.topicColour,tPop, border_radius = 5)
    def topicPopUpText(self):
        headText = self.font2.render(str(self.topicNumber) + ': ' + str(self.topicName), False, (0,0,0))
        headRect = headText.get_rect()
        headRect.topleft = (self.coords[0]+170, self.coords[1]+20)
        self.surface.blit(headText, headRect)
        subText = self.font2.render(str(self.completed) + '/' + str(self.lessons), False, (0,0,0))
        subRect = subText.get_rect()
        subRect.topleft = (self.coords[0]+170, self.coords[1]+40)
        self.surface.blit(subText, subRect)
    def topicPopUpButton(self):
        lessonBase = pygame.Rect(self.coords[0]+170, self.coords[1]+100,160,30)
        pygame.draw.rect(self.surface,(255,255,255),lessonBase, border_radius = 10)
        lessonText = self.font2.render(str('START LESSON'), False, (0,0,0))
        lessonRect = lessonText.get_rect()
        lessonRect.topleft = (self.coords[0]+190, self.coords[1]+110)
        self.surface.blit(lessonText, lessonRect)
        return lessonBase
    def makeLessonStart(self, lessonBase):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and (lessonBase.collidepoint(pos)):
            startLesson = True
        else:
            startLesson = False
        return startLesson
    def fillTopic(self): #draw bigger circle below topic circle, fill with sector 
        pass
