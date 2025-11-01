# 01_python_lists.py
# Introduction aux listes Python

# Étape 1 : Création d'une liste (hétérogène)
fam = ["Yann", 1.82, "Marie", 1.68, "Paul", 1.73]

# Étape 2 : Vérifier les informations de base
print(len(fam))   # nombre d'éléments → 6
print(type(fam))  # type → <class 'list'>
print(fam)        # affiche la liste complète

# Étape 3 : Exemple de liste homogène (uniquement des nombres)
heights = [1.82, 1.68, 1.73]
print(heights)

# Étape 4 : Exemple de liste de chaînes
names = ["Yann", "Marie", "Paul"]
print(names)

# Ces listes seront utilisées dans les prochains exercices
# pour faire des sélections (indexation, slicing)
