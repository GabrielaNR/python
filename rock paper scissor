import random
rock = '''
    __
---'   )
      ()
      ()
      ()
---.()
'''

paper = '''
    __
---'   )
          __)
          __)
         __)
---.__)
'''

scissors = '''
    __
---'   )
          __)
       __)
      (__)
---.(___)
'''

game = [rock, paper, scissors]
user_choice = int(input("type '0' for rock, '1' for paper or '2' for scissors\n"))
if user_choice >= 3 or user_choice < 0: 
  print("You Typed an invalid number, you lose")
else: 
  print (game[user_choice])
  pc_choice = random.randint(0, 2)
  print("Computer choose: ")
  print (game[pc_choice])

#int_user = int(user_choice)
#if int_user == 0:
  #print(game[0], rock)
#elif int_user == 1:
  #print(game[1], paper)
#elif int_user == 2:
  #print(game[2], scissors)
#else:
  #print("error")

#if pc_choice == 0:
  #print(game[0], rock)
#elif pc_choice == 1:
  #print(game[1], paper)
#else:
 # print(game[2], scissors)

  #print ("-----------------------------------------------")

  if user_choice == pc_choice:
    print("draw")
  elif user_choice != pc_choice:
      if user_choice == 0 and pc_choice == 1:
        print("you lose")
      elif user_choice == 0 and pc_choice == 2:
        print("you win")
      elif user_choice == 1 and pc_choice == 0:
        print("you win")
      elif user_choice == 1 and pc_choice == 2:
        print ("you lose")
      elif user_choice == 2 and pc_choice == 0:
        print("you lose")
      elif user_choice == 2 and pc_choice == 1:
        print("you win")


#else:
  #print("else")
