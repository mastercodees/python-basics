import random

top_of_range = input("Enter your number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)  

    if top_of_range <= 0:
        print("please enter a number greater than 0")
        quit()
else:
    print("please enter a number next time!")
    quit()

random_number = random.randint(0,top_of_range)
print(random_number)
guess = 0;
while True:
    guess+=1;
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
      user_guess = int(user_guess)  
    else:
     print("please enter a number next time!")
     continue

    if user_guess == random_number:
       print("you got it!")
       break

    elif user_guess > random_number:
          print("You were above the number!")
    else:
          print("you were below the number!")
          
 
print("you got in", guess , "guesses")