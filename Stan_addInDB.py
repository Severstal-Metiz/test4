from helpmodule import *
confirm=''
seichas()
data = LoadDB(filenameMainDB, path)

while(confirm.upper() != 'Д'):
	printhelp()
	nst=int(input('номер стана / заметка '))
	print('>',getname(nst))
	nbl=input('блок/агрегат ')
	vrnh=int(input('   вызов в (указать час) '))
	vrnm=int(input('   вызов в (указать мин) '))
	vrkh=int(input('закончил в (указать час) '))
	vrkm=int(input('закончил в (указать мин) '))
	podr=input('неисправность ')
	urs=int(input('уровень сложности (1-5) '))
	confirm=input('Все верно? д - верно: ')
	if vrnh>23 or vrnh<0 or vrnm>59 or vrnm<0:
		print('ОШИБКА ВРЕМЯ НАЧАЛА')
		confirm=''
	elif vrkh>23 or vrkh<0 or vrkm>59 or vrkm<0:
		print('ОШИБКА ВРЕМЯ КОНЦА')
		confirm=''
	elif urs<1 or urs>5:
		print('ОШИБКА УРОВНЯ СЛОЖНОСТИ')
		confirm=''

d={'nst':nst,'vrnh':vrnh,'vrnm':vrnm,'vrkh':vrkh,'vrkm':vrkm,'urs':urs,'podr':podr,'date':date,'time':time,'user':user,'nbl':nbl}

data.append(d)

SaveDB(data, filenameMainDB, path)
