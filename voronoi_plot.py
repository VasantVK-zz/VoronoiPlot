from graphics import *
from random import *
from math import *

def colors(n):
	col = []
	for i in range(1, n+1):
		col.append(color_rgb(randint(0,255), randint(0,255), randint(0,255)))

	return col

def first_min(arr1):
	min1 = min(arr1)
	# print(min1)

	return min1

def second_min(arr2):
	new_list_min = arr2
	del new_list_min[new_list_min.index(min(new_list_min))]
	min2 = min(new_list_min)
	# print(min2)

	return min2

def min_index(x, y, list_points):
	list_min = []
	for i in list_points:
		dif_x = i.getX() - x
		dif_y = i.getY() - y
		c = sqrt(dif_y**2 + dif_x**2)
		# print(c)
		list_min.append(c)

	# print(list_min)
	return list_min


def sq_multiples(num):
	div_list = []
	for a in range(1, num+1):
		b = num % a
		if b == 0:
			div_list.append(a)

	if len(div_list) % 2 == 0:
		median = 2
	else:
		median = 1

	while len(div_list) != median:
		n = len(div_list)
		del div_list[n-1]
		del div_list[0]

	if median == 1:
		div_list.append(div_list[0])

	return div_list

def random_plot(sq_size, num_points = 1, bor_size = 0, alpha = 0):
	# try:
	win = GraphWin("Voronoi Diagram", sq_size, sq_size)
	list_points = []
	# grid = []
	# for l in range(1,3):
	# 	grid.append(Line(Point(l*(sq_size/num_points),0),Point(l*(sq_size/num_points),sq_size)))
	# 	grid.append(Line(Point(0,l*(sq_size/num_points)),Point(sq_size,l*(sq_size/num_points))))
	# for l_num in grid:
	# 	l_num.draw(win)
	spaceX = int(sq_size/sq_multiples(num_points)[0])
	spaceY = int(sq_size/sq_multiples(num_points)[1])
	x = 0
	y = 0
	initial = 0
	finalX = spaceX
	finalY = spaceY
	for i in range(1,num_points+1):
		list_points.append(Point(randint(initial+x,finalX+x),randint(initial+y,finalY+y)))
		# print(str(x) + ", " + str(y))
		if x < (sq_size-spaceX):
			x += spaceX
		else:
			y += spaceY
			x = 0
	
	# except ValueError:
	# 	print("Value error detected. Plot size must be divisble by the number of points.")

	# Voronoi plot
	list_colored_points = []
	color_list = colors(len(list_points))
	print(color_list)
	print(list_points)
	for intervalX in range(1, sq_size + 1):
		for intervalY in range(1, sq_size + 1):
			min_index_list = min_index(intervalX, intervalY, list_points)
			min_num_1 = first_min(min_index_list)
			min_index_1 = min_index_list.index(min_num_1)
			min_num_2 = second_min(min_index_list)
			min_dist = min_num_2 - min_num_1

			# win.plotPixel(intervalX, intervalY, color_list[min_index_1])

			# Border & Alpha Additions
			if min_dist > bor_size:
				win.plotPixel(intervalX, intervalY, color_list[min_index_1])
			else:
				win.plotPixel(intervalX, intervalY, "black")

			


	win.getMouse() # pause for click in window
	win.close()

def main():
	random_plot(500,10,10)

main()