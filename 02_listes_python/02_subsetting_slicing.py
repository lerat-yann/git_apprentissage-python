# 02_subsetting_slicing.py
# Sélections dans les listes : indexation & slicing

# Liste hétérogène (nom, taille)
fam = ["Yann", 1.82, "Marie", 1.68, "Paul", 1.73]

# 1) Indexation (un seul élément) ------------------------------------------
print(fam[0])    # premier élément -> "Yann"
print(fam[2])    # troisième élément -> "Marie"

# Indexation négative (depuis la fin)
print(fam[-1])   # dernier élément -> 1.73
print(fam[-3])   # troisième en partant de la fin -> 1.68

# 2) Slicing (sous-liste) ---------------------------------------------------
# Rappel : start inclus, end exclus, step optionnel

print(fam[0:2])      # éléments d'indice 0 et 1  -> ["Yann", 1.82]
print(fam[2:6])      # éléments 2..5            -> ["Marie", 1.68, "Paul", 1.73]
print(fam[2:6:2])    # un élément sur deux (2,4)-> ["Marie", "Paul"]

# Bornes omises
print(fam[:3])       # du début jusqu’à 2       -> ["Yann", 1.82, "Marie"]
print(fam[3:])       # de 3 jusqu’à la fin      -> [1.68, "Paul", 1.73]

# Copie par slicing (shallow copy)
sub = fam[:]         # nouvelle liste (copie peu profonde)
print(sub)

# 3) Listes imbriquées (nested lists) --------------------------------------
fam2 = [
    ["Yann", 1.82],
    ["Marie", 1.68],
    ["Paul", 1.73],
]

print(fam2[0])       # -> ["Yann", 1.82]
print(fam2[0][0])    # -> "Yann"
print(fam2[0][1])    # -> 1.82
print(fam2[-1][0])   # -> "Paul"

# Slicing sur liste imbriquée
print(fam2[:2])      # -> [["Yann", 1.82], ["Marie", 1.68]]
