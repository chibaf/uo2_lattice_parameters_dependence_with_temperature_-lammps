import lammps.formats
import matplotlib.pyplot as plt
import math

x=[]
y=[]
for i in range(0,23):
  k=i*125+250
  x.append(k)
  fn="log."+str(k)
  a=lammps.formats.LogFile(fn)
  b=a.runs[0]['Volume']
  c=sum(b)/len(b)
  if i==0:
    d=pow(c,1/3)/5.47 # where 5.47 is an initial lattice parameter
  e=pow(c,1/3)/d
  y.append(e)
plt.plot(x,y,'k',x,y,'ro')
plt.show()