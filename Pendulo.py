import matplotlib.pyplot as plt
import numpy as np
import math
import getopt,sys

opcao,valor = getopt.getopt(sys.argv[1:],'g:w:')
for opcao,valor in opcao:
   if opcao =='-g':
      g = float (valor)
   if opcao == '-w':
      w = float (valor)

def verlet(xt,vt):
   p=xt+vt*dt+0.5*((-w)*math.sin(xt)-g*vt)*dt**2
   aux=((-w)*math.sin(p)-g*vt)
   vaux=vt+0.5*(((-w)*math.sin(xt)-g*vt)+aux)*dt
   aux=((-w)*math.sin(p)-g*vaux)
   f=vt+0.5*((-w)*math.sin(xt)-g*vt+aux)*dt
   return p,f

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
#plt.axis([0,10,-0.2,0.2])

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo(s)')
plt.ylabel(r'Posi\c{c}\~{a}o (m) eVelocidade($\frac{m}{s}$)')

plt.title(r'Pendulum Moviment Valores Diferentes de $\gamma$ e $\omega^{2}_{0}$', fontsize=12)
plt.grid()
plt.plot(t,x,'r-', linewidth=1, label="$x_{(t)}$")
plt.plot(t,v,'b-', linewidth=1, label="$v_{(t)}$")
plt.legend(loc='upper right')
plt.show()
