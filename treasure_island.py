print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

lc_go=input('You\'re at a cross road. Where so you want to go? Type "left" or "right"')
go=lc_go.lower()
if go=="left":
    lc_w_s=input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' ti swim across.")
    w_s=lc_w_s.lower()
    if w_s=="wait":
        lc_door=input("You arrive at the island unharmed. There is a house with 3 doors. One red. one yellow and one blue. Which colour do you choose?")
        door=lc_door.lower()
        if door=="yellow":
            print('YOU FOUND THE "TREASURE"!!')
        elif door=="red":
            print("GAME OVER!!,you entered room full of fire.")
        elif door=="blue":
            print("GAME OVER!!,door straight open into sea.")
        else:
            print("Invalid input.")
    elif w_s=="swim":
        print("GAME OVER!! ,you became alligator's feast!")
    else:
        print("Invalid input.")
elif go=="right":
    print("GAME OVER!! ,you're stuck in sandquick.")
else:
    print("Invalid input")

