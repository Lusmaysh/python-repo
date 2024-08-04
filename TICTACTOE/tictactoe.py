import random

# Function to print the current state of the board
def print_board(board):
    print("\n")
    print("  " + board[0] + " | " + board[1] + " | " + board[2])
    print(" ---|---|---")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print(" ---|---|---")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Function to check if a player has won the game
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the game is a draw
def check_draw(board):
    return ' ' not in board

# Function to get the move from the human player
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                return move
            else:
                print("This space is occupied!")
        except (IndexError, ValueError):
            print("Invalid move! Please enter a number between 1 and 9.")

# Function to get the move from the bot
def get_bot_move(board, bot_player):
    available_moves = [i for i, x in enumerate(board) if x == ' ']
    opponent = 'O' if bot_player == 'X' else 'X'
    
    # Check if the bot can win in the next move
    for move in available_moves:
        board_copy = board[:]
        board_copy[move] = bot_player
        if check_win(board_copy, bot_player):
            return move
    
    # Check if the opponent can win in the next move and block them
    for move in available_moves:
        board_copy = board[:]
        board_copy[move] = opponent
        if check_win(board_copy, opponent):
            return move
    
    # Choose a random move from the available moves
    return random.choice(available_moves)

# Main function to run the Tic Tac Toe game
def tic_tac_toe():
    while True:
        # Ask the user to choose to play with a Human or a Bot
        choice = input("Do you want to play with a (H)uman or (B)ot? ").upper()
        if choice in ['H', 'B']:
            break
        else:
            print("Invalid choice! Please choose 'H' for Human or 'B' for Bot.")
    
    # Initialize the board
    board = [' ' for _ in range(9)]
    
    if choice == 'B':
        # Randomly assign the player and the bot as 'X' or 'O'
        player = random.choice(['X', 'O'])
        bot_player = 'O' if player == 'X' else 'X'
        print(f"You are {player}. Bot is {bot_player}.")
    else:
        # Set default player symbol for human vs. human game
        player = 'X'
        bot_player = None
    
    # Start the game with player 'X'
    current_player = 'X'
    
    # Print the initial empty board
    print_board(board)
    
    while True:
        if choice == 'H' or (choice == 'B' and current_player == player):
            # Get the move from the human player
            move = get_player_move(board)
        else:
            # Get the move from the bot
            move = get_bot_move(board, bot_player)
        
        # Update the board with the current player's move
        board[move] = current_player
        print_board(board)
        
        # Check if the current player has won
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Entry point for the program
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    tic_tac_toe()
