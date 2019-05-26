# Code jeu de la vie.
def calcul_nb_voisins(Z):
    """
    la fonction calcul_nb_voisins reçoit en entrée une liste de liste
       et renvoie le nombre de voisin(s) de chaque cellule en appliquant les règles du jeu. 
    """
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                + Z[x-1][y] + 0 +Z[x+1][y] \
                + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N
