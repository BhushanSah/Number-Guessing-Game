import random
print("-----Number Guessing Game-----")
while True:
    print("Choose Difficulty Level\n1- Easy(1,50)\n2-Medium(1,100)\n3-Hard(1,500)")
    choice=input("Enter Difficulty level 1/2/3 or Quit(Q) to exit: ")
    if choice.upper()=="Q":
        exit()
    if choice.isdigit():
        if choice=="1":
            target=random.randint(1,50)
            limit=50
        elif choice=='2':
            target=random.randint(1,100)
            limit=100
        elif choice=='3':
            target=random.randint(1,500)
            limit=500
        else: 
            print("Default to medium")
            target=random.randint(1,100)
            limit=100
    else:
        print("Invalid. Enter number only ")
    Attempts=0
    while True:
        Guess= input("Enter Your Guess or Quit(q): ")
        if Guess.lower()=="q":
            exit()
        try:
            Guess=int(Guess)
        except ValueError:
            print("Numbers ONLY!!!")
        if Guess<1 or Guess>limit:
            print(f"Invalid! please Guess within limit: {limit}")
            continue 
        Attempts+=1
        if Guess==target:
            print(f"\n🎉 Congrats! You guessed it right!")
            print(f"Attempts Taken: {Attempts}")
            break
        elif Guess>target:
            print("Big Number, Guess Smaller Number")
        elif Guess<target:
            print("Small Number, Guess Bigger Number")
    Play_Again=input("Do you want to Play Again(Y/N): ")
    if Play_Again.upper()!="Y":
        break 
print("------Game Over-------\nThank You")   
