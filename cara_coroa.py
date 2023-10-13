#duas versões de código com a mesma função (simular um cara ou coroa do usuário com a máquina)

import random
choice = input("Heads or Tails: \n").capitalize()

def toss_coin():
    toss = random.randint(0,1)
    if (toss == 0):
        return "Heads"
    else:
        return "Tails"

winner = toss_coin()

if(choice == winner):
  print(f"The winner is {winner}. You win.")
else:
  print(f"The winner is {winner}. You lose.")



#------------

import random
choice = input("Heads or Tails: \n")
choice_capitalized = choice.capitalize()
toss = random.randint(0,1)
if (toss == 0):
  winner = "Heads"
else:
  winner = "Tails"
if(choice_capitalized == winner):
  print(f"The winner is {winner}. You win.")
else:
  print(f"The winner is {winner}. You lose.")
