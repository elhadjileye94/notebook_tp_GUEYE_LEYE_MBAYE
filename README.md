# notebook_tp_GUEYE_LEYE_MBAYE
INTRODUCTION
Dans le cadre  de l'évaluation de l'UE DEVELOPPEMENT LOGICIEL (partie python), un projet  composé de deux parties nous a été soumis. Une première partie concernant le jeu de la vie qui est un automate cellulaire mise au point par le  mathématicien britannique John Horton Conway en  1970. Et une deuxième partie qui concerne la régression logistique.
L’application de ce travail pratique sera faite avec le logiciel Python.
PARTIE 1
Dans cette partie nous allons mettre en  œuvre l’exercice 1 du TP.
Etape 1 : Implémentation sans numpy.
On applique la fonction donnée calcul_nb_voisins à Z pour calculer le nombre de voisins des cellules de Z. A la sortie on obtient N-nombre_de_voisin.
Nous avons aussi comme donnée la fonction  iteration_jeu qui applique les règles du  jeu sur la graine Z pour donner la génération suivante. On va utiliser la fonction subplot et imshow de matplotlib pour faire l’affichage  graphique de certains  nombre d’étapes du jeu.
Etape 2 : Implémentation avec  numba.
Nous reprenons la section précédente avec des fonctions qui utilisent « numba » et la compilation « jit » dont nous proposons un protocole pour voir son effet sur le temps de calcul.
Remarque : Pour la comparaison des temps de calcul, on voit qu’après un « Restart_and_Run_all», la fonction « iteration » qui utilise la fonction « jit » a un plus grand temps d’exécution mais après une deuxième exécution cette fonction a un temps  d’exécution plus petit que  la fonction « iteration » d’origine. Ceci est dû  au fait que pour une première exécution l’importation de la fonction « jit » impacte sur le  temps d’exécution.
Nous avons aussi  créé un « widget » qui permet au curseur de contrôler les itérations du jeu avec comme graine initiale la matrice Z_huge.
PARTIE 2
On va s’intéresser dans cette partie à la régression logistique.
Nous travaillons avec les  données MNIST que nous allons charger via la commande «from sklearn.datasets import fetch_openml ».
On va transformer les données X et y pour ne garder que les chiffres 3 et 7 de ces données en utilisant la fonction « mask ». Ainsi nous visualisons un exemple de chaque classe d’image avec la commande « imshow ».
Nous effectuons une classification sur l’intégralité des données avec la fonction « logisticRegression ». 
On propose un widget qui investigue l’impact de  la transformation de  l’image  par l’opération donnée dans le tp.
On a créé un film,  importé en HTML dans le notebook, qui représente l’évolution de l’image.
REMARQUE : L’affichage de ce film nécessite « MovieWriter (ffmpeg) qui n’arrive pas à fonctionner avec la version de notre  jupyter. 
Nous proposons enfin une ACP pour visualiser  la base de  données dans un espace de dimension 2. Nous classons ainsi les classes d’images.
