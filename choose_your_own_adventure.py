name = input ("Please enter your name")
print("Welcome", name, "to this adventure!")

answer = input( "You are on a dirt road. Which way would you like to go ? ").lower

if answer == "left":
    answer = input("You come to a river, you can walk over and swim. Do you want to walk or swim?")
    if answer == "swim":
        print("You sqim across and were eaten by a crocodile")
    elif answer == "walk":
        print("You walked and ran out of water.")
    else:
        print("Not Valid")

elif answer == "right":
    print()
else:
    print( "Not valid Answer")

# You can innovate and make it more difficult 
