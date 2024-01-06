import random
print('LETS PLAY ROCK PAPER SCISSOR !!')

user_choice=input("Choose from ~ ROCK, PAPER & SCISSOR : ").lower()

list=['ROCK','PAPER','SCISSOR']
length=len(list)

c_choice=random.randint(0,length-1)

random_choice= list[c_choice].lower()


print(f"'{user_choice}' AGAINST '{random_choice}'")

if user_choice == random_choice:
    print("DRAW !!")
elif user_choice=='paper':
    if random_choice=='rock':
        print(f"you WIN !!")
    else:
        print(f"you LOOSE ~")    
elif user_choice=='rock':
    if random_choice=='scissor':
        print(f"you WIN !!")
    else:
        print(f"you LOOSE ~")  
elif user_choice=='scissor':
    if random_choice=='paper':
        print(f"you WIN !!")
    else:
        print(f"you LOOSE ~")  
else:
    print("PLEASE ENTER VALID INPUT...")
