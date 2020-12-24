import random
rand = random.randint(1,9)

print("Number Guessing game")
print("Guess a number from 1-9")

chance = 5

while(chance >= 1):
    number = int(input("enter your guess : "))
    chance = chance - 1
    if (chance==0):
        if(number == rand):
            print("Congratulations! You Win")
            break
        else:
            print("Your chances are over . The correct number is", rand)
            break
    else:
        if(number == rand):
           print("Congratulations! You Win")
           break
        elif(number > rand):
           print("Your guess was high : Choose a number lower than", number)
        elif(number < rand):
           print("Your guess was low : Choose a number higher than", number)
        



           



