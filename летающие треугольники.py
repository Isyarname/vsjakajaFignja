import pygame as p
import sys
from math import *
from screeninfo import get_monitors
from random import randint as r

clock = p.time.Clock()
p.init()
monitors = get_monitors()
while monitors == []: #так работает
	monitors = get_monitors()
fsc = False #полный экран
bullets = []
ts = []

class Triangle:
	def __init__(self, surf, width, height, x, y, vx, vy):
		self.time = 0
		self.w = width
		self.h = height
		self.depth = width // 200
		self.x = x
		self.y = y
		self.color = (100,255,255)
		self.motion = []
		self.surface = surf
		self.r = 1
		self.ra = 1
		self.g = 0.1
		self.vx = vx
		self.vy = vy

	def movement(self):
		dx = self.w / 2 - self.x
		dy = self.h / 2 - self.y
		self.ra = sqrt(dx * dx + dy * dy) + self.r
		self.vx += dx * self.g / self.ra
		self.vy += dy * self.g / self.ra
		self.x += self.vx
		self.y += self.vy

	def draw(self):
		self.movement()
		x = round(self.x)
		y = round(self.y)
		form = [(x, y-self.depth), (x-self.depth, y+self.depth+1), (x+self.depth, y+self.depth+1)]
		p.draw.polygon(self.surface, self.color, form)


def events(fsc, Width, Height):
	f = False
	for event in p.event.get():
		if event.type == p.MOUSEBUTTONDOWN:
			pos = event.pos
			#print(pos[0], pos[1])
			ts.append(Triangle(sc, Width, Height, pos[0], pos[1], 0, 5))
		if event.type == p.KEYDOWN:
			if event.key == p.K_f:
				fsc = not fsc
				f = True
			elif  event.key == p.K_ESCAPE:
				p.quit()
				sys.exit()
		elif event.type == p.QUIT:
			p.quit()
			sys.exit()
	return fsc, f

def start(fsc):
	if fsc:
		Width = monitors[0].width
		Height = monitors[0].height
		#print(Height)
		sc = p.display.set_mode((Width, Height), p.FULLSCREEN)
	else:
		Width = 100
		Height = 50
		sc = p.display.set_mode((Width, Height))
	return sc, Width, Height


s = start(fsc)
sc, Width, Height = s[0], s[1], s[2]
a = Width//2
b = Height//2
while True:
	sc.fill((0, 30, 40))
	e = events(fsc, Width, Height)
	if e[1]:
		s = start(e[0])
		sc, Width, Height = s[0], s[1], s[2]
	ts.append(Triangle(sc, Width, Height, r(0,Width), r(0,Height), 0, 5))
	for i in ts:
		i.draw()

	#print(len(bullets))

	clock.tick()
	p.display.set_caption(str(clock))
	p.display.update()
	p.display.flip()