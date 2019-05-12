from random import randint
from pygame.locals import *
import sys, time, pygame

pygame.init()
DISPLAY=pygame.display.set_mode((800,800),0,32)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLACK=(0)

nums = [randint(0, 800) for x in range(100)]

def show(nums):
	global DISPLAY

	DISPLAY.fill(WHITE)

	for i in range(len(nums)):
		if i%2 == 0:
			pygame.draw.rect(DISPLAY, RED, [i*8, 800, 8, -nums[i]])
		else:
			pygame.draw.rect(DISPLAY, BLUE, [i*8, 800, 8, -nums[i]])

	pygame.display.update()

	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

def greater(n1, n2):
	return n1 > n2

def sort1_round(nums):
	'''
		Checks if number is greater, if so, reposition it
	'''
	for count in range(len(nums)-1):
		if greater(nums[count], nums[count+1]):
			x = nums[count]
			nums[count] = nums[count+1]
			nums[count+1] = x
	return nums

while True:
	nums = sort1_round(nums) 
