import random
def generate():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare_score(u_score,c_score):
    if u_score>21 and c_score>21:
        return "You went over.You lose."
    
    if u_score == c_score:
        return "Draw."
    elif u_score == 21:
        return "YOU WIN."
    elif c_score == 21:
        return "YOU LOSE."
    elif c_score == 0:
        return "You lose opponent has Blackjack."
    elif u_score == 0:
        return "You win with Blackjack."
    elif u_score > 21:
        return "You went over. You lose."
    elif c_score > 21:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose."

def play_game():
    user_cards=[]
    computer_cards=[]
    go_on=True

    for _ in range(2):
        user_cards.append(generate())
        computer_cards.append(generate())
    
    while go_on:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"User cards are: {user_cards} and score is: {calculate_score(user_cards)}")
        print(f"Computer's first cards is: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            go_on=False
        else:
            choice=input("Type 'y' to get another card or to quit type 'n': ").lower()
            if choice=="y":
                user_cards.append(generate())
            else:
                go_on=False
        
    while computer_score !=0 and computer_score < 17:
        computer_cards.append(generate())
        computer_score=calculate_score(computer_cards)

    print(f"Final user cards are: {user_cards} and score is: {user_score}")
    print(f"Final computer cards are: {computer_cards} and score is: {computer_score}")
    print(compare_score(user_score,computer_score))

        
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("~~THE BLACKJACK GAME~~")
    play_game()