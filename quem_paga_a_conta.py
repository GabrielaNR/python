names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
names_len = len(names)
random_name = random.randint(0, names_len - 1)
person_who_will_pay = names[random_name]
print(f"{person_who_will_pay} is going to buy the meal today!")
