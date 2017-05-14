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

dados=open('g07w7.txt','w')

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

for i in range(len(t)):
	dados.write("%f %f %f\n"%(t[i],x[i],v[i]))
	
dados.close()
