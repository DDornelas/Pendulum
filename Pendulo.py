import matplotlib.pyplot as plt
import numpy as np
import math

def verlet(xt,vt):
   p=xt+vt*dt+0.5*((-w)*math.sin(xt)-gama*vt)*dt**2
   aux=((-w)*math.sin(p)-gama*vt)
   vaux=vt+0.5*(((-w)*math.sin(xt)-gama*vt)+aux)*dt
   aux=((-w)*math.sin(p)-gama*vaux)
   f=vt+0.5*((-w)*math.sin(xt)-gama*vt+aux)*dt
   return p,f

w=3
gama=0.5
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
   if t1<55:
      print "x=%f; v=%f; t=%f\n"%(xt1,vt1,t1)
   
plt.figure(figsize=(6,5), dpi=96)
plt.axis([0,55,-1.5,1])

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo(s)')
plt.ylabel(r'Posi\c{c}\~{a}o (m) e Velocidade($\frac{m}{s}$)')

plt.title(r'Pendulum Moviment', fontsize=12)
plt.grid()
plt.plot(t,x,'r-', linewidth=1, label="$x_{(t)}$")
plt.plot(t,v,'b-', linewidth=1, label="$v_{(t)}$")
plt.legend(loc='upper right')
plt.savefig("XxTVxT.pdf", dpi=96)
plt.show()
