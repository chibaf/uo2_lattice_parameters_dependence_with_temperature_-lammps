# lattice_parameters_dependence_with_temperature_-lammps-

## computation of lattice pamrameters of UO2 for temperatures

lattice parameters of uo2 for temperatures (from 250K to 3000K; step size=125K) were computed.

lammps computed each volume corresponding to each temperature.

lattice parameter was computed as fllows:

c = (initial volume of system)**(1/3)/5.47     # where 5.47 is an initial lattice parameter.

lattice parameter at this temperature = (volume at this temperature)**(1/3) / c

### macbook air m1 is employed for this calculation

## installation with home brew and cmake

### openmpi

brew install open-mpi

### fftw

fftw

download tar ball and configure

### lammps

download tar ball

cd lammps-17Apr2024

cmake ../cmake/ -D PKG_KSPACE=yes -D FFT=fftw3

  cmake --build . -j 8

  ## test

  python3 fcc111.py > data.fcc111

  mpirun -np 8 lmp < in.1000

  ## computation of lattice parameter of UO2

  ### generate inputs

  python3 fcc111.py > data.fcc111

  python3 mkinput.py

  ### computation of lattice parameters

  python3 runlammps.py  

  ![image](https://github.com/chibaf/uo2_lattice_parameters_dependence_with_temperature_-lammps/assets/1296728/3d94f439-3c10-46f7-b458-f66794f2dfe2)

  ## References

Classical Molecular Dynamics Simulation of UO2 to Predict Thermophysical Properties, Chandra Bhanu Basak, 2003

https://www.researchgate.net/publication/248174824_Classical_Molecular_Dynamics_Simulation_of_UO2_to_Predict_Thermophysical_Properties


