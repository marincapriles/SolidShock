import plotly.plotly as py #For plotting
from plotly.graph_objs import *
import plotly.tools as tls 
import numpy as np 

py.sign_in("marincapriles", "iq8fliwhr7") #Login to Plotly for plotting

materialA = raw_input("Enter material of left flyer")
materialB = raw_input("Enter material of right flyer")

PropA = []
PropB = []

PropFound = False

while PropFound == False:

	PropA = getProp(MaterialA)

	if PropA != [0,0,0]:
		PropFound = True

PropFound = False

while PropFound == False:

	PropA = getProp(MaterialB)

	if PropA != [0,0,0]:
		PropFound = True

u0 = 0

x1 = list(range(0,100,1))
y1 = []

def Hugoniot (rho0,c0,u1,u0,s):

	P = rho0*c0*(u1-u0)+rho0*s*((u1-u0)**(2.0))

	return P

for i in range(1,100):
	
	y1.append(Hugoniot(1,1,i,0,1))

trace = dict(x=x1,y=y1)

data = [trace]

py.plot(data,filename = "first")