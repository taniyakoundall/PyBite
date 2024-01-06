print("WELCOME TO ROLLERCOASTER!!")
height=int(input("what is your height in cm? "))
if height>120:
    print("CONRATULATIONS YOU CAN RIDE ROLLERCOASTER!!")

    age=int(input("what is your age? "))
    bill=0
    if age<12:
        bill=5
        print("Pay $5 ")
    elif(age<=18):
        bill=7
        print("Pay $7 ")
    else:
        bill=12
        print("Pay $12 ")
    
    with_photo=input("Do you want to take photo with only $3? y for yes/ n for no: ")
    if with_photo=="y":
        bill+=3
    print(f"your total bill is ${bill} :)")
else:
    print("YOU HAVE TO GROW TALLER ")
