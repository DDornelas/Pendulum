import matplotlib.pyplot as plt

dados=open('energy.txt','r')

et=[]
t1=[]

for line in dados:
	t,e = line.split()
	t1.append(float(t))
	et.append(float(e))
	
plt.figure(figsize=(6,5), dpi=96)
plt.axis([-0.5,60,-0.1,0.6])

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo (s)')
plt.ylabel(r'Energia (N)')

plt.title(r'Pendulum Moviment Comportamento da Energia', fontsize=12)
plt.grid()
plt.plot(t1,et,'r-', linewidth=1)
plt.savefig("Energy.pdf", dpi=96)
plt.show()

dados.close()
