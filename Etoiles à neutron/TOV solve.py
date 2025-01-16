import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from tovsolver.tov import *
from tovsolver.constants import *
from dinosaures import dinosaure

deltaR = 100  # [m]
Rayon = 2e7  # [m]

rc('text.latex', preamble=r'\usepackage[helvet]{sfmath} \usepackage{sansmathfonts}')
plt.rcParams['figure.dpi'] = 150

eos = np.genfromtxt("eos.dat", names=True, skip_header=1)
n_arr, p_arr = eos["energy_density"], eos["pressure"]

tov_s = TOV(n_arr, p_arr, plot_eos=False)

m_arr = []
R_arr = []
pressure_profiles = []
average_pressure_arr = []

for dens_c in np.logspace(-0, 3.7, 350):
    R, M, prof = tov_s.solve(dens_c, rmax=Rayon, dr=deltaR)
    r, e_R, p_R, m_R = prof

    m_arr.append(M)
    R_arr.append(R)
    pressure_profiles.append((r, p_R))

    average_pressure = np.mean(p_R)
    average_pressure_arr.append(average_pressure)

r, p_R = pressure_profiles[-1]

data = np.column_stack((R_arr, m_arr, average_pressure_arr))
np.savetxt("Resultats_Masse_Rayon_Pression.dat", data, header="Rayon(km) Masse(M/M_sun) Pression_Moyenne(Pa)", fmt="%.30f")
pression = np.genfromtxt("Resultats_Masse_Rayon_Pression.dat", skip_header=3)[:, 1]

plt.figure()
plt.plot(r / 1e5, p_R, color="blue", linestyle="-", linewidth=1.5)
plt.title('Pression en fonction du rayon')
plt.xscale('log')
plt.yscale('log')
plt.xlim(1, 12) 
plt.ylabel(r'${\rm P~(Pa)}$')
plt.xlabel(r'${\rm Rayon~(km)}$')
plt.savefig('Graphes/Neutron_Stars/PressionRayon_Neutron.eps', format='eps')
plt.show()

plt.figure()
plt.plot(R_arr, m_arr, color="blue", linestyle="-", linewidth=1.5)
plt.title('Masse en fonction du rayon')
plt.xlim(10, 50)
plt.ylim(0, 2.3)
plt.ylabel(r'${\rm M/M_\odot}$')
plt.xlabel(r'${\rm Rayon~(km)}$')
plt.savefig('Graphes/Neutron_Stars/MasseRayon_Neutron.eps', format='eps')
plt.show()

dinosaure()
