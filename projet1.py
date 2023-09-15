"""
auteur : Enis Béziau 1H
Date : 15/09/23
"""
import random


def generer_nombre_au_hasard(borne_inferieure: int, borne_superieure: int) -> int:
    """
    Prend en entrée deux entiers : les bornes inférieures et supérieures de l'intervalle dans lequel
    la méhtode randint du module random va choisir un nombre au hasard. L'intervalle est [borne_inferieure ; borne_superieure]
    """
    return random.randint(borne_inferieure, borne_superieure)


def saisir_proposition():
    """
    Cette fonction propose à l'utilisateur de rentrer sa proposition et vérifie que c'est bien un entier
    """
    entree = input("Veuillez-entrer un nombre \n==> ")
    if entree.strip().isdigit():
        return int(entree)
    else:
        saisir_proposition()


def verifier_victoire(proposition: int, nbr_a_trouver: int):
    return proposition == nbr_a_trouver


def message_victoire(nbr_essai: int) -> str:
    if nbr_essai == 1:
        print("Tu n'as pris qu'un essai, félicitation")
    elif nbr_essai < 10:
        print(f"{nbr_essai} essais, c'est pas si mal en soit")
    else:
        print(f"{nbr_essai} essai c'est pas mal j'av")


def jeu():
    essai = 0
    nbr_aleatoire = generer_nombre_au_hasard(1, 1000)
    print(nbr_aleatoire)
    proposition_joueur = saisir_proposition()
    while not verifier_victoire(proposition_joueur, nbr_aleatoire):
        proposition_joueur = saisir_proposition()
        essai += 1
    return essai + 1


jeu = jeu()
message_victoire(jeu)