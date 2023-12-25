
print("Welcome to my Computer quiz!")

playing = input("Do you want to play ? ")

if playing != "Yes":
    quit()
    
print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect")

answer = input("What does GPU stands for? ")
if answer == "Graphics Process Unit":
    print("Correct!")
else:
    print("Incorrect")

answer = input("What does RAM stands for? ")
if answer == "Random Access Memory":
    print("Correct!")
else:
    print("Incorrect")

