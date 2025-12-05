# 02_methods.py
# Méthodes sur les chaînes de caractères et les listes

# Étape 1 : Méthodes de base sur les chaînes --------------------------------
name = "yann LERAT"

print(name.upper())   # tout en majuscules
print(name.lower())   # tout en minuscules
print(name.title())   # première lettre de chaque mot en majuscule

# On peut enchaîner les méthodes
clean_name = name.strip().title()  # strip() enlève les espaces au début/fin
print(clean_name)

print("-" * 50)

# Étape 2 : Remplacer du texte dans une chaîne -------------------------------
sentence = "Python, c'est cool ! Python est lisible."
print(sentence)

# replace(ancien, nouveau)
sentence_python3 = sentence.replace("Python", "Python 3")
print(sentence_python3)

print("-" * 50)

# Étape 3 : split() et join() ------------------------------------------------
# split() découpe une chaîne en liste
text = "Yann,Marie,Paul,Lucie"
names = text.split(",")  # découpe sur la virgule
print(names)             # -> ["Yann", "Marie", "Paul", "Lucie"]

# join() fait l'inverse : liste -> chaîne
joined_names = " - ".join(names)
print(joined_names)      # -> "Yann - Marie - Paul - Lucie"

print("-" * 50)

# Étape 4 : Méthodes de base sur les listes ----------------------------------
heights = [1.82, 1.68, 1.73]
print("Liste de départ :", heights)

# append() ajoute un élément à la fin
heights.append(1.60)
print("Après append(1.60) :", heights)

# insert(position, valeur) insère à un indice précis
heights.insert(1, 1.75)  # insère 1.75 à l'indice 1
print("Après insert(1, 1.75) :", heights)

# remove(valeur) supprime la première occurrence
heights.remove(1.60)
print("Après remove(1.60) :", heights)

# pop() supprime et renvoie le dernier élément (ou l’indice donné)
last_height = heights.pop()
print("Élément retiré avec pop() :", last_height)
print("Liste après pop() :", heights)

print("-" * 50)

# Étape 5 : Compter, trouver, trier ------------------------------------------
numbers = [3, 1, 4, 1, 5, 9, 1]

# count(valeur) : nombre d'occurrences
ones = numbers.count(1)
print("Nombre de '1' dans la liste :", ones)

# index(valeur) : premier indice de la valeur
first_index_of_4 = numbers.index(4)
print("Indice du premier 4 :", first_index_of_4)

# sort() trie la liste sur place
print("Liste avant tri :", numbers)
numbers.sort()
print("Liste après sort() :", numbers)

# reverse() inverse l'ordre
numbers.reverse()
print("Liste après reverse() :", numbers)


# pour filtrer, trier et manipuler des données plus complexes.
