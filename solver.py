import plotly.plotly as py #For plotting
from plotly.graph_objs import *
import plotly.tools as tls 
import numpy as np 
import sympy as sy
import Functions as f
import sys

#Build material hugonoits dictionary
hugoniots = f.buildHugs()

#Ask user to input first material
materialA = input('Enter materialA\n-->').title()

#If material found as key, assign properties to variables
if materialA in hugoniots:
	rhoA = hugoniots[materialA][0]
	c0A = hugoniots[materialA][1]
	sA = hugoniots[materialA][2]
	qA = hugoniots[materialA][3]

else:
	print('materialA not found')
	sys.exit()

materialB = input('Enter materialB\n-->').title()

if materialB in hugoniots:
	rhoB = hugoniots[materialB][0]
	c0B = hugoniots[materialB][1]
	sB = hugoniots[materialB][2]
	qB = hugoniots[materialB][3]

else:
	print('materialB not found')
	sys.exit()

u0A = float(input('Initial velocity of A\n-->'))
u0B = float(input('Initial velocity of B\n-->'))

#Initialize sympy symbols for algebraic manipulation
hugA = sy.Symbol('hugA')
hugB = sy.Symbol('hugb')
u1 = sy.Symbol('u1')

hugA = rhoA*c0A*(u1-u0A)+rhoA*sA*(u1-u0A)**2
hugB = rhoB*c0A*(u0B-u1)+rhoB*sB*(u0B-u1)**2 #Left going Hugoniot

#Build x-axis vector
x1 = [] #Initialize 1-D list

RL = int(u0B*100)

for i in range(RL):

	x1.append(float(i/RL)) #Add entries from 0 to RL in 0.01 increments

y1 = [] #Initialize y-axis vector
y2 = []

for i in range(RL):
	
	y1.append(rhoA*c0A*(float(i/100)-u0A)+rhoA*sA*(float(i/100)-u0A)**2)
	y2.append(rhoB*c0B*(u0B-float(i/100))+rhoB*sB*(u0B-float(i/100))**2)

traceA = dict(x=x1,y=y1)
traceB = dict(x=x1,y=y2)

data = [traceA,traceB]

py.plot(data,filename = "first") 

#NEED: build x-t plot for collision

u1 = sy.solve(hugA-hugB,u1)
p1 = rhoA*c0A*(u1[0]-u0A)+rhoA*sA*(u1[0]-u0A)**2
ushock = c0A + sA*u1[0]

#Print results
print('The particle velocity after collision is \n',u1[0])
print('The pressure after collision is \n',p1)
print('The shock velocity after collision is \n',ushock)
