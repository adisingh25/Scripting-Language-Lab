class Student:

    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    
    
    def accept(self):
        self.name=input('Enter the name of the student : ')
        self.age=int(input('Enter the age of the student : '))
        for i in range(1,4):
            m=int(input(f"Enter the marks for subject {i} : "))
            self.marks.append(m)
    
    
    def details(self):
        print('Name : ', self.name)
        print('Age : ',self.age)
        print('Marks : ',self.marks)


s1 = Student('Aditya','20', [3,5,7])
s1.details()

s2= Student('','',[])
s2.accept()
s2.details()