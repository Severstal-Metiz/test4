print('Станы.')
print('1 - добавить вызов / заметка')
print('2 - показаать отчёт')
a=int(input('действие: '))
if a==1:
	import Stan_addInDB
elif a==2:
	import OtchetDB
else:
	print('Не коректный ввод!')	