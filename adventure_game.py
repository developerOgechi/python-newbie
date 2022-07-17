'''This is a programme that demonstrates an adventure game whereby the user chooses their path and can either win or loose.'''

name = input("Type your name: ")
print("Welcome", name, "to this adventure game!")

answer = input("You are on a dirt road. It has come to a dead end. Which way would you like to go?(left/right) ").lower()

if answer == "left":
    answer = input("You've come to a river. Type 'WALK' to walk around it and 'SWIM' to swim across it: ").upper()

    if answer == "SWIM":
        print("You swam across and you were eaten by an alligator.")
    elif answer == "WALK":
        print("You walked for many miles, and reached the far end of the river.")
        print("You Won!!")
    else:
        print("Not a valid option. You Loose")
            
elif answer == "right":
    answer = input("You've come to a bridge. It looks wobbly. Type 'CROSS' to cross it and 'TURN AROUND' to head back: ").upper()

    if answer == "CROSS":
        print("Wow! You fell off the bridge.")
        print("You Lost!!.")
    elif answer == "TURN AROUND":
        print("You are heading back to the dirt road.")
    else:
        print("Not a valid option. You Loose")

else:
    print("Not a valid option. You Loose")

print("Thanks for playing", name)