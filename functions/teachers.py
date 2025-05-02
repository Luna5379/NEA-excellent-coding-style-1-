import math

from assets.constants import *
from classes.table import *
from classes.importing import *
from functions.buttons import *

def drawRows(tableClass):
    tableClass.drawRowLines()
    tableClass.drawRowText()
def drawColumns(tableClass):
    tableClass.drawColumnLines()
    tableClass.drawColumnNames()
def drawTable(code, font, surface, cursor):
    values, columns = getTableData(code, cursor)
    tableClass = table(values, columns, font, surface)
    drawColumns(tableClass)
    drawRows(tableClass)
def getTableData(code, cursor):
    cursor.execute("""SELECT profile.Username AS Username,
                    COALESCE(classroomData.LastLessonTime, MAX(lessonsCompleted.DateCompleted)) AS LastLessonTime,
                    COALESCE(classroomData.CurrentTopic,(SELECT questions.Topic
                    FROM lessonsCompleted
                    JOIN lessonQuestions ON lessonsCompleted.LessonID = lessonQuestions.LessonID
                    JOIN questions ON lessonQuestions.QuestionID = questions.QuestionID
                    WHERE lessonsCompleted.Username = profile.Username
                    ORDER BY lessonsCompleted.DateCompleted DESC
                    LIMIT 1)) AS CurrentTopic,
                    SUM(lessonsCompleted.CorrectAnswers) + COALESCE(classroomData.TotalCorrectAnswers, 0) AS TotalCorrectAnswers,
                    (COALESCE((AVG(lessonsCompleted.Percentage) + classroomData.TotalPercentage)/2, AVG(lessonsCompleted.Percentage)) * 100) AS TotalPercentage,
                    SUM(lessonsCompleted.PointsGained) + COALESCE(classroomData.TotalPoints, 0) AS TotalPoints
                    FROM profile
                    LEFT JOIN lessonsCompleted ON lessonsCompleted.Username = profile.Username
                    LEFT JOIN classroomData ON classroomData.Username = profile.Username
                    WHERE profile.ClassroomCode = ? AND profile.Teacher = ?
                    GROUP BY profile.Username
                    ORDER BY TotalPoints DESC;""", [code, 0])
    values = cursor.fetchall()
    valuesList = []
    for i in range(len(values)):
        temp = []
        for j in range(len(values[i])):
            if type(values[i][j]) == float:
                temp.append(str(round(values[i][j], 0)) + '%')
            elif len(str(values[i][j])) == 10 and '-' in values[i][j]:
                tempo = ''
                for x in range(len(values[i][j])):
                    if values[i][j][x] == '-':
                        tempo += '.'
                    else:
                        tempo += values[i][j][x]
                temp.append(tempo)
            else:
                temp.append(values[i][j])
        valuesList.append(temp), 0
    columnNames = ["Username", "Last \nLesson", "Topic", "Correct \nAnswers", "Percentage", "Points"]
    return valuesList, columnNames
def importRules(importer, table, surface):
    if importer.active:
        rules = [f'Please add your file with external users to the "{uploadPath}" folder', 'Your file must be a .csv file that is comma delimited', 'You can add external users to "profile" and "classroomData" tables', 'If you want to add to the "profile" table, you must upload a "password" file FIRST', 'The password file must contain the password for each user on a separate line', 'the row number must correspond to the row of the profile data', 'the profile table consists of the following columns', 'Username VARCHAR(255) NOT NULL PRIMARY KEY', 'Email VARCHAR(255)', 'Name CHAR(25)', 'Gender CHAR(25)', 'DateOfBirth DATETIME', 'Phone CHAR(255)', 'Hash INT <-- Please replace with None', 'Teacher BIT', 'ClassroomCode INT', 'the classroomData table consists of the following columns', 'Username VARCHAR(255) NOT NULL', 'CurrentTopic VARCHAR(25)', 'TotalCorrectAnswers INT', 'TotalPercentage REAL', 'LastLessonTime DATETIME', 'You must upload separate files for each table', 'You must include the table name in the file name']
        importer.displayImportPage()
        importer.displayImportRules(rules)
        table = importData(importer, table)
        importer.active = createButton([(255,0,255), (0,0,0), (52.5, 675), 'CANCEL', surface, pygame.font.Font(buttonFont, 18), (120,120,120), width, (318,42)])
    return table
def importData(importing, table):
    records = importing.getFile()
    if len(records) == 0:
        importing.errorMessage()
    else:
        table = importing.importRecords(records, table)
        uploaded = importing.successMessage(records)
        importing.deleteFiles(records, uploaded)
    return table
def getCode(username, cursor):
    cursor.execute("""SELECT ClassroomCode FROM profile WHERE Username = ?""", [username])
    code = str(cursor.fetchone()[0])
    while len(code) < 4:
        code = str(0) + code
    return code