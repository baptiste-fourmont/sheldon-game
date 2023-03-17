SHELDON GAME: (datascientist.fr)

# Introduction:

Dans un épisode de la série Big Bang Theory, Sheldon parle du jeu : Pierre feuille ciseaux lézard Spock.  

Les règles sont les suivantes :  

    Les ciseaux coupent la feuille
    La feuille couvre la pierre
    La pierre écrase le lézard
    Le lézard empoisonne Spock
    Spock casse les ciseaux
    Les ciseaux décapitent le lézard
    Le lézard mange la feuille
    La feuille réfute Spock
    Spock vaporise la pierre
    La pierre écrase les ciseaux

Pour les besoins de notre projet, nous considérons aussi la règle suivante :

    Lors d'une égalité, le gagnant est le joueur dont le nom est avant dans l'ordre alphabétique.

Dans un monde parallèle, il y aura bientôt des tournois de ce jeu qui vont se dérouler.  
Une équipe de data-scientist a réussis à trouver la liste des coups que vont jouer chacun des joueurs pour chaque round du tournois. 
Ils ont stocké ces coups dans des fichiers players_infos.csv avec le format suivant :
Name	Round	Sign
John	0	PAPER
John	1	LIZARD
John	2	ROCK
Jack	0	SPOCK
Jack	1	PAPER
Jack	2	ROCK
Henry	0	SCISSORS
Henry	1	SPOCK
Henry	2	LIZARD
Paul	0	PAPER
Paul	1	ROCK
Paul	2	SPOCK

Dans l'exemple ci-dessus :

    John jouera le signe PAPER lors son 1er duel
    John jouera le signe LIZARD lors son 2ème duel
    John jouera le signe ROCK lors son 3ème duel
    Jack jouera le signe SPOCK lors son 1er duel
    Jack jouera le signe PAPER lors son 2ème duel
    Jack jouera le signe ROCK lors son 3ème duel
    Henry jouera le signe SCISSORS lors son 1er duel
    Henry jouera le signe SPOCK lors son 2ème duel
    Henry jouera le signe LIZARD lors son 3ème duel
    Paul jouera le signe PAPER lors son 1er duel
    Paul jouera le signe ROCK lors son 2ème duel
    Paul jouera le signe SPOCK lors son 3ème duel

Au début d'un tournois, nous avons la liste des duels pour le premier round (round numéro 0) : dans le fichier round_0.csv. Il contient la liste des premiers matches qui vont se dérouler. Avec le format suivant :
Player 1	Player 2
Henry	Jack
Paul	John

Avec les données que nous avons ci-dessus, le tournoi se déroulera comme ceci :

Henry : SCISSORS \
                   Jack : PAPER  \
Jack  : SPOCK    /                \
                                    John is the winner
Paul  : PAPER    \                /
                   John : LIZARD /
John  : PAPER    /

Enoncé

Nous voulons un programme qui nous trouve le gagnant d'un tournois à partir de deux fichiers : players_infos.csv et round_0.csv. Le programme doit afficher le nom du vainqueur du tournois de la manière suivante :

TOURNAMENT WINNER : <Nom Du Gagnant>

Le programme doit aussi écrire la liste des matches qui se sont déroulés dans un fichier matches.csv avec les informations suivantes :

    Round : numéro du round

    Winner: gagnant du match

    Player 1 name : Nom du joueur 1

    Player 1 sign : Signe joué par le joueur 1

    Player 2 name : Nom du joueur 2

    Player 2 sign : Signe joué par le joueur 2