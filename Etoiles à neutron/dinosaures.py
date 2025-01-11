import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import MultipleLocator
import numpy as np

limit_mass = 2.122

def dinosaure():
    rc('text.latex', preamble=r'\usepackage[helvet]{sfmath} \usepackage{sansmathfonts}')
    plt.rcParams['figure.dpi'] = 150
    
    file_path = 'Naines Blanches.xlsm'
    resultats_data = pd.read_excel(file_path, sheet_name='Resultats')

    x_resultats = resultats_data['Unnamed: 4'][2::].values  # Masse relative (Naines Blanches)
    y_resultats = resultats_data['Unnamed: 1'][2::].values / 1000  # Rayon Km (Naines Blanches)

    data = np.genfromtxt("Resultats_Masse_Rayon.dat", skip_header=1)
    R_imported = data[:, 0]  # Rayon Km (Étoiles à Neutrons)
    M_imported = data[:, 1]  # Masse relative (Étoiles à Neutrons)

    plt.figure(figsize=(8, 6))
    plt.plot(R_imported, M_imported, color="blue", linestyle="-", linewidth=1.5, label="Étoiles à Neutrons")
    plt.plot(y_resultats, x_resultats, color="blue", linestyle="-", linewidth=1.5, label="Naines Blanches")

    plt.xlabel(r'${\rm Rayon~(km)}$', fontsize=12)
    plt.ylabel(r'${\rm M/M_\odot}$', fontsize=12)
    plt.title('Masse en fonction du Rayon', fontsize=14)
    plt.xscale('log')

    plt.gca().yaxis.set_major_locator(MultipleLocator(0.25))
    plt.savefig('Graphes/Neutron_Stars/MasseRayon_Neutron_and_Dwarfs.eps', format='eps')
    plt.show()

    data = np.genfromtxt("Resultats_Masse_Rayon.dat", skip_header=1)
    M_imported = data[:, 1]  # Masse relative (Étoiles à Neutrons)

    Mmax = max(M_imported)

    print(f'\nLa masse max est {round(Mmax,4)} avec une erreur de {round((Mmax-limit_mass)/limit_mass *100,3)} %')