# 01_functions.py
# Introduction aux fonctions Python

# Étape 1 : Première fonction (sans paramètre, sans valeur de retour)
def say_hello():
    """Affiche un message de bienvenue."""
    print("Hello, Python !")
    print("Bienvenue dans le chapitre sur les fonctions.")


# Appel de la fonction
say_hello()

# Séparateur visuel
print("-" * 50)

# Étape 2 : Fonction avec un paramètre
def greet(name):
    """Affiche un message personnalisé avec le prénom."""
    print(f"Bonjour {name}, ravi de te voir ici !")


# Appels de la fonction avec des valeurs différentes
greet("Yann")
greet("Marie")

print("-" * 50)

# Étape 3 : Fonction avec plusieurs paramètres et valeur de retour
def bmi(weight, height):
    """
    Calcule le BMI (Body Mass Index) à partir du poids et de la taille.
    BMI = weight / height ** 2
    """
    result = weight / height ** 2
    return result


# Utilisation de la fonction
weight_kg = 68.7
height_m = 1.79

my_bmi = bmi(weight_kg, height_m)
print("Mon BMI est :", my_bmi)

print("-" * 50)

# Étape 4 : Réutiliser la valeur retournée
# Ici, on arrondit le BMI à 2 décimales
bmi_rounded = round(my_bmi, 2)
print("Mon BMI arrondi est :", bmi_rounded)

print("-" * 50)

# Étape 5 : Paramètres avec valeur par défaut
def welcome_user(name, language="fr"):
    """
    Affiche un message de bienvenue.
    - name : prénom de l'utilisateur
    - language : 'fr' ou 'en' (par défaut : 'fr')
    """
    if language == "fr":
        print(f"Bienvenue {name} !")
    elif language == "en":
        print(f"Welcome {name}!")
    else:
        print(f"Salut {name}, langue inconnue.")


welcome_user("Yann")        # utilise la valeur par défaut "fr"
welcome_user("Yann", "en")  # en anglais

# Ces fonctions seront réutilisées dans les prochains exercices
# pour aller plus loin avec les méthodes, les filtres et les tris.
