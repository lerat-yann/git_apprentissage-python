# 03_filtrage_tri_selection.py
# Filtrer, trier et sélectionner des éléments dans une liste

# Étape 1 : Sélectionner des éléments selon une condition --------------------
heights = [1.82, 1.68, 1.73, 1.55, 1.90, 1.61]
print("Liste des tailles :", heights)

# On souhaite extraire les tailles supérieures à 1.70
tall_people = []
for h in heights:
    if h > 1.70:
        tall_people.append(h)

print("Tailles supérieures à 1.70 :", tall_people)

print("-" * 50)

# Étape 2 : List comprehension -----------------------------------------------
# Permet d'écrire la même logique en une ligne
tall_people_fast = [h for h in heights if h > 1.70]
print("Avec list comprehension :", tall_people_fast)

print("-" * 50)

# Étape 3 : Filtrer des chaînes ----------------------------------------------
names = ["Yann", "Marie", "Paul", "Lucie", "Marc", "Mélissa"]

# On sélectionne les noms qui commencent par 'M'
m_names = []
for n in names:
    if n.startswith("M"):
        m_names.append(n)

print("Noms commençant par 'M' :", m_names)

# Version list comprehension
m_names_fast = [n for n in names if n.startswith("M")]
print("Version rapide :", m_names_fast)

print("-" * 50)

# Étape 4 : Trier les listes --------------------------------------------------
numbers = [3, 1, 4, 1, 5, 9, 2]

print("Liste avant tri :", numbers)

# sort() trie sur place
numbers.sort()
print("Tri croissant :", numbers)

# reverse=True permet le tri décroissant
numbers.sort(reverse=True)
print("Tri décroissant :", numbers)

print("-" * 50)

# Étape 5 : sorted() retourne une nouvelle liste ------------------------------
original = [42, 10, 5, 100, 7]

sorted_list = sorted(original)  # croissant
sorted_desc = sorted(original, reverse=True)

print("Original :", original)
print("sorted()  :", sorted_list)
print("sorted(reverse=True) :", sorted_desc)

print("-" * 50)

# Étape 6 : Tri avec clé (key=...) -------------------------------------------
# Exemple : trier une liste de chaînes par longueur

words = ["Python", "IA", "Données", "Analyse", "API"]

print("Mots :", words)

# Tri selon la longueur
words_sorted_by_length = sorted(words, key=len)
print("Tri par longueur :", words_sorted_by_length)

print("-" * 50)

# Étape 7 : Filtrer + transformer en même temps ------------------------------
# Exemple : convertir en cm uniquement les tailles > 1.70

heights_cm = [round(h * 100) for h in heights if h > 1.70]
print("Tailles > 1.70 converties en cm :", heights_cm)

# Ce fichier conclut les bases :
# - filtrage avec conditions
# - list comprehensions
# - tri basique et avancé
# - sélection d’éléments selon une clé
