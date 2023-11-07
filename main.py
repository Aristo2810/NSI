"""
Auteur : Enis Béziau
Date : 8 novembre 2022
Exercices du cours
"""
import random
import math


# Exercice 1
def distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    """Renvoie la distance entre deux points de coordonnées données en tuple"""
    return math.sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]))


assert distance((0, 0), (3, 4)) == 5.0
assert distance((0, 0), (3, 1)) == 3.1622776601683795
assert distance((5, 5), (-5, -5)) == 14.142135623730951
assert distance((0, 0), (0, 0)) == 0


def milieu(a: tuple[int, int], b: tuple[int, int]) -> tuple[float, float]:
    return (a[0] + b[0]) / 2, (a[1] + b[1]) / 2


assert milieu((1, 1), (3, 3)) == (2.0, 2.0)
assert milieu((0, 0), (0, 0)) == (0.0, 0.0)
assert milieu((5, 0), (0, 5)) == (2.5, 2.5)


# Exercice 4
def jour_semaine(date: tuple[int, int, int]):
    """Renvoie l'index correspondant au jour de la semaine : 0 --> dimanche ..."""
    jour, mois, annee = date[0], date[1], date[2]
    annee_corrigee = (annee - 1) if mois < 3 else annee
    k = ((23 * mois) // 9) + jour + 4 + annee + annee_corrigee // 4 - annee_corrigee // 100 + annee_corrigee // 400

    if mois < 3:
        return k % 7
    else:
        return (k - 2) % 7


semaine = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

assert semaine[jour_semaine((8, 11, 23))] == "Mercredi"
assert semaine[jour_semaine((21, 10, 7))] == "Dimanche"
assert semaine[jour_semaine((28, 10, 24))] == "Lundi"

