class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, type, max_stud):
        self.type = type
        self.max_stud = max_stud
        self.students = []

    def add_on(self, student):
        if len(self.students) < self.max_stud:
            self.students.append(student)
            return True
        else:
            return False
        
    def get_avg(self):
        avg = 0
        for s in self.students:
            avg += s.get_grade()
        
        return avg/len(self.students)


s1 = Student("tim", 19, 95)
s2 = Student("bill", 19, 85)
s3 = Student("jim", 19, 65)

c1 = Course("science", 2)
c1.add_on(s1)
c1.add_on(s2)
c1.add_on(s3)
print(c1.get_avg())