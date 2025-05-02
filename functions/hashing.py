import csv

from assets.constants import *

def hashTable(tablesize):
  table = [[] for i in range(tablesize)]
  tableCSV = open(hashPath, 'r')
  csvReader = csv.reader(tableCSV, delimiter= ',')
  for row in csvReader:
     idx = row[0]
     passy = row[1]
     idx = int(idx)
     table[idx] = [idx,passy]
  tableCSV.close()
  return table

def hashStore(passw, i, table):
   if table[i] == []:
      table[i] = [i, passw]
   else:
      while table[i] != []:
         i += hashInterval
         if i > tablesize:
            i = i % tablesize
      table[i] = [i, passw]
   return i

def encrypt(text): #should i do this before the hashing or after the hashing?
  coded = ''
  for i in range(len(text)):
    coded += chr(ord(text[i]) + 1)
  return coded

def msquare(tablesize, text): #exception handling: make it so you can't just enter, maybe have password length rules? if not make sure final index is at least 4 characters long
  passw = encrypt(text)
  hash = ''
  square = ''
  tableindex = 0
  for j in passw:
    hash += str(ord(j))
  square = str(int(hash) * int(hash))
  square = square[len(square)//2:(len(square)//2)+4]
  tableindex = (int(square))%tablesize
  return(passw, tableindex)

def hashUpdate(table):
   updateTable = open(hashPath, 'w', newline = '')
   tableWriter = csv.writer(updateTable, delimiter = ',')
   for i in range(len(table)-1):
      if table[i] != []:
         tableWriter.writerow(table[i])
   updateTable.close()

def match(i, passw, table, tablesize):
    inTable = False
    checked = False
    original = i
    if table[i] == [i, passw]:
        inTable = True
    while not inTable and not checked:
        i += hashInterval
        i %= tablesize
        if table[i] == [i, passw]:
            inTable = True
        if i == original:
            checked = True
    if inTable:
        return inTable, i
    else:
        return not checked, i