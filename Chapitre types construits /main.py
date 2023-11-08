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


