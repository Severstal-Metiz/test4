import json
import os
from datetime import datetime as dt, timedelta as td
import helpmodule as hmd
#path='/storage/emulated/0/documents/станы/'
path=''
filename='DB.txt'

Segodnya = dt.now().date()
Vchera = dt.now().date() - td(days=1)

if os.stat(path+filename).st_size!=0:
    with open(path+filename) as file:
        J = json.load(file)
hmd.seichas()
hmd.printhelp()
print('Показываю отчёт за вчерашний день {0} и сегодняшний день [{1}]'.format(Vchera,Segodnya))
i=0
for d in J:
    if (str(d['date']) == str(Vchera) or str(d['date']) == str(Segodnya)):
        i=i+1
        if (d['vrnh']>=8 and d['vrnh']<20): dayOrNight = 'Дневная смена '
        else: dayOrNight = 'Ночная смена  '
        if (d['urs'] == 1): slojnost =      ' ОЧ ЛЕГКО'
        elif (d['urs'] == 2): slojnost =    '    ЛЕГКО'
        elif (d['urs'] == 3): slojnost =    'НОРМАЛЬНО'
        elif (d['urs'] == 4): slojnost =    '   СЛОЖНО'
        elif (d['urs'] == 5): slojnost =    'ОЧ СЛОЖНО'
        else: slojnost = 'ERROR'
        S = str(i) + '\t' + dayOrNight +': '+ d['date'] + ', ' + str(d['vrnh']).rjust(2,'0') + ':' + str(d['vrnm']).ljust(2,'0') + '-' + str(d['vrkh']).rjust(2,'0') + ':' + str(d['vrkm']).ljust(2,'0') + '\n\t\t' + str(hmd.getname(d['nst']))+ '\t' +d['podr'] + '.  ' + slojnost + ', ' + d['user'] + '.'
        print(S)


