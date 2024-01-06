alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(e_text,e_shift,d):
    end_text = ""
    if d == "decode":
        e_shift*=-1
    for char in e_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position-e_shift
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"The {d}d text is {end_text}")
            
go_on=True
while go_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    encrypt(e_text=text,e_shift=shift,d=direction)
    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if choice=="yes":
        go_on=True
    elif choice=="no":
        go_on=False
        print("GOODBYE!")