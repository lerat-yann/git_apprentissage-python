# 01_hello_python.py
# Premiers pas : afficher du texte, faire des calculs, manipuler des chaînes

# Affichage simple
print("Hello Python")

# Calculs de base
print(3 + 4)           # addition
print(10 * 2)          # multiplication
print(8 / 3)           # division réelle (float)
print(8 // 3)          # division entière
print(8 % 3)           # reste (modulo)
print(2 ** 5)          # puissance

# Variables + affichage (concaténation et f-strings)
language = "Python"
print("Hello " + language)     # concaténation
print(f"Hello {language} !")   # f-string

# Paramètres utiles de print
print("one", "two", "three", sep=" - ")  # séparateur personnalisé
print("ligne sans retour", end="... fin\n")  # fin personnalisée

# Chaînes : longueur et répétition
print(len(language))   # longueur de la chaîne
print(language * 3)    # répétition de la chaîne

# Caractères d'échappement
print("Ligne 1\nLigne 2\t(tab)")
