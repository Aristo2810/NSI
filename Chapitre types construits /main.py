"""
Auteur : Enis Béziau
Correction des exercices sur les listes et les tuples
Pour trouver un exo particulier, utiliser l'outil de recherche car exos dans le désordre
"""
import random


def convert1(duree):
    """
    Renvoie le nombre de seconde dans la durée donnée en argument
    :param tuple[int, int, int] duree: tuple comportant les heures, minutes et secondes
    :return: le nombre de seconde
    :rtype: int
    """
    heure, minute, seconde = duree[0], duree[1], duree[2]

    assert heure >= 0
    assert 0 <= minute < 60
    assert 0 <= seconde < 60

    return heure * 3600 + minute * 60 + seconde


assert convert1((3, 20, 5)) == 12_005
assert convert1((23, 43, 18)) == 85_398
assert convert1((4, 8, 50)) == 14_930


def convert2(nbr_seconde):
    """
    Cette fonction renvoie le nombre d'heure, minute et seconde d'un nombre de seconde donné en argument
    :param int nbr_seconde: le nombre de seconde, strictement positif
    :return: un tuple format (heure, minute, seconde)
    :rtype: tuple[int, int, int]
    """
    assert nbr_seconde >= 0

    heure = nbr_seconde // 3600  # On calcule le nombre d'heure entière
    minute = (nbr_seconde % 3600) // 60  # On prend les heures pas entières qu'on divise par 60
    seconde = nbr_seconde % 60  # On prend les secondes qui sont pas des minutes entières

    return heure, minute, seconde


assert convert2(12_005) == (3, 20, 5)
assert convert2(85_398) == (23, 43, 18)
assert convert2(14_930) == (4, 8, 50)


# Exercice 11
def initiale(nom, prenom):
    """
    Cette fonction renvoie les initiales du nom et du prénom donné en paramètre
    :param str nom: le nom dont on doit retourné l'initiale
    :param str prenom: le prénom dont on doit retourné l'initiale
    :return: les initiales
    :rtype: str
    """
    return nom[0] + '.' + prenom[0]


assert initiale('Ravier', 'Christophe') == 'R.C'
assert initiale("Béziau", "Enis") == "B.E"
assert initiale("Michel", "Jean") == "M.J"


def initiale2(chaine):
    """
    Renvoie les initiales d'un nom donné en argument
    :param str chaine: La chaine de caractère contenant le prénom et le nom
    :return: Les initiales
    :rtype: str
    """
    return chaine.split()[0][0] + '.' + chaine.split()[-1][0]


assert initiale2('Dupont Jean-Paul') == "D.J"


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


# Exercice 13
def bintodec(nombre):
    """
    Renvoie l'écriture base 10 du nombre passé en argument
    :param str nombre: chaine de caractère composé uniquement de 0 ou de 1
    :return: L'écriture base 10
    :rtype: int
    """
    total = 0
    for index in range(len(nombre)):
        chiffre = nombre[-1 - index]
        total += int(chiffre) * 2**index
    return total


