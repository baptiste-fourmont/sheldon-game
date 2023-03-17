# Constants (Input/Output filenames)
import csv
PLAYER_INFO_FILE = 'players_infos.csv'
ROUND_0_FILE = 'round_0.csv'
MATCHES_FILE = 'matches.csv'

# Player
class Player():
    def __init__(self, name) -> None:
        self.__name = name
        self.__round = 0
        self.__actions = {}

    def next_round(self):
        self.__round += 1

    def set_action(self, round, action):
        self.actions.update({round: action})
    
    def get_action(self, round):
        return self.actions.get(round)

    def __str__(self) -> str:
        return "Player: " + self.__name + " Round: " + str(self.__round) + " Actions: " + str(self.__actions)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def round(self):
        return self.__round
    
    @property
    def actions(self):
        return self.__actions
    
    @actions.setter
    def actions(self, actions):
        self.__actions = actions
    
    @round.setter
    def round(self, round):
        self.__round = round
    
    @name.setter
    def name(self, name):
        self.__name = name

    @staticmethod
    def get_player_by_name(name, players):
        for player in players:
            if player.name == name:
                return player
        return None

class Action():

    def __init__(self, type: str) -> None:
        self.type = type

    # Return Player
    @staticmethod
    def evaluate_winner(p1, p2):
        p1_name, p2_name = p1[0], p2[0]
        p1_act, p2_act = p1[1], p2[1]

        if p1_act == p2_act:
            return p1_name if p1_name < p2_name else p2_name
        if p1_act == "SCISSORS":
            return p1_name if p2_act == "LIZARD" or p2_act == "PAPER" else p2_name
        elif p1_act == "PAPER":
            return p1_name if p2_act == "ROCK" or p2_act == "SPOCK" else p2_name
        elif p1_act == "SPOCK":
            return p1_name if p2_act == "ROCK" or p2_act == "SCISSORS" else p2_name
        elif p1_act == "LIZARD":
            return p1_name if p2_act == "SPOCK" or p2_act == "PAPER" else p2_name
        elif p1_act == "ROCK":
            return p1_name if p2_act == "SCISSORS" or p2_act == "LIZARD" else p2_name


class Tournaments():

    def __init__(self) -> None:
        self.initialize()
        # On initialise les joueurs (Liste des joueurs)
        self.players = self.set_players()
        # On initialise les actions 
        self.actions = self.set_actions()
        # On initialise les matchs
        self.matches = self.set_matches()
        self.play()

    def set_players(self):
        players = dict()
        with (open(ROUND_0_FILE, mode='r')) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                (player1, player2) = (row['Player 1'], row['Player 2'])
                if player1 not in players:
                    players[player1] = Player(player1)
                if player2 not in players:
                    players[player2] = Player(player2)
                if player1 == player2:
                    print("ERROR : %s" % (player1))
        assert(players != {})
        return players

    def set_matches(self):
        matches = []
        with (open(ROUND_0_FILE, mode='r')) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                (player1, player2) = row['Player 1'], row['Player 2']
                if player1 == player2:
                    raise ValueError("ERROR : %s" % (player1))
                else:
                    matches.append(
                        Match(self.players[player1], self.players[player2]))
        assert(matches != [])
        return matches

    # On définit un winner qui ne perd jamais
    # On suppose qu'une personne qui a perdu ne peut plus jouer
    # Sinon il faut enlever le jouer dès qu'il perd de la liste des joueurs
    def play(self):

        def unique(sequence):
            seen = set()
            return [x for x in sequence if not (x in seen or seen.add(x))]

        def pairwise(iterable):
            a = iter(iterable)
            return zip(a, a)

        winners = []
        for match in self.matches:
            winners.append(match.winner)

        # On veut garder la liste des vainqueurs en gardant l'ordre
        dico = {key: winners.count(key) for key in unique(winners)}
        if len(dico) % 2 == 0:
            res = pairwise(list(dico.keys()))
            # On a une liste de tuple de vainqueur (on peut faire un match)

            def recursif(self, winners):
                res = []
                for elt1, elt2 in winners:
                    if elt1 == None or elt2 == None:
                        raise ValueError("ERROR : %s" % (elt1))
                    m = Match(self.players[elt1], self.players[elt2])
                    res.append(m.winner)
                if len(res) == 1:
                    return res[0]
                else:
                    return recursif(self, pairwise(res))
            winner = recursif(self, res)
            print("TOURNAMENT WINNER : %s" % (winner))
        else:
            print("TOURNAMENT WINNER : %s" % (winners[0]))

    def initialize(self):
        with(open(MATCHES_FILE, mode='w')) as csvfile:
            fieldnames = ['Round', 'Winner', 'Player 1 name',
                          'Player 1 sign', 'Player 2 name', 'Player 2 sign']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    # Set the actions for each player by round
    def set_actions(self):
        with(open(PLAYER_INFO_FILE, mode='r')) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player, num, sign = row['Name'], int(row['Round']), row['Sign']
                self.players[player].set_action(num, sign)    

class Match():

    def __init__(self, p1, p2) -> None:
        self.__p1 = p1
        self.__p2 = p2
        self.__winner = self.evaluate_round()
        self.p1.next_round()
        self.p2.next_round()

    @property
    def p1(self):
        return self.__p1
    
    @property
    def p2(self):
        return self.__p2
    
    @property
    def winner(self):
        return self.__winner
    
    # We need to evaluate for eah match the action TODO
    def get_actions(self, name, round):
        return (name, self.p1.get_action(round)) if self.p1.name == name else (name, self.p2.get_action(round))

    def evaluate_round(self):
        p1 = self.get_actions(self.p1.name, self.p1.round)
        p2 = self.get_actions(self.p2.name, self.p2.round)
        winner = Action.evaluate_winner(p1, p2)
        self.log_write(self.p1.round, winner, p1[0], p1[1], p2[0], p2[1])
        return winner

    def log_write(self, round, winner, p1_name, p1_sign, p2_name, p2_sign):
        with open(MATCHES_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                                    'Round', 'Winner', 'Player 1 name', 'Player 1 sign', 'Player 2 name', 'Player 2 sign'])
            writer.writerow({'Round': round, 'Winner': winner, 'Player 1 name': p1_name,
                            'Player 1 sign': p1_sign, 'Player 2 name': p2_name, 'Player 2 sign': p2_sign})


def main() -> int:
    Tournaments()
    return 0


if __name__ == '__main__':
    main()
