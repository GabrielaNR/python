#tentativa de fazr o desafio Love Calculator do bootcamp 100 days of code Python 
#não cheguei a olhar a solução ainda, mas o código passou nos testes do auditorium kkkkk
#claro que tem maneiras melhores, mais limpas e rápidas de resolver esse exercício. pretendo ajeitá-lo quando tiver um tempinho

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2

combined_array = []
for letra in combined_names:
  combined_array.append(letra)
  score = 0
  score2 = 0
for item in combined_array:
  if item.lower() == 't':
    score += 1
  if item.lower() == 'r':
    score += 1
  if item.lower() == 'u':
    score += 1
  if item.lower() == 'e':
    score += 1
  if item.lower() == 'l':
    score2 += 1
  if item.lower() == 'o':
    score2 += 1
  if item.lower() == 'v':
    score2 += 1
  if item.lower() == 'e':
    score2 += 1
final_score = str(score) + str(score2)

int_final_score = int(final_score)
if (int_final_score < 10) or (int_final_score > 90):
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif (int_final_score >40) and (int_final_score < 50):
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")
