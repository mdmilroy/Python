letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key,value in zip(letters,points)}
letter_to_points[" "] = 0
print(letter_to_points,"\n")

def score_word(word):
  word = word.upper()
  point_total = 0
  for letter in word:
    letter
    point_total += letter_to_points.get(letter,0)
  return point_total

brownie_points = score_word("brOWNiE")
print(brownie_points)

player_to_words = {"player1":["blue","TENNIS","EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER","BELLY","HUSKY"], "Prof Reader":["ZAP","COMA","PERIOD"]}

player_to_points = {}

def play_word(player, word):
  if player in player_to_words.keys():
    player_to_words[player].append(word)
    update_point_totals()
  else:
    print("Player not found.")

def update_point_totals():
  for player,words in player_to_words.items():
    player_points = 0
    for word in words:
      for letter in word:
        player_points += score_word(letter)
    player_to_points[player] = player_points
    print(str(player)+"'s score: ", player_points)

update_point_totals()
print("\n")
play_word("Prof Reader","new")
