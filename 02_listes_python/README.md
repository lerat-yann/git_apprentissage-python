📚 02_listes_python

Dans ce deuxième chapitre, je poursuis mon apprentissage du langage Python en découvrant une structure essentielle : les listes.
Elles permettent de regrouper plusieurs valeurs, de les manipuler, d’en extraire certaines parties et de les modifier facilement.
Ce chapitre est divisé en trois exercices progressifs qui couvrent toutes les bases nécessaires pour être à l’aise avec la manipulation de listes.

🔹 01_python_lists.py

Dans cet exercice, j’ai appris à :

créer mes premières listes en Python ;

distinguer des listes hétérogènes (types mélangés) et homogènes (même type) ;

vérifier la taille d’une liste avec len() ;

afficher son type avec type() ;

afficher le contenu complet d’une liste.

Exemple de sortie :

6
<class 'list'>
['Yann', 1.82, 'Marie', 1.68, 'Paul', 1.73]
['Yann', 'Marie', 'Paul']
[1.82, 1.68, 1.73]

🔹 02_subsetting_slicing.py

Cet exercice m’a permis d’aller plus loin en apprenant comment accéder à des éléments précis d’une liste.

J’y découvre :

l’indexation positive pour récupérer un élément (fam[0]) ;

l’indexation négative pour accéder depuis la fin (fam[-1]) ;

le slicing, c’est-à-dire l’extraction d’une sous-partie de liste (fam[0:2], fam[:3], fam[3:]) ;

l’utilisation d’un pas dans l’extraction (fam[2:6:2]) ;

la création d’une copie par slicing (fam[:]) ;

la manipulation de listes imbriquées et l’accès à leurs éléments (fam2[0][1]).

Exemple de sortie :

Yann
Marie
1.73
1.68
['Yann', 1.82]
['Marie', 1.68, 'Paul', 1.73]
['Marie', 'Paul']
['Yann', 1.82, 'Marie']
[1.68, 'Paul', 1.73]
['Yann', 1.82]
1.82
Paul
[['Yann', 1.82], ['Marie', 1.68]]

🔹 03_manipulating_lists.py

Dans cet exercice, j’apprends à modifier et mettre à jour une liste existante.
C’est une étape importante car les listes Python sont mutables, ce qui signifie qu’on peut les changer après leur création.

J’y apprends notamment :

modifier un élément (fam[3] = 1.70) ;

ajouter de nouveaux éléments avec append() ;

étendre une liste avec l’opération + ;

supprimer un élément avec del ;

comprendre la différence entre :

une référence vers une même liste (y = x) ;

une copie indépendante (z = list(x) ou x[:]).

Exemple de sortie :

['Yann', 1.82, 'Marie', 1.68, 'Paul', 1.73]
['Yann', 1.82, 'Marie', 1.70, 'Paul', 1.73]
['Yann', 1.82, 'Marie', 1.70, 'Paul', 1.73, 'Lucie', 1.60]
['z', 'b', 'c']
['z', 'b', 'c']
['w', 'b', 'c']

🎯 Objectif du chapitre

Ce chapitre m’a appris à :

créer des listes simples et variées ;

extraire précisément la partie d’une liste dont j’ai besoin ;

modifier, compléter et nettoyer une liste ;

comprendre comment fonctionnent les références et les copies en Python.

Ces connaissances sont indispensables pour la suite de mon apprentissage, notamment pour travailler avec les fonctions, les boucles, les tableaux, ou encore des structures de données plus avancées.
