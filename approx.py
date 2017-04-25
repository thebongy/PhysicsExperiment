from math import sin,cos,sqrt,pi
g = 10.0
ph=(pi/9)
l=1.0
h=0.39
def projRange(x):
    v = sqrt(2*g*l*(cos(x)-cos(ph)))
    t1 = v*cos(x)
    t2 = (v*sin(x))/g
    t3 = sqrt((2*((((v**2)*(sin(x)**2))/(2*g))+(l*(1-cos(x)))+h))/g)
    return t1*(t2+t3)

print projRange(0)
