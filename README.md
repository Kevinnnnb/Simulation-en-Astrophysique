# Simulation en Astrophysique

Ce dépôt contient les ressources liées à notre travail de maturité sur la **modélisation et la simulation de la structure interne des naines blanches (et d'étoiles à neutrons)**.

## Contenu

- **`Naines blanches.xlsm`** : Fichier Excel concernant la simulation des naines blanches
- **`TOV solve.py`** : Script principal pour la simulation des étoiles à neutrons
- **`dinosaures.py`** : Contient la fonction dinosaure utilisée dans le script TOV solve.py
- **`Limit Neutron Stars.nb`** : Fichier mathematica contenant le calcul de la masse limite pour une étoile à neutron (1ère approximation)
- **`requirements.txt`** : Contient toutes les bibliothèques à installer pour pouvoir exécuter les scripts python

## Prérequis

- **Python 3.8+**
- Bibliothèques nécessaires (installables via pip3) :
  - `numpy`
  - `matplotlib`
  - `tovsolver`

Pour installer les dépendances : 
```bash
pip3 install -r requirements.txt
