import matplotlib.pyplot as plt

dados=open('g07w7.txt','r')

xt=[]
vt=[]
t1=[]

for line in dados:
	t,x,v = line.split()
	t1.append(float(t))
	xt.append(float(x))
	vt.append(float(v))
	
plt.figure(figsize=(6,5), dpi=96)

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Posi\c{c}\~{a}o (m)')
plt.ylabel(r'Velocidade($\frac{m}{s}$)')

plt.title(r'Pendulum Moviment Espa\c{c}o de Fases $\gamma$=0,7 $\omega^{2}_{0}$=7', fontsize=12)
plt.grid()
plt.plot(xt,vt,'r-', linewidth=1)
plt.savefig("EFG07W7.pdf", dpi=96)
plt.show()

dados.close()
