from classstudent import Student

class Attendance(Student):
    def __init__(self,attendence,name_of_student,rollno,class_name):
       Student.__init__(self,name_of_student,rollno,class_name)
    #  super().__init__(self,name_of_student,rollno,class_name)
       self.attendence=attendence
       print(self.name_of_student,"\nRoll Number:",self.rollno,"\nhas",(attendence/340)*100,"% of Attendence")
class Marks_obtained(Student):   
    def __init__(self,name_of_student,rollno,class_name,P,C,M,cs):
        Student.__init__(self,name_of_student,rollno,class_name)
        self.P=P
        self.C=C  
        self.M=M
        self.cs=cs
        print(self.name_of_student,"\nRoll Number:",self.rollno,"\nhas scored:",(P+C*0.5+M+cs)/4,"% in",self.class_name,"class")

class Assignment_submission(Student):
    def __init__(self,name_of_student,rollno,class_name,y):
       Student.__init__(self,name_of_student,rollno,class_name)
 
       self.y=y
       if y==True:
         print(self.name_of_student,": Roll number",self.rollno,"submits the assignment on time, of subject:",self.class_name)
       else:
         print(self.name_of_student,"\t",self.rollno,"donot submits the assignment on time, of subject:",self.class_name)

p=Student("Priya Mishra",17,"Science")
print(p.name_of_student)
p_attend=Attendance(298,"Priya Mishra",17,"Science")
p_assign=Assignment_submission("Priya Mishra",17,"Science", True)