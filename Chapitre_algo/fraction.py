# -*- coding: utf-8 -*-
"""
Auteur : Enis Béziau 1H
Date : 12 octobre 2023
"""
def pgcd(a: int, b: int) -> int:
    """Cette fonction renvoie PGCD(a ; b) grace à l'algorithme d'Euclide"""
    while b:
        a, b = b, a % b
    return a


def ajouter_fraction(fraction1: tuple[int, int], fraction2: tuple[int, int]) -> tuple[int, int]:
    """
    Cette fonction renvoie la forme exacte d'une addition de fraction en passant par le PGCD pour mettre au meme
    denominateur et simplifier la fraction
    """
    denominateur_commun = fraction1[1] * fraction2[1] // pgcd(fraction1[1], fraction2[1])

    #  Ajustement en * le numérateur par le coefficient de * entre le denominateur commun et le dénominateur de base
    ajutement_fraction_1 = fraction1[0] * (denominateur_commun // fraction1[1])
    ajutement_fraction_2 = fraction2[0] * (denominateur_commun // fraction2[1])

    numerateur_final = ajutement_fraction_1 + ajutement_fraction_2

    # Calcul le PGCD pour en déduire par quoi diviser pour simplifier
    diviseur_commun = pgcd(numerateur_final, denominateur_commun)

    return numerateur_final // diviseur_commun, denominateur_commun // diviseur_commun


assert ajouter_fraction((0, 10), (8, 5)) == (8, 5)
assert ajouter_fraction((9, 34), (23, 4)) == (409, 68)
assert ajouter_fraction((8, 19), (5, 1)) == (103, 19)
