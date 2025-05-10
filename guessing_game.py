import random   #randomn module

print("Let's Start the Game:")

def guessing_game():
    num = random.randint(1,100)
    cnt = 0

    while(True):
        guess = int(input("Guess the number: "))
        cnt += 1

        if(guess > num):
            print("The number is lower")
        elif(guess < num): 
            print("The number is higher")
        else:
            print("You have Guessed the number in attempt no:",cnt)
            break
        

guessing_game()
print("Thank you! for Playing the game")
  




