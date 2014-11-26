import Collision 
#from sympy import *


#Get variables to build Hugoniots
rho0 = float(input("Enter the initial density rho: ")) #2.785
c0 = float(input("Enter C0: ")) #5.328
s = float(input("Enter s: ")) #1.338
u0 = float(input("Enter the initial velocity of slab A: ")) #1.0

u1 = Collision.PartSpeed(rho0,c0,s,u0)
