import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def R(s,t,n):
  return -np.sin(t*np.log(n))/n**s

def L(s,t,n):
  return np.cos(t*np.log(n))/n**s

def zeta_real(s,t, m):
  return sum(L(s,t,n) for n in range(1,m+1))

def zeta_img(s,t,m):
  return sum(R(s,t,n) for n in range(1,m+1))

def zeta(s,t, m):
  return zeta_real(s,t,m)+1j*zeta_img(s,t,m)

#All vertical lines
Y = np.arange(-5, 5, 0.01)
pointsI = [(2,t) for t in Y]
domainI = [s+t*1j for (s,t) in pointsI]
RangeI = [zeta(s,t,100) for (s,t) in pointsI]
VX1 = np.array([x.real for x in domainI])
VY1 = np.array([x.imag for x in domainI])
ZVX1 = np.array([x.real for x in RangeI])
ZVY1 = np.array([x.imag for x in RangeI])

pointsII = [(3,t) for t in Y]
domainII = [s+t*1j for (s,t) in pointsII]
RangeII = [zeta(s,t,100) for (s,t) in pointsII]
VX2 = np.array([x.real for x in domainII])
VY2 = np.array([x.imag for x in domainII])
ZVX2 = np.array([x.real for x in RangeII])
ZVY2 = np.array([x.imag for x in RangeII])

pointsIII = [(4,t) for t in Y]
domainIII = [s+t*1j for (s,t) in pointsIII]
RangeIII = [zeta(s,t,100) for (s,t) in pointsIII]
VX3 = np.array([x.real for x in domainIII])
VY3 = np.array([x.imag for x in domainIII])
ZVX3 = np.array([x.real for x in RangeIII])
ZVY3 = np.array([x.imag for x in RangeIII])

pointsIV = [(1.5,t) for t in Y]
domainIV = [s+t*1j for (s,t) in pointsIV]
RangeIV = [zeta(s,t,100) for (s,t) in pointsIV]
VX4 = np.array([x.real for x in domainIV])
VY4 = np.array([x.imag for x in domainIV])
ZVX4 = np.array([x.real for x in RangeIV])
ZVY4 = np.array([x.imag for x in RangeIV])

pointsV = [(4/3,t) for t in Y]
domainV = [s+t*1j for (s,t) in pointsV]
RangeV = [zeta(s,t,100) for (s,t) in pointsV]
VX5 = np.array([x.real for x in domainV])
VY5 = np.array([x.imag for x in domainV])
ZVX5 = np.array([x.real for x in RangeV])
ZVY5 = np.array([x.imag for x in RangeV])


#All horizontal lines
X = np.arange(1.1, 10, 0.1)
points1 = [(s, 1) for s in X]
domain1 = [s+t*1j for (s,t) in points1]
HX1 = np.array([x.real for x in domain1])
HY1 = np.array([x.imag for x in domain1])
range1 = [zeta(s,t,100) for (s,t) in points1]
ZHX1 = np.array([x.real for x in range1])
ZHY1 = np.array([x.imag for x in range1])

points2 = [(s, 2) for s in X]
domain2 = [s+t*1j for (s,t) in points2]
HX2 = np.array([x.real for x in domain2])
HY2 = np.array([x.imag for x in domain2])
range2 = [zeta(s,t,100) for (s,t) in points2]
ZHX2 = np.array([x.real for x in range2])
ZHY2 = np.array([x.imag for x in range2])

points3 = [(s, 3) for s in X]
domain3 = [s+t*1j for (s,t) in points3]
HX3 = np.array([x.real for x in domain3])
HY3 = np.array([x.imag for x in domain3])
range3 = [zeta(s,t,100) for (s,t) in points3]
ZHX3 = np.array([x.real for x in range3])
ZHY3 = np.array([x.imag for x in range3])

points4 = [(s, 4) for s in X]
domain4 = [s+t*1j for (s,t) in points4]
HX4 = np.array([x.real for x in domain4])
HY4 = np.array([x.imag for x in domain4])
range4 = [zeta(s,t,100) for (s,t) in points4]
ZHX4 = np.array([x.real for x in range4])
ZHY4 = np.array([x.imag for x in range4])

points5 = [(s, 5) for s in X]
domain5 = [s+t*1j for (s,t) in points5]
HX5 = np.array([x.real for x in domain5])
HY5 = np.array([x.imag for x in domain5])
range5 = [zeta(s,t,100) for (s,t) in points5]
ZHX5 = np.array([x.real for x in range5])
ZHY5 = np.array([x.imag for x in range5])

