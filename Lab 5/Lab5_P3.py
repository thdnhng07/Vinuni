# Take two inputs: the current position of a piece and the move position
place = input()  # Example input: 'e4'
move = input()   # Example input: 'f5'

# Extract the letter (column) and number (row) from the current position
letter_place = place[0]  # Extract the column letter from 'place', e.g., 'e'
num_place = int(place[1])  # Extract the row number from 'place' and convert it to an integer, e.g., 4

# Extract the letter (column) and number (row) from the move position
letter_move = move[0]  # Extract the column letter from 'move', e.g., 'f'
num_move = int(move[1])  # Extract the row number from 'move' and convert it to an integer, e.g., 5

# Convert the column letters to their ASCII values to compare their positions
ord_letter_place = ord(letter_place)  # Get the ASCII value of the column letter in 'place', e.g., ord('e') = 101
ord_letter_move = ord(letter_move)    # Get the ASCII value of the column letter in 'move', e.g., ord('f') = 102

# Check if the row number of the move is adjacent or the same as the current position
if num_place == num_move + 1 or num_place == num_move or num_place == num_move - 1:
    # Check if the column letter of the move is adjacent or the same as the current position
    if ord_letter_place == ord_letter_move + 1 or ord_letter_place == ord_letter_move - 1 or ord_letter_place == ord_letter_move:
        print(True)  # If both row and column are adjacent or the same, the move is valid (output True)
    else:
        print(False)  # If the columns are not adjacent, the move is invalid (output False)
else:
    print(False)  # If the rows are not adjacent, the move is invalid (output False)
