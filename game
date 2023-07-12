print('''
                                _._
                               .-~ | ~-.
                               |   |   |
                               |  _:_  |                    .-:~--.._
                             .-"~~ | ~~"-.                .~  |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |      |
  _..--~:-.|    |  |         |     |     |                |   |      |
 |      |  ~.   |  |         |  __.:.__  |                |   |      |
 |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
 |      A   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |      R   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |      A   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      S   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      A   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      K   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      A   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
print("Welcome to Night City.")
print("Where your dreams come true!") 
name = input("Type your name: ")

print("You're an edgerunner with a bomb who wants to destroy Arasaka. What would be your first step?? ")

step_1 = input("If you want to enter through the front door, type 'right'. \nIf you wanna try to hack the backdoor, type 'left'.\n")

step_1_lower = step_1.lower()


if step_1_lower == 'left':
  print("You successfully hacked the backdoor and made your way inside the building in stealth mode.")
  step_2 = input("You wanna put the bomb in the roof. If you wanna go through the stairs, type 'left'. If you wanna go through the elevator, type 'right'.\n")
  step_2_lower = step_2.lower() 
  if step_2_lower == 'left':
      print("You did it through the stairs.")
      step_3 = input("You succesfully install the bomb. And now you'll need run. What door you'll choose?\n Type 'red' if you choose the red door, type 'yellow' if you choose the yellow door or type 'blue' if you choose the blue door.\n" )
      step_3_lower = step_3.lower()
      if step_3_lower == 'yellow':
        print(f"The bomb exploded. You didn't escape. You turn into a Night City legend. Everyone will remember your acts while drinking {name} in Afterlife. Congratulations :D")
      elif step_3_lower == 'blue':
        print("The bomb exploded. You run. No one will never know your name. You will live the rest of your life in peace. Game over.")
      else:
        print("The bomb did not exploded. The guards found you. Adam Smasher laughs as he rips your ams off. No one will remember you. You're note special. ")

  else:
    print("Adam Smasher found you. He laughs as he rips yours amrs out. You're not special. You're just a little shit. Sorry :(")
else:
  print("The pigs found you. You're shot till death. Your name will never be a drink in Afterlife :(  ")
