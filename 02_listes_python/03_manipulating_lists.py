# 03_manipulating_lists.py
# Modifier, ajouter, supprimer des éléments dans une liste
# + différence entre référence et copie

# Liste de départ (nom, taille)
fam = ["Yann", 1.82, "Marie", 1.68, "Paul", 1.73]
print("Liste de départ :", fam)

# 1) Modifier des éléments --------------------------------------------------
# Par exemple, on corrige la taille de Marie
fam[3] = 1.70
print("Après correction de la taille de Marie :", fam)

# 2) Ajouter des éléments ---------------------------------------------------
# Ajouter une nouvelle personne à la famille
fam.append("Lucie")
fam.append(1.60)
print("Après ajout de Lucie :", fam)

# On peut aussi concaténer deux listes
more_people = ["Tom", 1.80]
fam_extended = fam + more_people
print("Nouvelle liste étendue (fam_extended) :", fam_extended)

# 3) Supprimer des éléments -------------------------------------------------
# Suppression par index avec del
del fam[0]        # supprime "Yann"
del fam[0]        # supprime 1.82 (ancien élément d'indice 1)
print("Après suppression de Yann et sa taille :", fam)

# 4) Références vs copies ---------------------------------------------------
# Exemple classique pour montrer que les listes sont mutables
x = ["a", "b", "c"]
y = x          # y NE crée PAS une nouvelle liste, c'est la même référence
y[0] = "z"

print("x après modification via y :", x)  # -> ["z", "b", "c"]
print("y :", y)                           # -> ["z", "b", "c"]

# Pour créer une vraie copie indépendante :
z = list(x)    # ou z = x[:]
z[0] = "w"

print("x après modification de z :", x)   # -> ["z", "b", "c"]
print("z (copie modifiée) :", z)          # -> ["w", "b", "c"]
