"""
auteur : Enis Béziau 1H
Date : 15/09/23
Le programme génère un nombre aléatoire compris dans un intervalle à déterminer
Il demande ensuite à l'utilisateur d'entrer un nombre et vérifie si l'entrée est valide et égale au nombre généré aléatoirement
S'il l'est, le programme s'arrête et affiche un message en fonction du nombre d'essai_necessaires nécessai_necessairere. Incrémente le compteur d'essai_necessaire sinon
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



def verifier_victoire(proposition: int, nbr_a_trouver: int) -> bool:
    """
    Retourne True si la proposition est égal au nbr_a_trouver, False sinon
    """
    return proposition == nbr_a_trouver


def message_victoire(nbr_essai_necessaire: int) -> str:
    """
    Renvoie un message personnalisé en fonction du nbr de tentatives dont 
    l'utilisateur a eu besoin pour trouver le mot
    """
    if nbr_essai_necessaire == 1:
        print(f"Félicitations !\nVous n'avez eu besoin que d'un seul essai")
    elif nbr_essai_necessaire <= 10:
        print(f"Pas mal !\nVous avez eu besoin de {nbr_essai_necessaire} essais")
    else:
        print(f"Vous ferez mieux la prochaine fois\n{nbr_essai_necessaire} ont été nécessaire")


def jeu():
    """
    Code principal du jeu qui gère la boucle principale et la définition des variables
    """
    essai_necessaire = 0
    nbr_aleatoire = generer_nombre_au_hasard(1, 1000)
    print(nbr_aleatoire)
    proposition_joueur = saisir_proposition()
    while not verifier_victoire(proposition_joueur, nbr_aleatoire):
        proposition_joueur = saisir_proposition()
        essai_necessaire += 1
    return essai_necessaire + 1


jeu = jeu()
message_victoire(jeu)
rejouer = input("Voulez-vous rejouer ? (o/n)\n==> ")
if rejouer == "o":
    jeu()