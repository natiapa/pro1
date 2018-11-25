
import course_resize

import GradeAvg
import M_login
from telnetlib import DO

def InputCourse():
    
    File_C=open('courses.txt','a')
    Name_C=input('Enter Name of course:\n')
    File_C.write(Name_C)
    File_C.write(' ') 
    File_C.write(input('Enter number of seats'))
    File_C.write(' ') 
    File_C.write(input('Enter day of the course'))
    File_C.write(' ') 
    File_C.write(input('Enter hour of the course'))
    File_C.write('\n') 
    

def InputStudent():
    
    File_S=open('students.txt','w')
    File_S.write(input('Enter Id of the student:'))
    File_S.write(' ') 
    File_S.write(input('Enter first name of the student:'))
    File_S.write(' ') 
    File_S.write(input('Enter last name of the student:'))
    File_S.write(' ') 
    File_S.write(input('Enter date of birth:'))
    File_S.write(' ') 
    File_S.write(input('Enter average of the student:'))
    File_S.write('\n')
    
    
def M_login():
    print('') 
    print('press 1 to add new student\n press 2 to add new course\n press 3 to delete course\n press 4 to add more places to course\n press 5 for student averages\n')
    choice=-1
    while(choice!=0):
        choice = int(input(''))
        if choice==1:
            InputStudent()
        elif choice==2:
            InputCourse()
        elif choice==3:
            M_login.DeleteCourse()
        elif choice==4:
            course_resize.Increase_Seats()
        elif choice==5:
            GradeAvg.Average_Grades()
        else:
            print('try again') 
M_login()
        







