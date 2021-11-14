# import stud_data
class Student:
    def __init__(self,name_of_student,rollno,class_name):
        self.name_of_student=name_of_student
        self.rollno=rollno
        self.class_name=class_name
p=Student("Priya Mishra",17,"Science")
print(p.rollno)