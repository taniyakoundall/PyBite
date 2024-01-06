print("!!LOGO!!")
bid={}
go_on=True

def highest_bid(biid):
    high_b=0
    winner=""
    for koe in biid:
        biiid=biid[koe]
        if biiid>high_b:
            high_b=biiid
            winner=koe  
    print(f"the winner is {winner} with ${high_b}")   

while go_on:
    name=input("What's your name?\n")
    amount=int(input("Enter the bid amount:\n$"))
    bid[name]=amount

    choice=input("Is there another bidder? 'yes' or 'no'\n")
    if choice=="yes":
        go_on=True
    elif choice=="no":
        highest_bid(bid)
        go_on=False
        