import random 
comp = random.randint(1,100)

tries = 0 

while True:
    user = int(input("Enter a number: "))
    tries = tries + 1 

    if comp == user: 
        print(f"Congratulations, You have won in {tries} tries")
        break
    elif comp > user: 
        print("Oops! go a little higher")
    elif comp < user: 
        print("Oops! go a little lower")
