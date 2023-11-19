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
    :rtype: list
    """
    assert nombre >= 0 and isinstance(nombre, int)
    tab = [1] * nombre
    if nombre in (0, 1):
        return tab
    else:
        for index in range(2, nombre):
            tab[index] = tab[index - 1] + tab[index - 2]
        return tab


assert fibonnaci(0) == []
assert fibonnaci(1) == [1]
assert fibonnaci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# Exercice 22
def euro_million():
    """
    :return: La liste des numéros de l'euroMillion généré aléatoiremment
    :rtype: list[int]
    """
    numeros = [random.randint(1, 50) for _ in range(3)]
    etoiles = [random.randint(1, 12) for _ in range(2)]
    return numeros + etoiles


# Exo cours 1
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


# Exercice 23
def cherche(tab, x):
    """
    :param list tab: Le tableau à analyser
    :param int | float | str x: L'élement à chercher
    :return: l’indice de l’élément x s’il est présent dans le tableau tab et −1 s’il n’y est pas
    :rtype: int
    """
    for index in range(len(tab)):
        if tab[index] == x:
            return index
    return -1


assert cherche([1, 2, 3], 1) == 0
assert cherche(['a', 'b', 'c', 'd'], 'b') == 1
assert cherche([1.5, 1.6, 1.7], 1.8) == -1
assert cherche([9, 3, 1, -1, 0], 0) == 4


def occurrences(tab, x):
    """
    :param list tab: Le tableau à parcourir
    :param int | float | str x: L'élement dont nous devons compter l'occurrence
    :return: le nombre d’occurrences de l’élément x dans le tableau tab
    :rtype: int
    """
    occurrence_x = 0
    for element in tab:
        if element == x:
            occurrence_x += 1
    return occurrence_x


assert occurrences([1, 1, 1, 1], 1) == 4
assert occurrences(['abcdef'], 'abcde') == 0
assert occurrences([1, 9, 1, 9], 9) == 2


# Exercice 36
def nbr_record(liste):
    """
    :param list[int] liste: La liste de nombre à parcourir
    :return: Une liste comportant tous les nbr record de la liste donnée en argument
    :rtype: list[int]
    """
    assert liste
    liste_nbr_record = [liste[0]]  # Le premier nbr est toujours un nbr record

    for nombre_courant in liste:
        if nombre_courant > liste_nbr_record[-1]:
            liste_nbr_record.append(nombre_courant)


def estime_records(longueur_liste):
    """
    :param int longueur_liste: La longueur de la liste
    :return: le nombre moyens de records dans une liste de taille longueur_liste
    :rtype: float
    """
    total_nbr_record = 0

    for i in range(100_000):
        liste_aleatoire = [random.randint(1, 100) for _ in range(longueur_liste)]
        total_nbr_record += len(nbr_record(liste_aleatoire))

    return total_nbr_record / 100_000


# Exercice 39
def rectangle(largeur, hauteur):
    """
    :param int largeur: La longueur du rectangle à dessiner
    :param int hauteur: La hauteur du rectangle à dessiner
    :return: des symboles # disposés en rectangle de largeur l et de hauteur h
    :rtype: str
    """
    for ligne in range(hauteur):
        for colonne in range(largeur):
            print('#', end='')
        print()
    return None


# Exercice 29
def produit(tab, n):
    """
    :param list[int] tab: Le tableau à parcourir
    :param int n: Le coefficient multiplicateur
    :return: un nouveau tableau obtenu en multipliant chaque élément de tab par n
    :rtype: list[int]
    """
    assert isinstance(n, int)
    return [element * n for element in tab]


assert produit([1, 2, 3], 5) == [5, 10, 15]
assert produit([], 4) == []
assert produit([50, 20, -1], 0) == [0, 0, 0]


def produit2(tab, n):
    """
    Modifie le tableau tab en argument
    :param list[int} tab: Le tableau à parcourir
    :param n: Le coefficient multiplicateur
    :rtype: None
    """
    for index in range(len(tab)):
        tab[index] *= n
    return None


def moyenne(tab):
    """
    :param list[int] tab: Le tableau contenant les valeurs dont nous devons faire la moyenne
    :return: La moyenne des nombres de tab
    :rtype: float
    """
    assert tab
    total_addition_nbr = 0

    for nombre in tab:
        total_addition_nbr += nombre

    return total_addition_nbr / len(tab)


def table_hasard(nbr, borne_sup):
    """
    :param int nbr: La longueur de la liste générée au hasard
    :param borne_sup: La borne supérieure de l'intervalle [1 ; borne_sup] dans lequel sont tiréses les nbr
    :return: une liste de n nombres tirés au hasard entre 1 et max
    :rtype: list[int]
    """
    assert nbr >= 0
    assert borne_sup >= 1
    return moyenne([random.randint(1, borne_sup) for _ in range(nbr)])


# Exercice 25
def mini_tab(tab):
    """
    :param list[int] tab: Le tableau à parcourir
    :return: L'élement minimum présent dans tab
    :rtype: int
    """
    assert tab
    minimum = tab[0]
    for element in tab:
        if element < minimum:
            minimum = element
    return minimum


assert mini_tab([1, 2, 3, 4]) == 1
assert mini_tab([-1, 0, 1, 62, -13, 903]) == -13
assert mini_tab([-1, 902, -9]) == -9


def mini_tab_bis(tab):
    """
    :param list[int] tab: Le tableau d'entier à parcourir
    :return: L'indice et la valeur du minimum de tab
    :rtype: tuple[int, int]
    """
    assert tab
    index_min, element_min = 0, tab[0]
    for index in range(len(tab)):
        if tab[index] < element_min:
            element_min = tab[index]
            index_min = index
    return index_min, element_min


assert mini_tab_bis([1, 2, 3, 4]) == (0, 1)
assert mini_tab_bis([-1, 0, 1, 62, -13, 903]) == (4, -13)
assert mini_tab_bis([-1, 902, -9]) == (2, -9)


# Exercice 24
def compte_plus(tab, x):
    """
    :param list[int] tab: Le tableau à parcourir
    :param int x: l'élement
    :return: le nombre d’éléments du tableau supérieurs ou égaux à x
    :rtype: int
    """
    nbr_element = 0
    for element in tab:
        if element >= x:
            nbr_element += 1
    return nbr_element


assert compte_plus([1, 2, 3, 4], 1) == 4
assert compte_plus([0, 1, -22, 99, 103, 83, 1], 1000) == 0
assert compte_plus([9, 1, 4, 10, -13], 0) == 4
assert compte_plus([], 9) == 0


# Exercice 27
def prefixe(tab1, tab2):
    """
    :param list[int] tab1: Le premier tab
    :param list[int] tab2: Le deuxième tab
    :return: True si le tableau tab2 commence par les éléments du tableau tab1 dans l’ordre et False sinon
    :rtype: bool
    """
    assert len(tab2) > 0
    for index in range(len(tab1)):
        if not tab1[index] == tab2[index]:
            return False
    return True


assert prefixe([1, 2, 3], [1, 2, 3, 4, 5, 6])
assert not prefixe([2, 8, 9], [2, 8, 1, 9, 3])
assert prefixe([-1], [-1, 9, 10])


# Exo cours
"""
L ← [10,'bonjour', 2] ; ajouter 5 à L puis afficher L va afficher [10, 'bonjour', 2, 5]

