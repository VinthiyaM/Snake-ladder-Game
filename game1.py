import random

# Board layout: snakes and ladders as a dictionary {start: end}
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

# Function to handle player movement based on snakes and ladders
def move_player(position):
    if position in snakes:
        print(f"Oh no! You encountered a snake at {position}. Move down to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Great! You climbed a ladder at {position}. Move up to {ladders[position]}")
        return ladders[position]
    else:
        return position

# Main game function
def play_game():
    player_position = 0  # Start position
    while player_position < 100:
        input("Press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"You rolled a {dice_value}")
        
        # Move player position and check if the position exceeds 100
        player_position += dice_value
        if player_position > 100:
            player_position -= dice_value  # Don't move if it goes beyond 100
            print("Roll more carefully to land on 100!")
            continue
        
        print(f"You move to position {player_position}")
        player_position = move_player(player_position)
        
        # Check for win
        if player_position == 100:
            print("Congratulations! You've won the game!")
            break

# Start the game4
play_game()