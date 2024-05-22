import random  # Import the random library to generate random numbers

def roll():
  """
  This function generates a random number between 1 and 6 (inclusive).

  Returns:
      int: The random number generated.
  """
  min_value = 1
  max_value = 6
  roll = random.randint(min_value, max_value)
  return roll

# Generate a random number for initial testing
value = roll()
print(value)  # Print the initial random number (optional)

while True:
  """
  This loop keeps prompting the user for the number of players until a valid input is provided (between 1 and 4).
  """
  players = input("Enter the number of players (1-4): ")
  if players.isdigit():
    players = int(players)
    if 1 <= players <= 4:
      break  # Exit the loop if a valid number of players is entered
    else:
      print("Must be between 1 - 4 players")
  else:
    print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]  # Create a list to store player scores (initialized to 0)

while max(player_scores) < max_score:
  """
  This loop continues until a player reaches the winning score (max_score).
  It iterates through each player in each round.
  """
  for player_idx in range(players):
    print("\nPlayer number", player_idx + 1, "turn has just started!\n")
    print("Your total score is:", player_scores[player_idx], "\n")
    current_score = 0

    while True:
      """
      This nested loop allows a player to keep rolling until they roll a 1 or choose to stop.
      """
      should_roll = input("Would you like to roll (y)?")
      if should_roll.lower() != "y":
        break  # Exit the inner loop if the player chooses not to roll

      value = roll()
      if value == 1:
        print("You rolled a 1! Turn done!")
        current_score = 0  # Reset current score to 0 if they roll a 1
        break  # Exit the inner loop if they roll a 1
      else:
        current_score += value
        print("You rolled a:", value)

      print("Your score this turn is:", current_score)

    player_scores[player_idx] += current_score
    print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
player_winning_idx = player_scores.index(max_score)
print("Player number", player_winning_idx + 1, "is the winner with the score", max_score)
