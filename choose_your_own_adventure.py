name = input("Type your name: ")

print("welcome",name,"to this adventure")

answer = input("You are on a dirt road, it has  come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? type walk to walk around and swim to swim  across: )  ")
    if answer == "swim":
      
      print()

    elif answer == "walk":

        print()
    else:
        print("Not a valid choice you loose.")

elif answer == "right":

    print()

else:

    print("Not a valid choice you loose.")