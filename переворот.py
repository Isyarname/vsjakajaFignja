text = input('Введите текст\n')
t = []

for i in text:
	t.append(i)
	
text = ''

for i in range(len(t)):
	text += (t[len(t)-1-i])
	
print(text)