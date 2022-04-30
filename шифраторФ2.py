import sys

def aL():
	al = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
	return al

def inp():
	sch = input('1.шифр Цезаря\n2.атбаш\n3.перевернуть только слова\n4.перевернуть предложение\n')
	text = input('Введите текст\n')
	return(text, sch)

def f(sch):
	s = int(input('Введите сдвиг\n'))
	sc = input('1.шифровать  2.дешифровать\n')
	return(s, sc)

def revolution(text, tl, t, sch, i): #переворот
	if sch == '3': #слова
		for j in i:
			tl.append(j)
		for j in range(len(tl)):
			t += tl[len(tl)-1-j]
		tl = []
		t += ' '		
	elif sch == '4': #предложение
		tl.append(i)
	return(t, tl)

def cipferC(j, s, sc, al, t): #шифр Цезаря
	if sc == '1': #шифровать
		a = j + s 
	elif sc == '2': #дешифровать
		a = j - s
	t += al[a]
	return t

def cipferA(t, al, j): #атбаш
	t += al[len(al)-1-j]
	return t

def cipfer(text, t, al, sch, sc, s, i):
	for l in i:
		for j in range(len(al)):
			if l == al[j]:
				if sch == '1': #шифр Цезаря
					t = cipferC(j, s, sc, al, t)
				elif sch == '2': #атбаш
					t = cipferA(t, al, j)
	t += ' '
	return t


def main():
	al = aL()
	p = inp()
	t = ''
	tl = []
	text = p[0]
	sch = p[1]
	s = 0
	sc = 0
	if sch == '1':
		po = f(sch)
		s = po[0]
		sc = po[1]
	
	if sch != '4':
		text = text.split(' ')
		
	for i in text:
		if (sch == '1') or (sch == '2'):
			t = cipfer(text, t, al, sch, sc, s, i)	
		elif (sch == '3') or (sch == '4'):
			pos = revolution(text, tl, t, sch, i)
			tl = pos[1]
			t = pos[0]
			
	if sch == '4':
		for a in range(len(tl)):
			t += tl[len(tl)-1-a]
		
	print(t)

if __name__ == '__main__':
	sys.exit(main())