"""On considère le jeu suivant : on a un plateau de n cases numérotées de 0 à n−1. Un enfant écrit sur chaque case un
numéro de case (il peut écrire le même numéro sur plusieurs cases différentes ; il peut écrire le numéro d’une case
dans la case elle-même ou pas.) On place un pion sur la case numéro 0 et on procède comme suit : dans la case sur
laquelle est posée le pion, il y a un numéro. On lit le numéro, appelons le N, puis on déplace le pion jusqu’à la
case N. On recommence en déplacant le pion jusqu’à arriver sur la case numéro 1. Remarque : il est possible qu’on
déplace indéfiniment le pion sans jamais arriver sur la case 1 Exemple : imaginons que le plateau soit : 3 2 8 4 2 3
6 3 1. On démarre sur la case 0 ; il est écrit 3 donc on va sur la case 3, qui nous envoie sur la case 4,
qui nous envoie sur la case 2, qui nous envoie sur la case 8 qui nous envoie sur la case 1. En 5 coups on est donc
arrivé à la case 1.
"""


def jeu(plateau):
    """
    :param list[int] plateau: Le plateau du jeu
    :return: −1 si le jeu ne se termine pas ou le nombre de déplacements pour atteindre la case 1 s’il se termine
    :rtype: int
    """
    assert plateau != []
    pos_actuelle, nbr_coup = 0, 0
    while pos_actuelle != 1:
        if nbr_coup >= len(plateau):
            return -1
        prochaine_pos = plateau[pos_actuelle]
        pos_actuelle = prochaine_pos
        nbr_coup += 1
    return nbr_coup


assert jeu([3, 2, 8, 4, 2, 3, 6, 3, 1]) == 5
assert jeu([0, 4, 10, 2, 3]) == -1
assert jeu([1, 3, 4, 2, 3]) == 1
assert jeu([2, 1, 3, 0]) == -1
assert jeu([2, 1, 3, 1]) == 3
