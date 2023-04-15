import random         #La fonction import random permet l'utilisation de la fonction random.randint(0, 1) pour sélectionner un joueur aléatoire pour commencer la partie.

class TicTacToe:

    def __init__(self):  #Initialise la classe et crée un plateau vide.

        self.board = []

    def create_board(self):   #Crée un plateau vide de 3x3.

        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):   #Retourne un nombre aléatoire 0 ou 1 qui détermine quel joueur va jouer en premier.

        return random.randint(0, 1)

    def fix_spot(self, row, col, player):   #Fixe une case du plateau pour un joueur spécifique (X ou O).

        self.board[row][col] = player

    def is_player_win(self, player):       #Vérifie si le joueur spécifié (X ou O) a gagné le jeu en vérifiant toutes les rangées, colonnes et diagonales du plateau.

        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):       # Vérifie si le plateau est complètement rempli (toutes les cases sont remplies) sans qu'un joueur ait gagné.

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):  # Échange les tours des joueurs (X ou O).

        return 'X' if player == 'O' else 'O'

    def show_board(self):               #Affiche le plateau de jeu.

        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):           #Démarre le jeu en créant le plateau et en alternant les tours des joueurs jusqu'à ce qu'un joueur gagne ou que le plateau soit rempli. La fonction affiche également le plateau final et le résultat de la partie.

        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot (besh y3abi l gamer l case)
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not (t3abew les cases ou pas encore)
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player) 

        # showing the final view of board
        print()
        self.show_board()
        # starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
