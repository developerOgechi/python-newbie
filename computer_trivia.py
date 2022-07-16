print("Welcome to Computer Quiz Game!")


playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0


answer = input("Who is the father of Computer science? ").lower()
if answer == "Charles Babbage":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")


answer = input("Which is the common name for the crime of stealing passwords? ")
if answer == "Spoofing":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")


answer = input("What is the name of the first electronic computer? ")
if answer == "ENIAC":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")


answer = input("What does USB stand for? ")
if answer == "Universal Serial Bus":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You scored " + str((score/4) * 100) + "%.")
