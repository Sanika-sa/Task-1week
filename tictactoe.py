import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
        self.scores = {"Wins": 0, "Losses": 0, "Ties": 0}

    def print_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\nPositions are 0-8 as shown below:")
        print(" 0 | 1 | 2 ")
        print("---+---+---")
        print(" 3 | 4 | 5 ")
        print("---+---+---")
        print(" 6 | 7 | 8 \n")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def check_winner(self, board, player):
        # Winning combinations
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6]            # Diagonals
        ]
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
                return True
        return False

    def evaluate(self, board):
        if self.check_winner(board, self.ai):
            return 1
        elif self.check_winner(board, self.human):
            return -1
        return 0

    def minimax(self, board, depth, is_maximizing):
        # Terminal states
        if self.check_winner(board, self.ai):
            return 10 - depth
        if self.check_winner(board, self.human):
            return depth - 10
        if not ' ' in board:
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for move in [i for i, spot in enumerate(board) if spot == ' ']:
                board[move] = self.ai
                eval = self.minimax(board, depth + 1, False)
                board[move] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for move in [i for i, spot in enumerate(board) if spot == ' ']:
                board[move] = self.human
                eval = self.minimax(board, depth + 1, True)
                board[move] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def ai_move(self):
        best_score = -math.inf
        best_move = None
        for move in self.available_moves():
            self.board[move] = self.ai
            score = self.minimax(self.board, 0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        self.board[best_move] = self.ai

    def play_game(self):
        print("=" * 50)
        print("🤖 Welcome to AI-Based Tic-Tac-Toe (Minimax Algorithm)")
        print("=" * 50)

        while True:
            self.board = [' ' for _ in range(9)]
            current_player = 'X' # Human goes first

            while self.empty_squares():
                self.print_board()
                print(f"Scoreboard -> Wins: {self.scores['Wins']} | Losses: {self.scores['Losses']} | Ties: {self.scores['Ties']}")
                
                if current_player == self.human:
                    try:
                        move = int(input("Your turn (Enter position 0-8): "))
                        if move not in self.available_moves():
                            print("Invalid move! Position already taken or out of range. Try again.")
                            continue
                    except ValueError:
                        print("Please enter a valid integer between 0 and 8.")
                        continue
                    
                    self.board[move] = self.human
                    if self.check_winner(self.board, self.human):
                        self.print_board()
                        print("🎉 Congratulations! You beat the AI!")
                        self.scores["Wins"] += 1
                        break
                    current_player = self.ai
                else:
                    print("AI ('O') is thinking...")
                    self.ai_move()
                    if self.check_winner(self.board, self.ai):
                        self.print_board()
                        print("🤖 AI wins! Better luck next time.")
                        self.scores["Losses"] += 1
                        break
                    current_player = self.human
            
            if not self.empty_squares() and not self.check_winner(self.board, self.human) and not self.check_winner(self.board, self.ai):
                self.print_board()
                print("🤝 It's a tie!")
                self.scores["Ties"] += 1

            play_again = input("\nDo you want to play another round? (y/n): ").lower().strip()
            if play_again != 'y':
                print(f"\nFinal Scoreboard -> Wins: {self.scores['Wins']} | Losses: {self.scores['Losses']} | Ties: {self.scores['Ties']}")
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()