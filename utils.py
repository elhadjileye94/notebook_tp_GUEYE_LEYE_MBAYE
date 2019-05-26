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
#######################################################################################################################
def iteration_jeu(Z):
    """
       la fonction iteration_jeu reçoit en entrée une liste de liste qui représente l'étape initiale du jeu 
       et renvoie la génération qui suis en appliquant les règles du jeu .
    """
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z
 ###########################################################################

def iter(n):
    """
      la fonction iter reçoit en entrée un entier n qui représente le nombre d'itérations souhaité 
       et renvoie les n étapes du jeu correspondant en appliquant les règles du jeu.
    """
    Z_huge = np.zeros((20, 20)) #creation
    Z_np = np.array(
    [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]])

    Z_huge[10:16, 10:16] = Z_np
    
    liste=list()
    for i in range(n):
        liste.append(iteration_jeu(Z_huge))
        plt.subplot(6,5,i+1)
        ax=plt.subplot(6,5,i+1)
        plt.setp(plt.gca(), yticklabels=[])
        plt.title('iteration {}'.format(i))
        plt.imshow(liste[i])
        plt.tight_layout(rect = [0,0, 6, 5])
        
        ##################################################################################################
        
