import lammps.formats
a=lammps.formats.LogFile("log.250")
print(a.runs('Volume'))

