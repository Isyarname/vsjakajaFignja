t = input('Введите цифры без пробелов\n')
n = int(input('Введите максимальную длину числа\n'))
pl = []
pa = []
pb = []
pc = []

for i in t:
	pl.append(i)
pl.sort()
pa = pl.copy()

for i in range(n):
	for a in range(len(pa)):
		for b in range(len(pl)):
			pb.append(pa[a] + pl[b])
	pc += pa
	pa = pb
	pb = []
	
text = ''
for c in pc:
	text += c+', '
print(text)
print('Количество чисел: '+str(len(pc)))