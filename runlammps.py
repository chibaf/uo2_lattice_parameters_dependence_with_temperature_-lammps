# run lammps
import os
for i in range(0,23):
    temp=250+125*i
    fn="in."+str(temp)
    print(fn)
    os.system("mpirun -np 8 lmp < "+fn)
print("end tasks")
