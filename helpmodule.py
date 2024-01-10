import datetime as dt

stand={46:'плющ',901:'травилка',902:'нейтрализация',501:'FIB-1',502:'FIB-2',503:'FIB-3',1000:'Мокрое сволочение'}

date=str(dt.date.today())
time=str(dt.datetime.now().time())

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

print('Сделай так и больше нинаааааадааа. сделать оттельно блоки фиба доп ввод или станов на мокром. + редактор записей')

if __name__=='__main__':
	seichas()
	printhelp()
	print('Это дополнительный модуль, он ничего не делает')
