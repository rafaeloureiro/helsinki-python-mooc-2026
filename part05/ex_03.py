"""
Go game board by counting pieces.

Rules for this exercise:
- 0 represents an empty square.
- 1 represents Player 1's pieces.
- 2 represents Player 2's pieces.
- The player with the highest total number of pieces on the board wins.

Args:
    game_board (list): A 2D list of integers representing the game board.

Returns:
    int: 1 if Player 1 wins, 2 if Player 2 wins, or 0 in the event of a tie.
"""

def who_won(game_board: list) -> int:
    count_1 = 0
    count_2 = 0

    """ contagem das jogadas, 1 para o jogador 1 e 2 para o jogador 2 """

  for row in game_board:
        for item in row:
            if item == 1:
                count_1 += 1
            elif item == 2:
                count_2 += 1

  if count_1 > count_2:
      return 1
  elif count_2 > count_1:
      return 2
  else:
      return 0
