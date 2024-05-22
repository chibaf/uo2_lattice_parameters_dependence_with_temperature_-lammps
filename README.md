# lattice_parameters_dependence_with_temperature_-lammps-
lattice_parameter_dependence_with_temperatures_(lammps)

## installation with cmake

brew install open-mpi

fftw

download and configure

download tar ball

cd lammps-17Apr2024

cmake ../cmake/ -D PKG_KSPACE=yes -D FFT=fftw3

  510  cmake --build . -j 8

  ## test

  python3 fcc111.py > data.fcc111

  512  mpirun -np 8 lmp < in.1000
