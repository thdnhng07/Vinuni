def convert_input(player_list):
    """
    Converts a comma-separated string of player names and scores into a list of players.
    
    Args:
        player_list (str): A string with player names and scores separated by commas, e.g., "Alice 10,Bob 15"
        
    Returns:
        list: A list of [name, score] pairs where `name` is a string and `score` is an integer.
    """
    players = []

    # Split the input string by commas and process each name-score pair
    for item in player_list.split(','):
        name, score = item.split()
        players.append([name, int(score)])  # Convert score to integer and add to players list

    return players  


def perform_operations(players, operations_str):
    """
    Performs a series of operations on the players' scores.
    
    Args:
        players (list): List of players, where each element is a [name, score] pair.
        operations_str (str): String of operations to perform, formatted as "insert Alice 10, remove Bob, adjust Alice 5".
        
    Returns:
        list: Updated list of players after performing all operations.
    """
    # Convert players list to a dictionary for easy manipulation
    players_dict = {name: score for name, score in players}

    # Process each operation in the operations string
    for operation in operations_str.split(','):
        parts = operation.strip().split()
        op, name = parts[0], parts[1]
        score = int(parts[2]) if len(parts) > 2 else 0  # Set score to 0 if not specified

        # Perform the specified operation
        if op == "insert":
            players_dict[name] = score  # Insert or update player with specified score
        elif op == "remove":
            players_dict.pop(name, None)  # Remove player if they exist
        elif op == "adjust":
            if name in players_dict:
                players_dict[name] += score  # Adjust player's score by adding specified value

    # Convert dictionary back to list of [name, score] pairs
    return [[name, score] for name, score in players_dict.items()]


def sort_players(players):
    """
    Sorts players by score in descending order and by name in ascending order for ties.
    
    Args:
        players (list): List of players, where each element is a [name, score] pair.
        
    Returns:
        list: Sorted list of players by score (descending) and name (ascending).
    """
    return sorted(players, key=lambda x: (-x[1], x[0]))


def print_sort_players(players):
    """
    Prints player names in sorted order without their scores.
    
    Args:
        players (list): Sorted list of players, where each element is a [name, score] pair.
    """
    for player in players:
        print(player[0], end=' ')


# Example usage:
player_list = input("Enter players (format: 'Name Score,...'): ")
operation = input("Enter operations (format: 'insert Name Score, remove Name, adjust Name Score,...'): ")

# Convert input string to list of players
players = convert_input(player_list)
# Perform operations on players
players = perform_operations(players, operation)
# Sort players by score (descending) and name (ascending)
sorted_players = sort_players(players)
# Print sorted player names
print_sort_players(sorted_players)
