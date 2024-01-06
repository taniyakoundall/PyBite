print("HERE!!, NOW ORDER YOUR PIZZA!!")
size=input("what size you want your pizza? S, M or L ?")
# add_pepperoni=input("Do you want to add pepperoni? Y or N ? ")
# cheese=input("Do you want to add cheese? Y or N ? ")
bill=0
if size=="S":
    bill=15
    print(f"your bill: {bill}")
elif size=="M":
    bill=20
    print(f"your bill: {bill}")
else:
    bill=25
    print(f"your bill: {bill}")
add_pepperoni=input("Do you want to add pepperoni? Y or N ? ")
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
        print(f"your bill: {bill}")
    else:
        bill+=3
        print(f"your bill: {bill}")
else:
    print(f"your bill: {bill}")
cheese=input("Do you want to add cheese? Y or N ? ")
if cheese=="Y":
    bill+=1
    print(f"your bill: {bill}")
# else:
#     print(f"your bill: {bill}")

print(f"your final bill is {bill}")
