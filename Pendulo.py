import matplotlib.pyplot as plt
import numpy as np
import math
import sys

def verlet(xt,vt):
   p=xt+vt*dt+0.5*((-w)*math.sin(xt)-(eval(sys.argv[1]))*vt)*dt**2
   aux=((-w)*math.sin(p)-(eval(sys.argv[1]))*vt)
   vaux=vt+0.5*(((-w)*math.sin(xt)-(eval(sys.argv[1]))*vt)+aux)*dt
   aux=((-w)*math.sin(p)-(eval(sys.argv[1]))*vaux)
   f=vt+0.5*((-w)*math.sin(xt)-(eval(sys.argv[1]))*vt+aux)*dt
   return p,f

w=3
xt1=1
vt1=0
dt=0.01
t1=0
x=[1]
v=[0]
t=[0]

while t1<60:
   t1+=dt
   xt1,vt1=verlet(xt1,vt1)
   x.append(xt1)
   v.append(vt1)
   t.append(t1)
   
plt.figure(figsize=(6,5), dpi=96)

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Posi\c{c}\~{a}o (m)')
plt.ylabel(r'Velocidade($\frac{m}{s}$)')

plt.title(r'Pendulum Moviment Espa\c{c}o de Fases $\gamma$=0,1', fontsize=12)
plt.grid()
plt.plot(x,v,'r-', linewidth=1)
plt.savefig("EFG01.pdf", dpi=96)
plt.show()
