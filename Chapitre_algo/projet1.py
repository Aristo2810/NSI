# -*- coding: utf-8 -*-
"""
Auteur : Enis Béziau ; Gabriel Claude-Bouilly
Date : 5 octobre 2023
Le programme génère aléatoirement un nombre entre 1 et 1000 grace à la méthode randint() du module random
Le but du programme est de faire deviner ce nombre à l'utilisateur. Pour ce faire, il pourra entrer un nombre
Si ce nombre est entre 1 et 1000
    Si le nombre entré est égal au nombre généré aléatoirement, on affiche un message de félicitation et le nbr d'essai
    Sinon on indique que le nombre n'est pas égal et on incrémente un compteur d'essai
Sinon on refait entrer un nombre à l'utilisateur sans compter un essai
"""
import random
import os


BORNE_MIN = 0
BORNE_MAX = 1000


def generer_nombre_au_hasard(borne_1, borne_2):
    """
    :param int borne_1: La borne inférieure de l'intervalle dans lequel le nombre sera généré. La borne est inclue
    :param int borne_2: La borne supérieure de l'intervalle dans lequel le nombre sera généré. La borne est inclue
    :return: Un nombre aléatoire dans l'intervalle [borne_1 ; borne_2]
    :rtype: int
    """
    return random.randint(borne_1, borne_2)


def saisir_et_verif_proposition(borne_min_a_verif, borne_max_a_verif):
    """
    Cette fonction sert à récolter l'entrée de l'utilisateur et à vérifier si le nombre est bien compris entre 1 et 1000
    :param int borne_min_a_verif: La borne minimale de l'intervalle dans lequel doit être compris le nombre a verif
    :param int borne_max_a_verif: La borne maximale de l'intervalle dans lequel doit être compris le nombre a verif
    :return: la proposition entrée par l'utilisateur
    :rtype: int
    """
    ok = False  # Variable drapeau
    while not ok:
        proposition = int(input(f"Veuillez-entrer un nombre entre {borne_min_a_verif} et {borne_max_a_verif}\n==> "))
        ok = borne_min_a_verif <= proposition <= borne_max_a_verif
    return proposition


def verif_victoire(proposition, nombre_gagnant):
    """
    Cette fonction vérifie si le nombre entré est bien le nombre généré aléatoirement
    :param int proposition: La proposition de nombre de l'utilisateur
    :param int nombre_gagnant: Le nombre généré aléatoirement
    :return: True si le nombre entré est gagnant, False sinon
    :rtype: bool
    """
    return proposition == nombre_gagnant


def message_victoire(nbr_essai_pour_gagner):
    """
    Cette fonction sert à renvoyer un message différent à l'utilisateur en fonction de son nbr de point
    :param int nbr_essai_pour_gagner: Le nombre d'essai dont l'utilsateur a eu besoin pour trouver le nbr aléatoire
    :return: Un message de félicitations
    :rtype: str
    """
    if nbr_essai_pour_gagner == 1:
        return "Félicitation, vous avez trouvé du premier coup"
    elif nbr_essai_pour_gagner < 10:
        return "Bravo, ça ne vous a pris que {} essais"
    else:
        return "Ne te décourage pas ! Tu n'as pris que {} essais"


def jeu():
    """
    Fonction initialisant le jeu en créant une variable essai_necessaire de type int qui fait office de compteur
    Génère le nombre au hasard
    S'occupe de la boucle du jeu
    :return: Le nombre d'essai nécessaire à l'utilisateur pour trouver nombre_hasard
    :rtype: int
    """
    essai_necessaire = 1
    nombre_hasard = generer_nombre_au_hasard(BORNE_MIN, BORNE_MAX)
    print(nombre_hasard)
    proposition_joueur = saisir_et_verif_proposition(BORNE_MIN, BORNE_MAX)
    while not verif_victoire(nombre_hasard, proposition_joueur):
        proposition_joueur = saisir_et_verif_proposition(BORNE_MIN, BORNE_MAX)
        essai_necessaire += 1
    return essai_necessaire


init_jeu = jeu()
print(message_victoire(init_jeu).format(init_jeu))

rejouer = input("Voulez-vous rejouer (o/n)\n==> ")
if rejouer == 'o':
    os.system('clear')
    jeu()
else:
    print("Fin du programme...")
