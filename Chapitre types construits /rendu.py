# Exercice 15
"""
1. typeError
2. ([7, 3], 5)
3. [3, 3]
4. TypeError
"""


# Exercice 21
def fibonnaci(nombre):
    """
    :param int nombre: nombre jusqu'auquel on génère la suite
    :return: La suite des n premiers termes de la suite de fibonnaci
    :rtype: list
    """
    assert nombre >= 0 and isinstance(nombre, int)
    tab = [1 for i in range(nombre)]
    if nombre in (0, 1):
        return tab
    else:
        for index in range(2, nombre):
            tab[index] = tab[index - 1] + tab[index - 2]
        return tab


assert fibonnaci(0) == []
assert fibonnaci(1) == [1]
assert fibonnaci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def ajoute_double(tab):
    assert tab
    taille_initiale = len(tab)
    nouveau_tableau = [0 for _ in range(taille_initiale * 2)]

    for i in range(taille_initiale):
        nouveau_tableau[i] = tab[i]
        nouveau_tableau[i + taille_initiale] = tab[i] * 2

    return nouveau_tableau


assert ajoute_double([1, 2, 3]) == [1, 2, 3, 2, 4, 6]
assert ajoute_double([8, 3, 0]) == [8, 3, 0, 16, 6, 0]
assert ajoute_double([0]) == [0, 0]


# Exo cours 2
def appartient(valeur, tab):
    assert tab
    """
    :param int valeur: La valeur dont nous devons déterminer la présence dans le tableau
    :param tuple[int] tab: Le tableau à parcourir
    :return: un booléen indiquant si element fait partie ou non du tableau
    :rtype: bool
    """
    for element in tab:
        if element == valeur:
            return True
    return False


tableau = [9, 18, 3, 7, 2]
assert appartient(3, tableau)
assert not appartient(5, tableau)
assert appartient(2, tableau)
