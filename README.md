# lattice_parameters_dependence_with_temperature_-lammps-
lattice_parameter_dependence_with_temperatures_(lammps)

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

