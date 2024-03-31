import datetime as dt
import json
import os

#path='/storage/emulated/0/documents/станы/'
path=''
filenameMainDB= 'DB.txt'
filenameNoteDB= 'Note.txt'
user='RomixERR'

stand={46:'плющ',901:'травилка',902:'нейтрализация',903:'грубое/среднее',501:'FIB-1',502:'FIB-2',503:'FIB-3',1000:'Мокрое сволочение',1100:'Кц-1',1200:'Кц-2',2000:'Прочее'}

date=str(dt.date.today())
time=str(dt.datetime.now().time())
Segodnya = dt.datetime.now().date()
Vchera = dt.datetime.now().date() - dt.timedelta(days=1)

def seichas():
	wdn=['пн','вт','ср','чт','пт','сб','вс']
	weekday=wdn[dt.date.today().weekday()]
	print('дата: {0}, время: {1}, {2}'.format(date,time,weekday))


def printhelp():
	amc=20
	st='подсказка'
	stl=len(st)
	fmc=int((amc-stl)/2)
	st='='*fmc+st+'='*fmc
	print(st)
	for k,v in stand.items():
		print(v,k,end='\n')
	print('='*amc)

def getname(k):
	if k in stand:
		return stand[k]
	else: return str(k)

def LoadDB(filename, path=''):
	data=[]
	if os.stat(path + filename).st_size != 0:
		with open(path + filename) as file:
			data = json.load(file)
	return data

def SaveDB(data, filename, path=''):
	with open(path + filename, 'w') as file:
		json.dump(data, file)

if __name__=='__main__':
	seichas()
	printhelp()
	print('Это дополнительный модуль, он ничего не делает')

