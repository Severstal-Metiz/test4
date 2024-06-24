from helpmodule import *
import notes

data = LoadDB(filenameMainDB, path)
notes.printNotes()
seichas()
printhelp()
srchstr = input('Введите строку для поиска в неисправностях: ')
print('Показываю отчёт со строкой поиска {0}'.format(srchstr))
i=0
for d in data:
    if srchstr in str(d['podr']):
        i=i+1
        if (d['vrnh']>=8 and d['vrnh']<20): dayOrNight = 'Дневная смена '
        else: dayOrNight = 'Ночная смена  '
        if (d['urs'] == 1): slojnost =      ' ОЧ ЛЕГКО'
        elif (d['urs'] == 2): slojnost =    '    ЛЕГКО'
        elif (d['urs'] == 3): slojnost =    'НОРМАЛЬНО'
        elif (d['urs'] == 4): slojnost =    '   СЛОЖНО'
        elif (d['urs'] == 5): slojnost =    'ОЧ СЛОЖНО'
        else: slojnost = 'ERROR'
        slojnost = '' # убрал из отчета
        if not 'nbl' in d: d['nbl']='' #для старых записей без nbl
        S = str(i) + '\t' + dayOrNight +': '+ d['date'] + ', ' + str(d['vrnh']).rjust(2,'0') + ':' + str(d['vrnm']).rjust(2,'0') + '-' + str(d['vrkh']).rjust(2,'0') + ':' + str(d['vrkm']).rjust(2,'0') + '\n\t\t' + str(getname(d['nst'])) +'\t'+ d['nbl'] +'\t' +d['podr'] + '.  ' + slojnost + ', ' + d['user'] + '.'
        print(S)


