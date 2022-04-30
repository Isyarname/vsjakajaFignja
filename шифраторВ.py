al = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

sch = input('1.шифр Цезаря\n2.атбаш\n3.перевернуть только слова\n4.перевернуть предложение\n')

text = input('Введите текст\n')
t = ''
tl = []

if sch == '3':
	text = text.split()		
	for i in text:	
		for j in i:
			tl.append(j)				
		for j in range(len(tl)):
			t += tl[len(tl)-1-j]
		tl = []
		t += ' '
		
if sch == '4':
	for i in text:
		tl.append(i)
	for i in range(len(tl)):
		t += (tl[len(tl)-1-i])

if sch == '1': #для шифра Цезаря
		s = int(input('Введите сдвиг\n'))
		sc = input('1.шифровать  2.дешифровать\n')
		
if (sch == '1') or (sch == '2'):
	text = text.split(' ')
	for l in text:
		for i in l:
			for j in range(len(al)):
				if i == al[j]:
					if sch == '1': #шифр Цезаря
						if sc == '1': #шифровать
							a = j + s 
						elif sc == '2': #дешифровать
							a = j - s
						t += al[a]
					elif sch == '2': #атбаш
						t += al[len(al)-1-j]
		t += ' '
		
print(t)