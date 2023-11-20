# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      year = "Leap year"
    else:
      year = "Not leap year"
  else:
    year = "Leap year"
else:
  year = "Not leap year"

print(year)
