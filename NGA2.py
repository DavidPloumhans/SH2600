import math
# Question 1
"""
MY VALUES, PUT IN YOURS
"""
J1 = 2.2e10 # [neutrons / (cm^2*s)]
J2 = 1e10 # [neutrons / (cm^2*s)]
theta = 34 # [degree]

# calculation

# Neutron flux, sum of the intensity of the beams
phi = J1 + J2 # [neutrons / (cm^2*s)]

# Neutron current, using Al-Kashi theorem
J = math.sqrt(J1**2 + J2**2 - 2 * J1 * J2 * math.cos(math.radians(180 - theta))) # [neutrons / (cm^2*s)]

alpha = math.acos((J**2 + J1**2 - J2**2) / (2 * J * J1)) # [radian]

print(f"Neutron flux : {phi} neutrons / (cm^2*s)\nNeutron current : {J} neutrons / (cm^2*s)\nAlpha : {math.degrees(alpha)} degree")

# Question 2
"""
MY VALUES, PUT IN YOURS THEN RUN THE FILE
"""
t_half = 2.3 # [min]
E_eV = 0.0253 # [eV]
simga_c = 0.23 # [barn]
phi = 3e8 # [neutrons / (cm^2*s)]
m = 0.03 # [g]

# constants
eV = 1.602176634e-19 # [J]
mn = 1.67492749804e-27 # [kg]
M_Al = 26.9815386 # [g/mol]
rho_Al = 2.69890 # [g/cm^3]

# calculation
# neutron densitiy
E_J = E_eV * eV # [J]
v = math.sqrt(2 * E_J / mn) # [m/s]
v_cm = v * 100 # [cm/s]
neutron_density = phi / v_cm  # [neutrons / cm^3]

# Production rate in the sample
sigma_c_sqcm = simga_c * 1e-24 # [cm^2]
Na = 6.02214076e23 # Avogadro's number [mol^-1]
N_Al = rho_Al / M_Al * Na # [atoms / cm^3] (atomic density)
V_Al = m / rho_Al # [cm^3]
production_rate = sigma_c_sqcm * phi * N_Al * V_Al # [neutrons / s] or [Bq]

# Maximum Activity of the sample
# Equal to the production rate as the sample is in secular equilibrium
activity = production_rate # [Bq]

print(f"Neutron density : {neutron_density} neutrons / cm^3\nProduction rate : {production_rate} atoms   / s\nActivity : {activity} Bq")