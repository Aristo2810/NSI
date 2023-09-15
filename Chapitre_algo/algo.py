"""
Auteur : Enis Béziau
Date : 13/09/23
Exo https://drive.google.com/drive/folders/1BupuPGlKAqCilow6GGcGf9JNwRKowDAZ
Programme Python correspondant aux 5 exercices, dans l'ordre
"""


# Exercice 1
x = int(input("Entrez un nombre entier > 0\n==> "))
if x % 2 == 0:
    y = x // 2
else:
    y = 3 * 1 + 1
print(f"L'application de Syracuse du nombre {x} donne {y}")


# Exercice 2
def heure_a_rio(heure_a_paris: int) -> int:
    """
    Prend en paramètre l'heure qu'il est à Paris et retourne celle qu'il est à Tokyo
    """
    if heure_a_paris >= 5:
        return heure_a_paris - 5
    else:
        return heure_a_paris + 24 - 5


# Exercice 3
def en_voiture(nombre_kilometre: int) -> float:
    """
    Prend en paramètre un entier, le nombre de kilomètre parcouru, et retourne le prix à payer
    """
    if nombre_kilometre >= 100:
        return 75
    else:
        return 75 + .35 * (nombre_kilometre - 100)


# Exercice 4
impot_paye = int(input("Combien d'impots avez vous payé ?\n==> "))
if impot_paye < 15000:
    a_payer = 0
elif impot_paye <= 30000:
    a_payer = 750 + .14 * (impot_paye - 30000)
else:
    a_payer = .05 * (impot_paye - 15000)

print(f"Vous allez devoir payer {a_payer} zeds")


def est_bisextille(annee: int) -> bool:
    """
    Prend en entrée un entier, une année à tester, et retoure True si celle ci est bisextille, False sinon
    """
    if annee >= 1582:
        if not annee % 4 == 0:
            return False
        else:
            if (annee % 100 == 0) and not (annee % 400 == 0):
                return False
            else:
                return True
    else:
        if annee % 4 == 0:
            return True
        else:
            return False
