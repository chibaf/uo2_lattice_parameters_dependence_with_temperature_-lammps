#!/usr/bin/python3

import sys
from string import *
import os
from subprocess import *
    
for i in range(0,23):
 temp=250+i*125
 fn="in."+str(temp)
 os.system("cat script_part1.txt >"+fn)
 s="log log."+str(temp)+" "
 os.system("echo " +s+ ">>"+fn)
 s="velocity all create " +str(float(temp))+ " 78621 dist gaussian"
 os.system("echo " +s+ ">>"+fn)
 s="fix NPT all npt temp " +str(float(temp))+ " " +str(float(temp))+ " 0.005 iso 0.0 0.0 10.0 drag 0.2"
 os.system("echo " +s+ ">>"+fn)
 s="thermo 10 "
 os.system("echo " +s+ ">>"+fn)
 os.system("echo " +s+ ">>"+fn)
 s="run 3000 "
 os.system("echo " +s+ ">>"+fn)
 os.system("time mpirun -np 8 lmp < "+fn)