from helpmodule import *
import notes

data = LoadDB(filenameMainDB, path)
notes.printNotes()
seichas()
printhelp()
print('Показываю отчёт за вчерашний день {0} и сегодняшний день [{1}]'.format(Vchera,Segodnya))
i=0
for d in data:
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
        if not 'nbl' in d: d['nbl']='' #для старых записей без nbl
        S = str(i) + '\t' + dayOrNight +': '+ d['date'] + ', ' + str(d['vrnh']).rjust(2,'0') + ':' + str(d['vrnm']).ljust(2,'0') + '-' + str(d['vrkh']).rjust(2,'0') + ':' + str(d['vrkm']).ljust(2,'0') + '\n\t\t' + str(getname(d['nst'])) +'\t'+ d['nbl'] +'\t' +d['podr'] + '.  ' + slojnost + ', ' + d['user'] + '.'
        print(S)


