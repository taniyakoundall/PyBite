print("WELCOME TO TIP CALCULATOR.")
bill=float(input("what was the total bill: "))
tip=int(input("what percentage tip would you like to give? : 10, 12, or 15?"))

bill= tip/100*bill+bill


contri=input("how many people to split bill: ")
totalbill=float(bill)/int(contri)
totalbill="{:.2f}".format(totalbill)
print(totalbill)
