@@ -3,21 +3,37 @@ from random import *
from math import *

def colors(n):
	ret = []
	col = []
	for i in range(1, n+1):
		ret.append(color_rgb(randint(0,255), randint(0,255), randint(0,255)))
		col.append(color_rgb(randint(0,255), randint(0,255), randint(0,255)))

	return ret
	return col

def find_min(x, y, list_points):
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
		dif_x = i.getX()
		dif_y = i.getY()
		dif_x = i.getX() - x
		dif_y = i.getY() - y
		c = sqrt(dif_y**2 + dif_x**2)
		# print(c)
		list_min.append(c)

	return list_min.index(min(list_min))
	# print(list_min)
	return list_min


def sq_multiples(num):
@ -42,7 +58,7 @@ def sq_multiples(num):

	return div_list

def random_plot(sq_size, num_points = 1):
def random_plot(sq_size, num_points = 1, bor_size = 0, alpha = 0):
	# try:
	win = GraphWin("Voronoi Diagram", sq_size, sq_size)
	list_points = []
@ -73,14 +89,32 @@ def random_plot(sq_size, num_points = 1):

	# Voronoi plot
	list_colored_points = []
	color_list = colors(len(list_points))
	print(color_list)
	print(list_points)
	for intervalX in range(1, sq_size + 1):
		for intervalY in range(1, sq_size + 1):
			win.plotPixel(intervalX, intervalY, (colors(len(list_points))[find_min(intervalX, intervalY, list_points)]))
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
	random_plot(540,12)
	random_plot(500,10,10)

main()