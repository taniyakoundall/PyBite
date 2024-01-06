import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}.')
wlen=len(chosen_word)

lives=6

display=[]
for i in chosen_word:
    display.append("_")

endgame=False

while not endgame:
    guess=input("Guess a letter: ").lower()

    for i in range(wlen):
        letter=chosen_word[i]
        if letter==guess:
            display[i]=guess

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            endgame=True
            print("Bye LOOSER !!")

    if "_" not in display:
        endgame=True
        print("Bye LOOSER !!")

    print(display)       
    print(f"only {lives} lives left.")
    print(stages[lives])
