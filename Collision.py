
def PartSpeed(rho0,c0,s,u0):
	u = (u0*(c0+s*u0))/(2.0*(c0+u0))

	return u

def Press(rho0,c0,s,u0,u1):
	P = rho0*c0*(u1)+rho0*s*((u1)**(2.0))

	return P


def ShockSpeed(c0,s,u1):
	U = c0 + s*u1**2.0

	return U

