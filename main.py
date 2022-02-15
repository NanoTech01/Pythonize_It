#sets the gamestate to play so you could play the game
playing = True

#if player selects "cancel" in the end of the game, then the loop is stopped and the game ends

while(playing == True):

  #starting line for the game
  
  print ("""
  
  You are in a land full of dragons. In front of you, you see two caves.
  In one cave, the dragon is friendly and will share his treasure with you.
  The other dragon is greedy and hungry, and will eat you on sight.
  """)

  #gives choice of which cave to enter + changes answer to a number

  answer = input("Which cave will you go into? (1 or 2): ")
  #prevents user to enter anything other then 1 or 2, if so, it replays question and changes it back to a number

  while(answer != "1" and answer != "2"):
    answer = input("Which cave will you go into? (1 or 2): ")

  if(answer == "1"):
    path = 1
  else:
    path = 2

  #generates random value for the dragon to determine if the player wins or loses
  import random
  rand = random.randint(1, 2)
  
  #dialouge for the game

  print("""
  """)
  print ("You approach the cave…")
  print ("It is dark and spooky…")
  print ("A large dragon jumps out in front of you! He opens his jaws and...")

  #if the player's answer and the random number match up, it replys the winning ending. If not, then it's the bad ending. Both endings ask if you want to play again

  if(path == rand):
    print ("Gives you a treasure")
    retry = input("Do you want to play again? (yes or no): ")
  else:
    print ("Gobbles you down in one bite!")
    retry = input("Do you want to play again? (yes or no): ")   

  retry.lower()

  while(retry != "yes" and retry !=  "no"):
    retry = input("Do you want to play again? (yes or no): ")
    retry.lower()

  if (retry == "no"):
    playing = False
  elif (retry == True):
    playing = True