Exemple : 
type(L) vaut list
type(L[0]) vaut int
len(L) vaut 3

L.append(5) ; L vaut [10, 'bonjour', 2, 5]
L = [3, 1] + L ; L vaut [10, 'bonjour', 2, 5, 3, 1]
L[0] = 'a' ; L vaut ['a', 'bonjour', 2, 5, 3, 1]
len(L) vaut 6



1) construire la liste des multiples de 13 inférieurs à 100
liste = []
for i in range(13, 101):
    if i % 13 == 0:
        liste.append(i)

2) On part du nombre 4 et chaque nombre est égal au double du précédent auquel on soustrait 3. Construire
la liste des 10 premiers termes ainsi définis. Même question si on veut la liste des termes inférieurs à 100
def sequence(nbr_terme):
    '''
    :param int nbr_terme: le nbr de terme que l'on veut générer
    :return: une liste contenant les termes
    :rtype: list[int]
    '''
    liste = [4]
    for i in range(nbr_terme - 1):
        liste.append(liste[i] * 2 - 3)
    return liste


type(Lbis) vaut list
type(Lbis[0]) vaut list
type(Lbis[1]) vaut int

Lbis[0][1] vaut 'bonjour'
Lbis[1][0] vaut typeError
len(Lbis) vaut 5
Lbis.append([5]) ; Lbis vaut [[10, 'bonjour', 2], 2, 10, [], [1, 2, 3], [5]]

Le slicing
L=[2,5,2,1,12]

M = L[1:3] vaut [5, 2]
M=L[1:4:2] vaut [5, 1]
M=L[1:] vaut [5, 2, 1, 12]
M=L[:2] vaut [2, 5]
M = L[:] vaut [2, 5, 2, 1, 12]
M = L[::2] vaut [2, 2, 12]
M=L[1:1] vaut []

"""