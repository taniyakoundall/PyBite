#addition
def addition(n1,n2):
    return n1+n2

#subtraction
def subtraction(n1,n2):
    return n1-n2

# multiplication
def multiplication(n1,n2):
    return n1*n2

#division
def division(n1,n2):
    return n1/n2

operation = {
"+": addition,
"-": subtraction,
"*": multiplication,
"/": division,
}
def calculator():
    num1=float(input("What's the first number?: "))
    
    go_on=True
    while go_on:
        for i in operation:
            print(i)

        operation_symbol=input("Pick an operation from line above: ")

        num2=float(input("What's the next number?: "))

        calculation=operation[operation_symbol]
        answer=calculation(num1,num2)


        print(f"{num1}{operation_symbol}{num2}={answer}")
        should_continue=input("Enter 'y' to continue with calculations and 'n' to quit : " ).lower()
        if should_continue=="y":
            num1=answer
        elif should_continue=="n":
            go_on=False
            calculator()
        else:
            go_on=False
            print("INVALID INPUT.")

calculator()