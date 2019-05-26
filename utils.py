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
        
def predir(x):
    """
    La fonction predir reçoit en entrée l'image x et renvoie l'image x et une prédiction de cette image.
    """
    a=np.dot(W,x)
    if a>0:
        print("la classe de l'image est 7")
    else:
        print("la classe de l'image est 3")
    plt.imshow(np.matrix(x).reshape(28,28), cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()
    
    #################################################################################################

def fig_digit(alpha):
    """
    La fonction fig_digit reçoit en entrée un paramètre alpha et utilise l'image associée au chiffre 7 et
    nous renvoie la transformation de cette image.
    """
    x=X7[2]
    x_mod=x-alpha*(np.dot(W,x)/np.dot(W,W.T))*W
    plt.title('image modifier ')
    plt.imshow(np.matrix(x_mod).reshape(28,28), cmap=plt.cm.gray_r, interpolation='nearest')
    plt.show()
