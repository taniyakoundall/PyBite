import random

names_string = input("Give me everybody's names, separated by a comma. ")

# Split string method
names = names_string.split(", ")

length=len(names)

random_name=random.randint(0,length-1)
random_name=names[random_name]

print(f"{random_name} is going to buy the meal today!")