#待編輯
# first set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(1, 10), ylim=(-5, 5))
lineI, = ax.plot([], [], lw=2)
lineII, = ax.plot([], [], lw=2)
lineIII, = ax.plot([], [], lw=2)
lineIV, = ax.plot([], [], lw=2)
lineV, = ax.plot([], [], lw=2)
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
line3, = ax.plot([], [], lw=2)
line4, = ax.plot([], [], lw=2)
line5, = ax.plot([], [], lw=2)


# initialization function: plot the background of each frame
def initI():
  lineI.set_data([], [])
  return lineI,
def initII():
  lineII.set_data([], [])
  return lineII,
def initIII():
  lineIII.set_data([], [])
  return lineIII,
def initIV():
  lineIV.set_data([], [])
  return lineIV,
def initV():
  lineV.set_data([], [])
  return lineV,
def init1():
  line1.set_data([], [])
  return line1,
def init2():
  line2.set_data([], [])
  return line2,
def init3():
  line3.set_data([], [])
  return line3,
def init4():
  line4.set_data([], [])
  return line4,
def init5():
  line5.set_data([], [])
  return line5,

# animation function.  this is called sequentially
def animateI(i):
  x = (i/100)*ZVX1 + (1-i/100)*VX1
  y = (i/100)*ZVY1 + (1-i/100)*VY1
  lineI.set_data(x, y)
  return lineI,
def animateII(i):
  x = (i/100)*ZVX2 + (1-i/100)*VX2
  y = (i/100)*ZVY2 + (1-i/100)*VY2
  lineII.set_data(x, y)
  return lineII,
def animateIII(i):
  x = (i/100)*ZVX3 + (1-i/100)*VX3
  y = (i/100)*ZVY3 + (1-i/100)*VY3
  lineIII.set_data(x, y)
  return lineIII,
def animateIV(i):
  x = (i/100)*ZVX4 + (1-i/100)*VX4
  y = (i/100)*ZVY4 + (1-i/100)*VY4
  lineIV.set_data(x, y)
  return lineIV,
def animateV(i):
  x = (i/100)*ZVX5 + (1-i/100)*VX5
  y = (i/100)*ZVY5 + (1-i/100)*VY5
  lineV.set_data(x, y)
  return lineV,

def animate1(i):
  x = (i/100)*ZHX1 + (1-i/100)*HX1
  y = (i/100)*ZHY1 + (1-i/100)*HY1
  line1.set_data(x, y)
  return line1,

def animate2(i):
  x = (i/100)*ZHX2 + (1-i/100)*HX2
  y = (i/100)*ZHY2 + (1-i/100)*HY2
  line2.set_data(x, y)
  return line2,

def animate3(i):
  x = (i/100)*ZHX3 + (1-i/100)*HX3
  y = (i/100)*ZHY3 + (1-i/100)*HY3
  line3.set_data(x, y)
  return line3,

def animate4(i):
  x = (i/100)*ZHX4 + (1-i/100)*HX4
  y = (i/100)*ZHY4 + (1-i/100)*HY4
  line4.set_data(x, y)
  return line4,

def animate5(i):
  x = (i/100)*ZHX5 + (1-i/100)*HX5
  y = (i/100)*ZHY5 + (1-i/100)*HY5
  line5.set_data(x, y)
  return line5,

aniI = FuncAnimation(fig, animateI, init_func=initI, frames=100, interval=100)
aniII = FuncAnimation(fig, animateII, init_func=initI, frames=100, interval=100)
aniIII = FuncAnimation(fig, animateIII, init_func=initI, frames=100, interval=100)
aniIV = FuncAnimation(fig, animateIV, init_func=initI, frames=100, interval=100)
aniV = FuncAnimation(fig, animateV, init_func=initI, frames=100, interval=100)
ani1 = FuncAnimation(fig, animate1, init_func=init1, frames=100, interval=100)
ani2 = FuncAnimation(fig, animate2, init_func=init2, frames=100, interval=100)
ani3 = FuncAnimation(fig, animate3, init_func=init3, frames=100, interval=100)
ani4 = FuncAnimation(fig, animate4, init_func=init4, frames=100, interval=100)
ani5 = FuncAnimation(fig, animate5, init_func=init5, frames=100, interval=100)

plt.show()