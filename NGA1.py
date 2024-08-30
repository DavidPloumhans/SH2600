# Question 1
# Atomic weight
# List of elements
B = [[10.012936862, 19.9], [11.009305166, 80.1]]
Cu = [[62.929597236, 69.15], [64.927789487, 30.85]]
Ag = [[106.905091531, 51.839], [108.904752, 48.161]]
# In = [[atomic weight of Indium 113, abundance of Indium 113]  ,  [atomic weight of Indium 115, abundance of Indium 115]]
In = [[112.904060448, 4.281], [114.903878773, 95.719]]
U = [[234.04095, 0.0054], [235.04393, 0.7204], [238.05079, 99.2742]]

def get_natural_atomic_weight(Element):
    toReturn = 0
    for i in range(len(In)):
        toReturn += Element[i][0] * Element[i][1] / 100
    return toReturn


# Mass defect
mn = 1.008664916
mp = 1.007276467

B10 = [10, 5, 10.012936862]
B11 = [11, 5, 11.009305166]

Cu63 = [63, 29, 62.929597236]
Cu65 = [65, 29, 64.927789487]

Ag107 = [107, 47, 106.905091531]
Ag109 = [109, 47, 108.904752]

In113 = [113, 49, 112.904060448]
In115 = [115, 49, 114.903878773]

U234 = [234, 92, 234.04095]
U235 = [235, 92, 235.04393]
U238 = [238, 92, 238.05079, 99.2742]

def get_mass_defect(Isotope):
    return Isotope[1] * mp + (Isotope[0] - Isotope[1]) * mn - Isotope[2]


# Binding energy per nucleon
def get_binding_energy_per_nucleon(Isotope):
    return get_mass_defect(Isotope) / Isotope[0] * 931.5


def get_answer(Element, Isotope):
    print(f"Natural atomic weight : {get_natural_atomic_weight(Element)}\nMass defect : {get_mass_defect(Isotope)}\nBinding energy per nucleon: {get_binding_energy_per_nucleon(Isotope)}")

"""
HERE YOU CAN CHANGE THE ELEMENT AND ISOTOPE AND GET THE ANSWER
"""
get_answer(In, In115)


# Question 2
"""
MY ISOTOPE, CHANGE VALUES FOR YOURS ACCORDINGLY THEN RUN THE FILE
"""
fission_energy_MeV = 196  # MeV
mass = 1  # g
molar_mass = 232.038054  # [g/mol]

# constants
eV = 1.602176634e-19  # [J]
Mev = 1.602176634e-13  # [J]
Na = 6.02214076e23  # Avogadro's number [mol^-1]

# calculation
number_of_nucleus = mass / molar_mass * Na
energy_released_MeV = fission_energy_MeV * number_of_nucleus
energy_released_J = energy_released_MeV * Mev

# conversion to kWh/g
energy_released_kWh = energy_released_J / (3600 * 1000) / mass
# conversion to MWd/g
energy_released_MWd = energy_released_J / (3600 * 24 * 10**6) / mass

print(f"Energy released in kWh/g : {energy_released_kWh}\nEnergy released in MWd/g : {energy_released_MWd}")

"""
RUN THE FILE
"""



































































"""# Version 2
In_atomic_weight = [112.904060448, 114.903878773]
In_abundance = [4.281, 95.719]

def get_natural_atomic_weight_v2(atomic_weight, abundance):
    toReturn = 0
    for i in range(len(atomic_weight)):
        toReturn += atomic_weight[i] * abundance[i] / 100
    return toReturn

print(get_natural_atomic_weight_v2(In_atomic_weight, In_abundance))"""



