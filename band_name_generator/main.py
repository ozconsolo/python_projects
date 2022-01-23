# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_together = (name1 + name2)
score1 = 0
score2 = 0

for i in range (len(name_together)):
    if name_together[i].upper() == "T" or name_together[i].upper() == "R" or name_together[i].upper() == "U" or name_together[i].upper() == "E":

        score1 += 1

for j in range (len(name_together)):
    if name_together[j].upper() == "L" or name_together[j].upper() == "O" or name_together[j].upper() == "V" or name_together[j].upper() == "E":

        score2 += 1

total = str(score1) + str(score2)

total_int = int(total)

if total_int < 10 or total_int > 90:

    print(f"Your score is {total_int}, you go together like coke and mentos.")

elif total_int >= 40 and total_int <= 50:

    print(f"Your score is {total_int}, you are alright together.")

else:

    print(f"Your score is {total_int}.")