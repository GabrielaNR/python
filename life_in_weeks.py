#esse código calcula quantas semanas você tem de vida, supondo que você morrerá aos 90 anos
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_left = 90 - int(age)
weeks_left = round(age_left * 52)
print(f"You have {weeks_left} weeks left.")
