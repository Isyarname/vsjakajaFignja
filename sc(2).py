al = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
sc = input('1.шифровать  2.дешифровать\n')
text = input('Введите текст\n')
text = text.split(' ')
s = int(input('Введите сдвиг\n'))
t = ''
	
for l in text:
	for i in l:
		for j in range(len(al)):
			if i == al[j]:
				if sc == '1':
					a = j + s 
				elif sc == '2':
					a = j - s
				t += al[a]
	t += ' '
	
print(t)