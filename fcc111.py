# file in sub_folder
import sys
from string import *
from math import *

#
# parameters
#
a=5.47                  # lattice parameter
b=a*sqrt(2)/2          
c=sqrt(3)*b/2
#
charge=2.4              # charge
charge1=str(charge)
charge2=str(-0.5*charge)
uran="1"                # atom type in lammps script
oxygen="2"              # atom type in lammps script
#
d0=b/2
mx=my=mz=20;      # number of atomsmx,my must be even numbers.

# generating coordinates of Oxygen atom
list_atom=[]
dp=c/2
dp1=dp/2.
c1=c/3.
kz=mx
for k in range(1,mz*2+1): # index for z direction
 for j in range(1,my+1):  # index for y direction
  for i in range(1,mx+1): # index for x direction
   k1=k
   if fmod(k1,2)==0:
    k1=k1-1
   x=(j-1)*c+c1*(k1-1)
   x=fmod(x,kz*c)
   if fmod(j,2)==1:
    el=[oxygen,charge2,x,d0+(i-1)*b,dp*(k-1)+dp1]
    list_atom.append(el)
   else:
    el=[oxygen,charge2,x,(i-1)*b,dp*(k-1)+dp1]
    list_atom.append(el)
# generating coordinates of Uranium atom (4x4x2 block)
dz=dp*2.
c2=2.*c/3.
for k in range(1,mz+1):   # index for z direction
 for j in range(1,my+1):  # index for y direction
  for i in range(1,mx+1): # index for x direction
    x=(j-1)*c+c2*(k-1)+c/3
    x=fmod(x,kz*c)
    if fmod(j,2)==1:
     el=[uran,charge1,x,(i-1)*b,dz*(k-1)+dp]
     list_atom.append(el)
    else:
     el=[uran,charge1,x,d0+(i-1)*b,dz*(k-1)+dp]
     list_atom.append(el)

#
#           printing lamms data file
#
f=sys.stdout  # use standard i/o
#
f.write("UO2(111) \n")        # header
f.write("\n")
f.write(str(len(list_atom))+" atoms\n")  # number of atoms
f.write("\n")
f.write("0 bonds\n")          # lammps parameter
f.write("0 angles\n")         # lammps parameter
f.write("0 dihedrals\n")      # lammps parameter
f.write("0 impropers\n")      # lammps parameter
f.write("\n")
f.write("2 atom types\n")     # number of atom types
f.write("0 bond types\n")     # lammps parameter
f.write("0 angle types\n")    # lammps parameter
f.write("0 dihedral types\n") # lammps parameter
f.write("0 improper types\n") # lammps parameter
f.write("\n")
f.write("\n")
#           range of box
f.write(''.join((str(0)," ",str(mx*c)," xlo xhi\n")))   # length of box for x direction
f.write(''.join((str(0)," ",str(my*b)," ylo yhi\n")))   # length of box for y direction
f.write(''.join((str(0)," ",str(mz*dz)," zlo zhi\n")))  # length of box for z direction
#
f.write("\n")
f.write("\n")
#           print coordinate sets of atoms
f.write("Atoms\n")
f.write("\n")
for i in range(0,len(list_atom)):
  el=list_atom[i]
  s=''.join((str(i+1)," ",el[0]," ",el[1]," ",str(el[2])," ",str(el[3])," ",str(el[4]),"\n"))
  f.write(s)