# 02_variables_types.py
# Découverte des variables, types et opérations de base en Python

# Déclaration des variables
height = 1.75      # taille en mètres
age = 32           # âge en années
name = "Yannick"   # nom sous forme de chaîne de caractères
is_student = True  # valeur booléenne
weight = 68.7      # poids en kilogrammes

# Affichage du type de chaque variable
print(type(height))     # float
print(type(age))        # int
print(type(name))       # str
print(type(is_student)) # bool

# Opération simple sur une variable
older_age = age + 10
print("Âge dans 10 ans :", older_age)

# Calcul de l'indice de masse corporelle (BMI)
bmi = weight / height ** 2
print("Indice de masse corporelle (BMI) :", bmi)

# Exemple de concaténation de chaînes
print("Nom :", name)
print("Hello " + name)

# Différence entre addition et concaténation
print(2 + 3)        # addition
print("ab" + "cd")  # concaténation de chaînes

# Exemple de reproductibilité :
# si on change la valeur du poids ou de la taille,
# le calcul du BMI s'adapte automatiquement.
