#generate lammps input fies
for i in range(0,23):
    temp=250+125*i
    fn="in."+str(temp)
    f=open(fn,'w',encoding="utf-8\n")
    #Initialization:
    f.write("atom_style charge\n")
    f.write("units metal\n")
    f.write("boundary        p p p\n")
    f.write("dimension       3\n")
    f.write("newton          on\n")
    #default is on
    #Atom definition:
    f.write("read_data data.fcc111\n")
    f.write("mass 1 238\n")
    f.write("group         1 type 1\n")
    f.write("mass 2 16\n")
    f.write("group         2 type 2\n")
    #Force fields:
    f.write("pair_style hybrid/overlay born/coul/long 10.0 morse 10.0\n")
    f.write("pair_coeff 1 1 born/coul/long 0.013806784 0.32702 3.26 0.0 0.0 10.0\n")
    f.write("pair_coeff 1 2 born/coul/long 0.013806827 0.327021 3.54 0.0 0.0 10.0\n")
    f.write("pair_coeff 1 2 morse 0.57745 1.65 2.369 10.0\n")
    f.write("pair_coeff 2 2 born/coul/long 0.013806869 0.327022 3.82 3.950633264 0.0 10.0\n")
    # refered to http://lammps.sandia.gov/threads/msg13365.html
    f.write("kspace_style pppm 1.0e-4\n")  # use ewald method
    f.write("log log.UO2_fcc111-"+str(temp)+"K\n")
    f.write("velocity all create "+str(float(temp))+" 78621 dist gaussian\n")
    f.write("fix NPT all npt temp "+str(float(temp))+" "+str(float(temp))+" 0.005 iso 0.0 0.0 10.0 drag 0.2\n")
    f.write("thermo 10\n")
    f.write("dump 1 all atom 10 dump.UO2_fcc111-"+str(temp)+"K.gz\n")
    f.write("run 2000\n")
    f.close()
