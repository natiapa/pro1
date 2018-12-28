def Main_Menu():
    print('for manager press 1,for worker press 2, for student press 3')
    choice = int(input(''))
    if choice==1:
        M_login()
    elif choice==2:
        W_login()
    elif choice==3:
        S_login()
    else:
        print('Invalid Choice')
    Main_Menu()
def M_login():
    print('press 1 to add new student')
    print('press 2 to add new course')
    print('press 3 to delete course')
    print('press 4 to add more places to course')
    print('press 5 for student averages')
    print('press 6 to send message')
    print('press 7 to check messages')
    print('press 8 to see students details')
    choice=-1
    while(choice!=0):
        choice = int(input(''))
        if choice==1:
            InputStudent()
        elif choice==2:
            InputCourse()
        elif choice==3:
            DeleteCourse()
        elif choice==4:
            Increase_Seats()
        elif choice==5:
            Average_Grades()
        elif choice==6:
            Outbox()
        elif choice==7:
            Inbox()
        elif choice==8:
            Show_students_details()
        else:
            print('try again') 
        M_login()
        
def W_login():
    print('press 1 to ')
    print('press 2 to ')
    print('press 3 to ')
    print('press 4 to ')
    print('press 5 for ')
    print('press 6 to send message')
    print('press 7 to check messages')
    print('press 8 to see students details')
    choice=-1
    while(choice!=0):
        choice = int(input(''))
        """if choice==1:
            
        elif choice==2:
            
        elif choice==3:
            
        elif choice==4:
            
        elif choice==5:"""
        
        if choice==6:
            Outbox()
        elif choice == 7:
            Inbox()
        elif choice==8:
            Show_students_details()
        else:
            print('try again') 
        W_login()
        
def S_login():
    print('press 1 to ')
    print('press 2 to ')
    print('press 3 to ')
    print('press 4 to ')
    print('press 5 for ')
    print('press 6 to send message')
    print('press 7 to check messages')
    choice=-1
    while(choice!=0):
        choice = int(input(''))
        """if choice==1:
            
        elif choice==2:
            
        elif choice==3:
            
        elif choice==4:
            
        elif choice==5:
        """
        if choice==6:
            Outbox()
        elif choice == 7:
            Inbox()
        else:
            print('try again') 
        S_login()
def InputStudent():
    
    File_S=open('students.txt','a')
    File_S.write(input('Enter Id of the student:'))
    File_S.write(' ') 
    File_S.write(input('Enter first name of the student:'))
    File_S.write(' ') 
    File_S.write(input('Enter last name of the student:'))
    File_S.write(' ') 
    File_S.write(input('Enter date of birth:'))
    File_S.write(' ') 
    File_S.write(input('Enter subjects and grades of the student:'))
    File_S.write(' ') 
    File_S.write(input('Enter average of the student:'))
    File_S.write('\n')
    
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
    File_C.write(input('Enter IDs of the students'))
    File_C.write('\n') 
    
def Increase_Seats():
    course = input("Enter course name: ")
    if Validate_Course(course):
        size = int(input("Enter new course size: "))
        return Update_File(course,size)
    else:
        print("Invalid Course")
        return False
    
def Validate_Course(course):
    file = open("courses.txt",'r')
    for line in file:
        if course == line.split(' ')[0]:
            file.close()
            return True
    file.close()
    return False

def Update_File(course,size):
    file = open("courses.txt",'r')
    courses = [line for line in file]
    file.close()
    for i in range(len(courses)):
        crs = courses[i].split(" ")
        if crs[0]==course:
            if int(crs[1])>size:
                print("Invalid Size")
                return False
            crs[1] = str(size)
            courses[i]=" ".join(crs)
            break
    file = open("courses.txt",'w')
    for line in courses:
        file.write(line)
    file.close()
    return True

def Average_Grades():
    file = open("students.txt",'r')
    count, total = 0,0
    for line in file:
        count+=1
        total+=int(line.split(' ')[-1])
    return total/count
def delete_course (nameOfCourse):
    fr = open('Courses.txt', 'r')
    Course = fr.read()
    lineOfCourse = str(Course).split("\n")
    i=0
    line = "start"
    newtxt = ""
    while(line[0] != "end"):
        line = lineOfCourse[i].split(" ")
        nameOfSamCourse = line[0]
        if(nameOfCourse != nameOfSamCourse):
            newtxt = newtxt + lineOfCourse[i]+"\n"
        i=i+1

    fr.close()

    fw = open('Courses.txt', 'w')
    fw.write(newtxt)
    fw.close()


def DeleteCourse():
    nameOfCourse = input("Please enter the name of the course: ")
    delete_course(nameOfCourse)
    
def Show_students_details():
    check=input('Enter the ID of the student of whom you would like to see details.')
    File_Check=open('students.txt','r')
    line=File_Check.readline()
    element=line.split(' ')
    while(line):
        if(element[0]==check):
            print(line)
            break    
        line=File_Check.readline()   
        element=line.split(' ')
            
    if(element[0]!= check):
        print('try again the ID is wrong')
        File_Check.close()
        Outbox()  
    File_Check.close()   
        
def Outbox():
    File_O=open('outbox.txt','a+')
    check=input('Enter to whom do you want to send the message:student/worker.')
    if check=='student':
        File_Check=open('students.txt','r')
        id=input('Enter Id of the student:')
        line=File_Check.readline()
        element=line.split(' ')
        while(line):
            if(element[0]==id):
                File_O.write(id)
                File_O.write(' ') 
                File_O.write(input('Enter the your name:'))
                File_O.write(' ') 
                File_O.write(input('Enter the message:'))
                break    
            line=File_Check.readline()   
            element=line.split(' ')
            
        if(element[0]!= id):
            print('try again the ID is wrong') 
            File_Check.close()
            Outbox() 
            
    elif check=='worker':
        File_Check=open('workers.txt','r')
        id=input('Enter Id of the worker:')
        line=File_Check.readline()
        element=line.split(' ')
        while(line):
            if(element[0]==id):
                File_O.write(id)
                File_O.write(' ') 
                File_O.write(input('Enter the your name:'))
                File_O.write(' ') 
                File_O.write(input('Enter the message:'))
                break    
            line=File_Check.readline()   
            element=line.split(' ')
            
        if(element[0]!= id):
            print('try again the ID is wrong')  
            File_Check.close()
            Outbox() 
        
    else:
        print('try again.')
        Outbox()    
    File_O.write('\n')
    File_O.close()

def Inbox():
    File_O=open('outbox.txt','r')
    id=input('Enter your ID.')
    line=File_O.readline()
    element=line.split(' ')
    while(line):
        if(element[0]==id):
            print('to ',element[0],' from ',element[1],' '.join(element[2:]).strip())
            File_O.close()
            break    
        line=File_O.readline()   
        element=line.split(' ')
            
    if(element[0]!= id):
        File_O.close()
        print('try again the ID is wrong')
        Inbox() 
        
Main_Menu()
