import json
import datetime as dt
import os
import helpmodule as hmd
#path='/storage/emulated/0/documents/станы/'
path=''
filename='DB.txt'
user='RomixERR'
confirm=''

hmd.seichas()

if os.stat(path+filename).st_size!=0:
    with open(path+filename) as file:
        data = json.load(file)

while(confirm.upper() != 'Д'):
	hmd.printhelp()
	nst=int(input('номер стана '))
	print('>',hmd.getname(nst))
	vrnh=int(input('   вызов в (указать час) '))
	vrnm=int(input('   вызов в (указать мин) '))
	vrkh=int(input('закончил в (указать час) '))
	vrkm=int(input('закончил в (указать мин) '))
	podr=input('неисправность ')
	urs=int(input('уровень сложности (1-5) '))
	#ustr=input('Устранил (д/н)')
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
date=hmd.date
time=hmd.time
d={'nst':nst,'vrnh':vrnh,'vrnm':vrnm,'vrkh':vrkh,'vrkm':vrkm,'urs':urs,'podr':podr,'date':date,'time':time,'user':user}

data.append(d)

with open(path+filename,'w') as file:
	json.dump(data,file)
