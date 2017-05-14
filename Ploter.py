import matplotlib.pyplot as plt

dados=open('g03w5.txt','r')

xt=[]
vt=[]
t1=[]

for line in dados:
	t,x,v = line.split()
	t1.append(float(t))
	xt.append(float(x))
	vt.append(float(v))
	
plt.figure(figsize=(6,5), dpi=96)
plt.axis([0,60,-2,2])

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo(s)')
plt.ylabel(r'Posi\c{c}\~{a}o (m) e Velocidade($\frac{m}{s}$)')

plt.title(r'Pendulum Moviment $\gamma$=0,3 $\omega^{2}_{0}$=5', fontsize=12)
plt.grid()
plt.plot(t1,xt,'r-', linewidth=1, label="$x_{(t)}$")
plt.plot(t1,vt,'b-', linewidth=1, label="$v_{(t)}$")
plt.legend(loc='upper right')
plt.savefig("G03W5.pdf", dpi=96)
plt.show()

dados.close()
