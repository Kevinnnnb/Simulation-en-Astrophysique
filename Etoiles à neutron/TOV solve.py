import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from tovsolver.tov import *
from tovsolver.constants import *
from dinosaures import dinosaure
from datetime import datetime

deltaR = 100 #[m]
Rayon = 1e8 #[m]

print(f'\nLa simulation à commencé à : {datetime.now()}')
print(f'Avec un rayon max de {Rayon} m\n')

rc('text.latex', preamble=r'\usepackage[helvet]{sfmath} \usepackage{sansmathfonts}')

plt.rcParams['figure.dpi'] = 150

eos = np.genfromtxt("Neutron stars/TOVsolver/example/example_eos.dat", names=True, skip_header=1)

n_arr, p_arr = eos["energy_density"], eos["pressure"]

tov_s = TOV(n_arr, p_arr, plot_eos=False)

m_arr = []
R_arr = []
pressure_arr = []

for dens_c in np.logspace(-0, 3.7, 350):
    R, M, prof = tov_s.solve(dens_c, rmax=Rayon, dr=deltaR)
    m_arr.append(M)
    R_arr.append(R)

data = np.column_stack((R_arr, m_arr,))
np.savetxt("Resultats_Masse_Rayon.dat", data, header="Rayon(km) Masse(M/M_sun)", fmt="%.30f")

print(f'\nTerminé à : {datetime.now()}\n')

plt.plot(R_arr, m_arr, color="blue", linestyle="-", linewidth=1.5)
plt.title('Masse en fonction du rayon')
plt.xlim(10, 50)
plt.ylim(0, 2.3)

plt.ylabel(r'${\rm M/M_\odot}$')
plt.xlabel(r'${\rm R~(km)}$')

plt.savefig('Graphes/Neutron_Stars/MasseRayon_Neutron.eps', format='eps')
plt.show()

dinosaure() #trace le graphe de la masse en fonction du rayon pour les WD et les NS