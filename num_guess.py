import random
ran=random.randint(1,101)
# print(ran)
# global scope variables
easy_lives=10
hard_lives=5

go_on=True

def checklives():
    """keeping up with the lives."""
    if lives<=0:
        go_on=False
        print("ran out of lives. YOU LOSE.")
        print(f"The correct number was {ran}.")
    elif lives>0:
        go_on=True
        print(f"you are left with {lives} lives.")
    
choice=input("level you want to play: 'easy' or 'hard'?")
if choice=="easy":
    lives=easy_lives
elif choice=="hard":
    lives=hard_lives
else:
    print("INVALID INPUT.")
    go_on=False

while go_on==True:
    users=int(input("enter your guess:"))
    if users==ran:
        print(f"you won,your guess= {users} vs number= {ran}.")
        go_on=False
    elif users>ran:
        print("lower")
        lives-=1
        checklives()

    elif users<ran:
        print("higher")
        lives-=1
        checklives()