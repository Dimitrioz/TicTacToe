def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):  # Check diagonals
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def print_scoreboard(score_x, score_o):
    print("\nScoreboard:")
    print(f"Player X: {score_x} | Player O: {score_o}\n")

def main_menu():
    score_x = 0
    score_o = 0
    while True:
        print("\nTic Tac Toe")
        print("1. Play")
        print("2. How to Play")
        print("3. Credits")
        print("4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            score_x, score_o = main_game(score_x, score_o)
        elif choice == '2':
            how_to_play()
        elif choice == '3':
            credits()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def how_to_play():
    print("\nHow to Play:")
    print("The game is played on a grid that's 3 squares by 3 squares.")
    print("Player 1 is X, Player 2 (or computer) is O.")
    print("Players take turns putting their marks in empty squares.")
    print("The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.")
    print("When all 9 squares are full, the game is over.")
    input("Press Enter to return to the main menu.")

def credits():
    print("\nCredits:")
    print("Tic Tac Toe Game developed by Dimitrios Gkoro.")
    input("Press Enter to return to the main menu.")

def main_game(score_x, score_o):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        
        # Get valid row input
        while True:
            try:
                row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
                if row in [0, 1, 2]:
                    break
                else:
                    print("Invalid choice, please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input, please enter a number.")

        # Get valid column input
        while True:
            try:
                col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
                if col in [0, 1, 2]:
                    break
                else:
                    print("Invalid choice, please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input, please enter a number.")

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already taken. Choose another one.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            if current_player == "X":
                score_x += 1
            else:
                score_o += 1
            break

        if is_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
    
    print_scoreboard(score_x, score_o)
    
    # Ask if they want to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            return main_game(score_x, score_o)
        elif play_again == 'n':
            return score_x, score_o
        else:
            print("Invalid choice, please enter 'y' or 'n'.")

if __name__ == "__main__":
    main_menu()
