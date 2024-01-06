student_heights=input("enter the height of all the candidates: ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])


total=0
count=0

for n in student_heights:
    total+=n
    count+=1

print(round(total/count))