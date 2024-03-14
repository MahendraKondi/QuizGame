name = input("Please enter your name: ")
print("Welcome to Quiz Game",name)
choice = input("Do you want to play(y/n)").lower()
score = 0
if choice != 'y':
    exit()
else:
    ques = input("What does CPU stands for: ").lower()
    if ques == 'central processing unit':
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    ques = input("What does GUI stands for: ").lower()
    if ques == 'graphical user interface':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    ques = input("How many keys are there in keyboard: ")
    if ques == '104':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        

print("You have answered" ,score,"questions")