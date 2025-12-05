# 01_numpy_intro.py
# Introduction à NumPy : création et manipulation de tableaux 1D

import numpy as np   # import conventionnel de NumPy

# Étape 1 : Créer un tableau NumPy (1D) --------------------------------------
# Conversion d'une liste Python en array NumPy
heights_list = [1.82, 1.68, 1.73, 1.55, 1.90]
heights = np.array(heights_list)

print("Liste Python :", heights_list)
print("Array NumPy  :", heights)

print("-" * 50)

# Étape 2 : Comparaison liste Python vs array NumPy --------------------------
# Sur une liste Python, l'opération x * 2 duplique la liste
print("Liste * 2 :", heights_list * 2)

# Sur un array NumPy, l'opération est mathématique (vectorisée)
print("Array * 2 :", heights * 2)

print("-" * 50)

# Étape 3 : Propriétés utiles ------------------------------------------------
print("Type de heights :", type(heights))      # numpy.ndarray
print("Shape (forme)   :", heights.shape)      # (5,)
print("Taille totale   :", heights.size)       # 5
print("Type interne    :", heights.dtype)      # float64 en général

print("-" * 50)

# Étape 4 : Indexation et slicing -------------------------------------------
print("Premier élément :", heights[0])
print("Dernier élément :", heights[-1])

print("Slicing 0:3     :", heights[0:3])    # 3 premiers
print("Slicing 2:5     :", heights[2:5])    # du 3ème au dernier

print("-" * 50)

# Étape 5 : Opérations vectorisées ------------------------------------------
# Elles s'appliquent sur tous les éléments en même temps
print("heights + 0.10 :", heights + 0.10)
print("heights * 100  :", heights * 100)
print("heights ** 2   :", heights ** 2)

# Comparaisons vectorisées
print("heights > 1.70 :", heights > 1.70)

# Sélection via masque booléen
tall = heights[heights > 1.70]
print("Tailles > 1.70 :", tall)

# Ce fichier introduit les bases des arrays NumPy :
# - création
# - slicing
# - opérations vectorisées
# - filtrage avec masques
