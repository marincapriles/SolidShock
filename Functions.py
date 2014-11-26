from sympy import Symbol 
import csv

def buildHugs():

	hugoniots = {}

	with open('cooper.csv', newline='') as cooper:

		csv_in = csv.reader(cooper)

		for line_list in csv_in:

			hugoniots[line_list[0]] = [float(line_list[1]),float(line_list[2]),float(line_list[3]),0]

			if line_list[0] in ('Calcium','Cesium','Chromium','Iron','Nylon','Silastic','Water'):
				hugoniots[line_list[0]][3] = float(line_list[4])

	return hugoniots