assert bintodec("010110") == 22
assert bintodec("01001101") == 77
assert bintodec("00000000") == 0


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
    :rtype: list[int]
    """
    assert nombre >= 0, "Le nombre doit etre positif"

    if nombre == 0:
        return []
    elif nombre == 1:
        return [1]
    else:
        liste = [1] * nombre
        liste[0], liste[1] = 1, 1

        for index in range(2, len(liste)):
            liste[index] = liste[index - 1] + liste[index - 2]

        return liste


assert fibonnaci(0) == []
assert fibonnaci(1) == [1]
assert fibonnaci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# Exercice 22
def euro_million():
    """
    :return: La liste des numéros de l'euroMillion généré aléatoiremment
    :rtype: list[int]
    """
    tab = [0] * 5

    for index in range(3):
        tab[index] = random.randint(1, 50)

    for index in range(2):
        tab[-1 - index] = random.randint(1, 12)

    return tab


# Exercice 25
def mini(tab):
    """
    :param list[int] tab: La liste à analyser
    :return: Le plus petit élement du tableau passé en paramètre
    :rtype: int
    """
    assert tab
    minimum = tab[0]
    for element in tab:
        if element < minimum:
            minimum = element
    return minimum


assert mini([-8, 9, 7, 4, 5]) == -8
assert mini([100, 7, 21, 14, 29]) == 7


def mini_bis(tab):
    """
    :param list[int] tab: Le tableau à analyser
    :return: le plus petit élement du tableau et son indice
    :rtype: tuple[int, int]
    """
    assert tab
    minimum = tab[0]
    minimum_index = 0
    for index, element in enumerate(tab):
        if element < minimum:
            minimum = element
            minimum_index = index
    return minimum_index, minimum


assert mini_bis([-8, 9, 7, 4, 5]) == (0, -8)
assert mini_bis([100, 7, 21, 14, 29]) == (1, 7)


# Exo cours 1
def ajoute_double(tab):
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


# Exercice 30
def addition_tableau(tab1, tab2):
    """
    :param list[int] tab1: Le premier tableau
    :param list[int] tab2: Le second tableau
    :return: additionne les éléments de deux tableaux de même longueur
    :rtype: list[int]
    """
    assert len(tab1) == len(tab2)

    long = len(tab1)
    tableau_additionne = [0 for _ in range(long)]

    for index in range(long):
        tableau_additionne[index] = tab1[index] + tab2[index]
    return tableau_additionne


assert addition_tableau([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
assert addition_tableau([90, 132], [-1, -2]) == [89, 130]
assert addition_tableau([0], [0]) == [0]


# Exercice 28
def nbr_zero_consecutif(tab):
    """
    :param list[int] tab: Le tableau à parcourir
    :return: Le plus grand nombre de 0 consécutif dans tab
    :rtype: int
    """
    compteur_zero_courant = 0
    max_zero_consecutif = 0

    for element in tab:
        if element == 0:
            compteur_zero_courant += 1
            if compteur_zero_courant > max_zero_consecutif:
                max_zero_consecutif = compteur_zero_courant
        else:
            compteur_zero_courant = 0
    return max_zero_consecutif


assert nbr_zero_consecutif([0, 1, 1, 2, 0, 0, 0, 5, 0, 0]) == 3
assert nbr_zero_consecutif([1, 2, 5]) == 0
assert nbr_zero_consecutif([0, 0, 0, 0, 1, 0, 0, 1, 0, 0]) == 4


# Exercice 27
def prefixe(tab1, tab2):
    """
    :param list[int] tab1: Le premier tableau
    :param list[int] tab2: Le deuxième tableau
    :return: True si le tableau tab2 commence par les éléments du tableau tab1 dans l’ordre et False sinon
    """
    assert len(tab2) >= len(tab1)
    assert tab1

    for index in range(len(tab1)):
        if not tab1[index] == tab2[index]:
            return False
    return True


assert prefixe([1, 2, 3], [1, 2, 3, 4, 5, 6])
assert not prefixe([2, 8, 9], [2, 8, 1, 9, 3])
assert prefixe([-1], [-1, 9, 10])


# Exercice 31
def echange(tab, i, j):
    """
    :param list[int] tab: Le tableau à parcourir
    :param int i: Le premier index
    :param int j: Le second index
    :return: le tableau tab en échangeant les valeurs tab[i] et tab[j]
    :rtype: tab[int]
    """
    assert tab
    assert i <= len(tab) - 1
    assert j <= len(tab) - 1

    tab[i], tab[j] = tab[j], tab[i]
    return tab


assert echange([1, 2, 3, 4], 0, 3) == [4, 2, 3, 1]
assert echange([-1, 9, 2, 10, 9, 2], -3, 2) == [-1, 9, 10, 2, 9, 2]
assert echange([0, 1], 0, 1) == [1, 0]
