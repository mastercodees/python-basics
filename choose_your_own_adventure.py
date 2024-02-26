name = input("Type your name: ")

print("welcome",name,"to this adventure")

answer = input("You are on a dirt road, it has  come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? type walk to walk around and swim to swim  across: ")
    if answer == "swim":
      
      print("you swam across and was eaten by an allegator.")

    elif answer == "walk":

        print("you walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid choice you loose.")

elif answer == "right":

    answer = input("you have come to a bridge it looks wabbly, do you want to cross it or not (cross/back)")
    if answer == "back":
      
      print("you go back and lose.")

    elif answer == "cross":

        answer = input("you cross the bridge and meet a stranger. Do ypu talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. you WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. YOU LOOSE")
        else:
            print("Not a valid choice you loose.")
    else:
        print("Not a valid choice you loose.")

else:

    print("Not a valid choice you loose.")

print("Thank you for trying", name)