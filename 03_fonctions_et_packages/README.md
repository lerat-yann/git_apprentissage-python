03_fonctions_et_packages

Ce chapitre introduit trois notions essentielles en Python :

les fonctions (définir, appeler, retourner des valeurs),

les méthodes appliquées aux chaînes et aux listes,

les techniques de filtrage, tri et sélection d’éléments.

Ces outils permettent d’organiser son code, d’éviter les répétitions et de préparer les futures manipulations de données.

📌 01_functions.py — Premiers pas avec les fonctions

Dans ce fichier, j’apprends :

➤ Définir une fonction

Avec def suivi d’un nom et de parenthèses.

➤ Appeler une fonction

Il suffit d’écrire son nom suivi de ().

➤ Passer des paramètres

Exemple : greet(name) permet de personnaliser un message.

➤ Retourner une valeur

Avec return, comme dans le calcul du BMI.

➤ Utiliser des valeurs par défaut

Exemple : welcome_user(name, language="fr").

Ces exemples montrent comment structurer du code réutilisable.

📌 02_methods.py — Méthodes sur les chaînes et les listes

Dans ce fichier, j’utilise plusieurs méthodes utiles :

🔤 Chaînes de caractères

upper(), lower(), title()

strip()

replace()

split() pour découper

join() pour reconstruire une chaîne

📋 Listes

append(), insert() pour ajouter

remove(), pop() pour supprimer

count(), index()

sort(), reverse() pour trier ou inverser

Ces méthodes permettent de modifier et nettoyer des données facilement.

📌 03_filtrage_tri_selection.py — Filtrer et trier des données

Dans ce fichier, je pratique :

✔️ Filtrer une liste

Avec une boucle for et une condition (if), par exemple sélectionner les tailles > 1.70.

✔️ List comprehensions

La même logique écrite de manière plus compacte.

✔️ Trier des données

sort() (modifie la liste),

sorted() (retourne une nouvelle liste),

reverse=True pour trier dans l'ordre inverse.

✔️ Tri avec clé (key=)

Exemple : trier des mots selon leur longueur.

✔️ Combiner filtrage + transformation

Comme convertir en cm uniquement les valeurs supérieures à un seuil.

🎯 Conclusion du chapitre

Ce chapitre pose les bases essentielles pour écrire du code propre et organisé :

les fonctions structurent le programme ;

les méthodes facilitent les manipulations ;

le filtrage et le tri préparent aux traitements de données plus avancés.
