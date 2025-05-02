import csv
import os

import pygame

from assets.constants import *
from functions.hashing import *

class importing:
    def __init__(self, font, surface, cursor):
        self.font = font
        self.surface = surface
        self.cursor = cursor
        self.active = False
    def getFile(self):
        uploadContents = []
        for root, dirs, files in os.walk('upload'):
            for file in files:
                if file[-4:] == '.csv' and (('classroomData' in file) ^ ('profile' in file) ^ ('password' in file)):
                    if 'password' in file:
                        uploadContents.append([file, 'password', False])
                    elif 'classroomData' in file:
                        uploadContents.append([file, 'classroomData', False])
                        print("yoohoo")
                    else:
                        uploadContents.append([file, 'profile', False])
                        print("big summer blowout")
        uploadContents.sort(key = lambda item: 0 if item[1] == 'password' else 1)
        return uploadContents
    def importRecords(self, uploadContents, table, cursor):
        processProfiles = False
        passExists = any(file[1] == 'password' for file in uploadContents)
        profExists = any(file[1] == 'profile' for file in uploadContents)
        if passExists and profExists:
            processProfiles = True
        for filey in uploadContents:
            print(filey)
            if filey[2] == False:
                fileo = os.path.join(uploadPath,str(filey[0]))
                print(fileo)
                with open(fileo, "r") as file:
                    if filey[1] == 'classroomData':
                        for index,row in enumerate(csv.reader(file)):
                            try:
                                cursor.execute("""INSERT INTO classroomData VALUES (?,?,?)""", [filey[1], *row])
                            except:
                                pass
                        filey[2] = True
                    elif filey[1] == 'password' and processProfiles:
                        print("yipee")
                        for index,row in enumerate(csv.reader(file)):
                            passw, i = msquare(tablesize, row)
                            i = hashStore(passw, i, table)
                        hashUpdate(table)
                        filey[2] = True
                    elif filey[1] == 'profile' and processProfiles:
                        print("gidagidigidagidago")
                        for index, row in enumerate(csv.reader(file)):
                            try:
                                cursor.execute("""INSERT INTO profile VALUES (?,?,?,?,?,?,?,?,?)""", [*row])
                                cursor.execute("""UPDATE profile SET Hash = ? WHERE Username = ?""", [i, row[0]])
                            except:
                                pass
                        filey[2] = True
        return table
    def deleteFiles(self, uploadContents, uploaded):
        if uploaded:
            for file in uploadContents:
                filePath = os.path.join(uploadPath,str(file[0]))
                os.remove(filePath)
        else:
            for file in uploadContents:
                filePath = os.path.join(uploadPath,str(file[0]))
                if file[2] == True and file[1] == 'classroomData':
                    os.remove(filePath)
    def errorMessage(self):
        errorText = self.font.render(str('There are no valid files in the folder'), False, (255,0,0))
        errorRect = errorText.get_rect()
        errorRect.topleft = (2, 500)
        self.surface.blit(errorText, errorRect)
    def successMessage(self,uploadContents):
        numUploaded = 0
        for filey in uploadContents:
            if filey[2] == True:
                numUploaded += 1
        if numUploaded == len(uploadContents):
            successText = self.font.render(str('Upload successful!'), False, (0,255,0))
            successRect = successText.get_rect()
            successRect.topleft = (2, 450)
            self.surface.blit(successText, successRect)
            return True
        else:
            return False
    def displayImportRules(self, rules):
        ruleText = ['' for i in range(len(rules))]
        ruleRect = ['' for z in range(len(rules))]
        for j in range(len(rules)):
            ruleText[j] = self.font.render(str(rules[j]), False, (0,0,0))
            ruleRect[j] = ruleText[j].get_rect()
            ruleRect[j].topleft = (2, 15*j)
            self.surface.blit(ruleText[j], ruleRect[j])
    def displayImportPage(self):
        bgCol = (119,73,248)
        self.surface.fill(color=bgCol)
