import math
# Question 1
"""
MY VALUES, PUT IN YOURS
"""
number_hydrogen_atoms = 6.6e24 # [-]
diameter = 7.5 # [cm]

# constants
rho_water = 1 # density of water [g/cm^3]
M_water = 18.015694 # molecular weight of water [g/mol]
Na = 6.02214076e23 # Avogadro's number [mol^-1]

# calculation
number_of_mol_of_water = number_hydrogen_atoms / (Na * 2) # [mol]
mass = number_of_mol_of_water * M_water # [g]
volume = mass / rho_water # [cm^3]
radius = diameter / 2 # [cm]
height = volume / (math.pi * radius**2) # [cm]

print(f"Height of water column : {height} cm")

# Question 2
"""
MY VALUES, PUT IN YOURS THEN RUN THE FILE
"""
U = 6 # [MeV]

# constants
c = 299792458 # [m/s]
m0 = 9.10938356e-31 # electron rest mass [kg]
e = 1.602176634e-19 # electron charge [C]
eV = 1.602176634e-19  # [J]
Mev = 1.602176634e-13  # [J]

# calculation

# a
final_kinetic_energy_MeV = U # [MeV]
final_kinetic_energy_J = final_kinetic_energy_MeV * Mev # [J]
# b
# total final energy = kinetic energy + rest mass energy
rest_mass_energy_J = m0 * c**2 # [J]
rest_mass_energy_MeV = rest_mass_energy_J / Mev # [MeV]
total_final_energy_MeV = final_kinetic_energy_MeV + rest_mass_energy_MeV  # [MeV]

# c
# final mass in grams
# Formula : m = E_kinetic / c^2 + m0
final_mass_kg = final_kinetic_energy_J / c**2 + m0 # [kg]
final_mass_g = final_mass_kg * 1000 # [g]

# d
# Mass ratio
# Formula : m / m0
mass_ratio = final_mass_kg / m0 # [-]

print(f"Final kinetic energy: {final_kinetic_energy_MeV} MeV\nTotal final energy : {total_final_energy_MeV} MeV\nFinal mass : {final_mass_g} g\nMass ratio : {mass_ratio}")
