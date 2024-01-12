"""
Auteur : Enis Béziau
Calcule exact avec des rationnels
"""

#  1) (3, 5) ; (2, 0) ; (0, 1)


def est_egal(frac1: tuple[int, int], frac2: tuple[int, int]) -> bool:
    """
    prend en argument deux tuples représentant des fractions et qui dit si les deux fractions sont égales (on renverra
    un booléen).
    """
    assert frac1[1] != 0
    assert frac2[1] != 0
    if frac1[0] * frac2[1] == frac1[1] * frac2[0]:
        return True
    return False


assert est_egal((1, 2), (2, 4))
assert est_egal((10, 20), (1, 2))
assert est_egal((1, 3), (30, 90))
assert est_egal((0, 12), (0, 28))


def pgcd(a: int, b: int) -> int:
    """Prend en argument deux entiers et renvoie leur PGCD"""
    nbr1 = a
    nbr2 = b
    if nbr1 < nbr2:
        nbr1, nbr2 = nbr2, nbr1
    while nbr2 != 0:
        reste = nbr1 % nbr2
        nbr1 = nbr2
        nbr2 = reste
    return nbr1


assert pgcd(910, 18) == 2
assert pgcd(1, 1902) == 1
assert pgcd(900, 900) == 900
assert pgcd(0, 0) == 0


def simplifie(frac: tuple[int, int]) -> tuple[int, int]:
    numerateur, denominateur = frac
    pgcd_frac = pgcd(numerateur, denominateur)
    return numerateur // pgcd_frac, denominateur // pgcd_frac


assert simplifie((30, 90)) == (1, 3)
assert simplifie((2, 9)) == (2, 9)
assert simplifie((70, 25)) == (14, 5)


def ajouter_fraction(fraction1: tuple[int, int], fraction2: tuple[int, int]) -> tuple[int, int]:
    """
    Cette fonction renvoie la forme exacte d'une addition de fraction en passant par le PGCD pour mettre au meme
    denominateur et simplifier la fraction
    """
    denominateur_commun = fraction1[1] * fraction2[1] // pgcd(fraction1[1], fraction2[1])

    #  Ajustement en * le numérateur par le coefficient de * entre le denominateur commun et le dénominateur de base
    numerateur_1 = fraction1[0] * (denominateur_commun // fraction1[1])
    numerateur_2 = fraction2[0] * (denominateur_commun // fraction2[1])

    numerateur_final = numerateur_1 + numerateur_2

    # Calcul le PGCD pour en déduire par quoi diviser pour simplifier
    diviseur_commun = pgcd(numerateur_final, denominateur_commun)

    return numerateur_final // diviseur_commun, denominateur_commun // diviseur_commun


assert ajouter_fraction((0, 10), (8, 5)) == (8, 5)
assert ajouter_fraction((9, 34), (23, 4)) == (409, 68)
assert ajouter_fraction((8, 19), (5, 1)) == (103, 19)
assert ajouter_fraction((1, -2), (1, 3)) == (1, -6)
assert ajouter_fraction((5, 5), (3, 3)) == (2, 1)


def multiplier_fraction(fraction1: tuple[int, int], fraction2: tuple[int, int]) -> tuple[int, int]:
    """
    Cette fonction renvoie la forme exacte d'une multiplication de fraction
    """
    numerateur = fraction1[0] * fraction2[0]
    denominateur = fraction1[1] * fraction2[1]
    pgcd_fraction = pgcd(numerateur, denominateur)
    return numerateur // pgcd_fraction, denominateur // pgcd_fraction


assert multiplier_fraction((10, 31), (2, 3)) == (20, 93)
assert multiplier_fraction((9, 1), (28, 92)) == (63, 23)
assert multiplier_fraction((0, 19), (11, 27)) == (0, 1)


def inverse(frac: tuple[int, int]) -> tuple[int, int]:
    """
    Prend en argument une fraction et renvoie son inverse (si num et denom sont diff de 0)
    """
    if frac[0] != 0 and frac[1] != 0:
        return frac[1], frac[0]
    return "undef"


assert inverse((1, 2)) == (2, 1)
assert inverse((10, 30)) == (30, 10)
assert inverse((1, 1)) == (1, 1)


def divise(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    """
    Prend en argument deux fractions retourne leur division entre elles
    """
    if frac1 == frac2:
        return (1, 1)
    fraction_2_inverse = inverse(frac2)
    return multiplier_fraction(frac1, fraction_2_inverse)


assert divise((1, 2), (1, 2)) == (1, 1)
assert divise((3, 2), (7, 6)) == (9, 7)
assert divise((10, 30), (30, 10)) == (1, 9)
    
