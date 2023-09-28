def maximum(a, b, c):
    """
    Cette fonction renvoie la maximum entre a, b, et c.
    En cas de nombres qui sont à la fois égaux et le maximum, on renvoie la valeur d'un d'eux
    :param int a: Premier nombre
    :param int b: Deuxième nombre
    :param int c: Troisième nombre
    :return: Le maximum de a, b, c
    :rtype: int
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(maximum(12, 6, 4))
print(maximum(6, 12, 4))
print(maximum(6, 4, 12))
print(maximum(6, 12, 12))
print(maximum(12, 6, 12))
print(maximum(12, 12, 6))
print(maximum(12, 12, 12))
print(maximum(18, 12, 12))
print(maximum(12, 18, 12))
print(maximum(12, 12, 18))



def technique_russe(a, b):
    """
    Cette fonction renvoie le produit a * b grâce à une technique russe faisable à la main facilement
    :param int a: premier nombre à multiplier
    :param int b: second nombre à multiplier
    :return: Le produit de a * b
    :rtype: int
    """
    res = 0
    while a != 0:
        if a % 2 == 0:
            a /= 2
            b *= 2
        else:
            res += b
            a = (a - 1) / 2
            b *= 2
    return res
