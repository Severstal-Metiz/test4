import datetime
from helpmodule import *

data = LoadDB(filenameNoteDB, path)
deltaTreshold = 5

def hoursAndMinutes(string):
    dt = datetime.datetime.fromisoformat(string)
    return dt.hour, dt.minute, dt

def DelOrNot(stringDt):
    #stringDt = "2024-01-11 19:41:24.485892"
    _, _, dtn = hoursAndMinutes(stringDt)
    delta = dt.datetime.now() - dtn
    deltaHours = delta.total_seconds() / 60 / 60
    return deltaHours > deltaTreshold
def clearNotes():
    for i,d in enumerate(data):
        if DelOrNot(d['dt']):
            data[i] = 'DELETE'
    while 'DELETE' in data:
        data.remove('DELETE')

if len(data)!=0: clearNotes()

def printNotes():
    if len(data)==0: return
    s='ЗАМЕТКИ'
    for i,d in enumerate(data,1):
        h,m,dt = hoursAndMinutes(d['dt'])
        dt = dt.date()
        s = s + '\n' + 'N' + str(i)+ '\t\t'+ str(dt) +' ' + str(h).rjust(2,'0') + ':' + str(m).rjust(2,'0') + '\t' + d['text']
    print(s)
    print('----------')

def saveNote(text):
    d={}
    d['dt']=str(dt.datetime.now())
    d['text']=text
    data.append(d)
    SaveDB(data,filenameNoteDB,path)
#clearNotes()
#print(DelOrNot('2024-01-10 00:40:24.485892'))
#saveNote('Дурачо ккк к кк  к')
printNotes()