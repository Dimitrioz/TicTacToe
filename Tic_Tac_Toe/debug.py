import os

def clear_screen():
    # Clear the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    # Print the current state of the game board
    for row in board:
        print(row)

def check_winner(board, player):
    # Check all rows, columns, and diagonals for a winning condition
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    # Check both diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    # Check if the board is full (no empty spaces)
    return all([cell != " " for row in board for cell in row])

def print_scoreboard(score_x, score_o, player1_name, player2_name):
    # Print the current scoreboard
    print("\nScoreboard:")
    print(f"{player1_name}: {score_x} | {player2_name}: {score_o}\n")

def main_menu():
    # Clear the screen and print the welcome message
    clear_screen()
    print("Welcome to Tic Tac Toe!")
    
    # Prompt players to input their names
    player1_name = input("Enter the name for Player 1 (X): ")
    player2_name = input("Enter the name for Player 2 (O): ")
    
    # Initialize scores for both players
    score_x = 0
    score_o = 0
    
    # Set the initial starting player
    starting_player = "X"

    while True:
        # Clear the screen and display the main menu options
        clear_screen()
        print("\nTic Tac Toe")
        print("1. Play")
        print("2. How to Play")
        print("3. Credits")
        print("4. Quit")
        
        # Get the user's choice
        choice = input("Enter your choice: ")

        # Respond to the user's choice
        if choice == '1':
            # Start a new game
            score_x, score_o, starting_player = main_game(score_x, score_o, player1_name, player2_name, starting_player)
        elif choice == '2':
            # Display instructions on how to play the game
            how_to_play()
        elif choice == '3':
            # Display credits
            credits()
        elif choice == '4':
            # Quit the game
            print("Goodbye!")
            break
        else:
            # Invalid choice, prompt again
            print("Invalid choice, please try again.")

def how_to_play():
    # Clear the screen and display how to play instructions
    clear_screen()
    print("\nHow to Play:")
    print("The game is played on a grid that's 3 squares by 3 squares.")
    print("Player 1 is X, Player 2 is O.")
    print("Players take turns putting their marks in empty squares.")
    print("The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.")
    print("When all 9 squares are full, the game is over.")
    input("Press Enter to return to the main menu.")

def credits():
    # Clear the screen and display the credits
    clear_screen()
    print("\nCredits:")
    print("Tic Tac Toe Game developed by [Your Name].")
    input("Press Enter to return to the main menu.")

def main_game(score_x, score_o, player1_name, player2_name, starting_player):
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Set the current player based on who should start
    current_player = starting_player
    current_player_name = player1_name if current_player == "X" else player2_name

    while True:
        # Clear the screen and print the game board
        clear_screen()
        print_board(board)

        # Get valid row input from the current player
        while True:
            try:
                row = int(input(f"{current_player_name}, enter the row (1, 2, or 3): ")) - 1
                if row in [0, 1, 2]:
                    break
                else:
                    print("Invalid choice, please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input, please enter a number.")

        # Get valid column input from the current player
        while True:
            try:
                col = int(input(f"{current_player_name}, enter the column (1, 2, or 3): ")) - 1
                if col in [0, 1, 2]:
                    break
                else:
                    print("Invalid choice, please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input, please enter a number.")

        # Check if the chosen cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player  # Place the player's mark on the board
        else:
            print("Cell already taken. Choose another one.")
            continue

        # Check if the current player has won
        if check_winner(board, current_player):
            clear_screen()
            print_board(board)
            print(f"{current_player_name} wins!")
            if current_player == "X":
                score_x += 1
            else:
                score_o += 1
            break

        # Check if the board is full (draw)
        if is_full(board):
            clear_screen()
            print_board(board)
            print("The game is a draw!")
            break

        # Switch the current player
        current_player = "O" if current_player == "X" else "X"
        current_player_name = player2_name if current_player == "O" else player1_name

    # Print the updated scoreboard
    print_scoreboard(score_x, score_o, player1_name, player2_name)

    # Ask if players want to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            # Alternate the starting player for the next game
            starting_player = "O" if starting_player == "X" else "X"
            return main_game(score_x, score_o, player1_name, player2_name, starting_player)
        elif play_again == 'n':
            return score_x, score_o, starting_player
        else:
            print("Invalid choice, please enter 'y' or 'n'.")

if __name__ == "__main__":
    main_menu()
