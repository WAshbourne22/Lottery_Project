#  Question 3
# Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery ticket.
# It should then generate seven random numbers. After comparing the two sets of numbers, the program should output a prize based
# on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random

lotteryNumbers = []

for i in range(0, 7):
    number = random.randint(1, 40)
    while number in lotteryNumbers:
        number = random.randint(1, 40)

    lotteryNumbers.append(number)

lotteryNumbers.sort()

myLotteryNumbers = []
for i in range(0, 7):
    number = int(input("Pick a number between 1 and 40: "))
    while number in myLotteryNumbers or number<1 or number>40:
        print("Number invalid, please try again")
        number = int(input("Pick a number between 1 and 40: "))

    myLotteryNumbers.append(number)

myLotteryNumbers.sort()

counter = 0
for number in myLotteryNumbers:
    if number in lotteryNumbers:
        counter +=1

if counter == 3:
    print("Congratulations, you have won £20")
elif counter == 4:
    print("Congratulations, you have won £40")
elif counter == 5:
    print("Congratulations, you have won £100")
elif counter == 6:
    print("Congratulations, you have won £10000")
elif counter == 7:
    print("Congratulations, you have won £1000000")
else:
    print("No win this time, Good luck on your next try")

print(">>> Today's lottery numbers are: ")
print(lotteryNumbers)

print(">>> Your numbers are: ")
print(myLotteryNumbers)