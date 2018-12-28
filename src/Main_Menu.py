account = ''

def Main_Menu():
    print('Login:')
    ID = input('Enter ID: ')
    pasw = input('Enter Password ')
    file = open('M_login.txt','r')
    flag = True
    for line in file:
        l = line.split()
        if l[0]==ID and l[1].strip()==pasw:
            global account
            account = l[0][1:]
            code = l[0][0]
            if code == 'm':
                M_login()
            if code == 'w':
                W_login()
            if code == 's':
                S_login()
            flag = False
    if flag:
        print('Incorrect ID/Password')
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
    print('press 9 to change the budget')
    choice=-1
    while(choice!=0):
        choice = int(input(''))
        if choice==1:
            InputStudent()
        elif choice==2:
            InputCourse()
        elif choice==3:
            M_Delete_Course()
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
        elif choice==9:
            Change_Budget()
        else:
            print('try again') 
        M_login()
        
def W_login():
    print('press 1 to ')
    print('press 2 to ')
    print('press 3 to ')
    print('press 4 to open complaints in Oscar')
    print('press 5 to see course budget')
    print('press 6 to send message')
    print('press 7 to check messages')
    print('press 8 to see students details')
    choice=-1
    while(choice!=0):
        choice = int(input(''))
        """if choice==1:
            
        elif choice==2:
            
        elif choice==3:"""
            
        if choice==4:
            Open_Bugs()
        elif choice==5:
            Print_budget()
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
    
def Open_Bugs():
    File_O=open('bugs.txt','a+')
    File_O.write(input('write the name of the person with the problem.'))
    File_O.write(input('write the complaint'))
    File_O.close()
Open_Bugs()
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
 

def M_Delete_Course():
    course = input("Please enter the name of the course: ")
    file = open('courses.txt','r')
    courses = [line for line in file]
    file.close()
    flag = False
    for i in range(len(courses)):
        if courses[i].split()[0]==course:
            flag=True
            del courses[i]
            break
    if not flag:
        print("Course does not exist")
        return False
    file = open("courses.txt",'w')
    for line in courses:
        file.write(line)
    file.close()
    return True

    
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
                File_O.write(account)
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
                File_O.write(account)
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
    line=File_O.readline()
    element=line.split(' ')
    while(line):
        if(element[0]==account):
            print('to ',element[0],' from ',element[1],'"',' '.join(element[2:]).strip(),'"')
            File_O.close()
            break    
        line=File_O.readline()   
        element=line.split(' ')
            

def W_Remove_Student():
    W_Print_Remove()
    student = input('Enter student to remove: ')
    course = input('Enter course: ')
    if not W_Confirm_Remove_Request(student,course):
        print('Request does not exists')
        return False
    file = open('courses.txt','r')
    courses = [line for line in file]
    file.close()
    for i in range(len(courses)):
        crs = courses[i].split(" ")
        if crs[0]==course:
            if student in crs:
                check = W_Confirm_Remove(student,course)
                if check==0:
                    print('Request sent')
                    return False
                if check==1:
                    crs.remove(student)
                    print('Student removed from course')
                if check==2:
                    print('Request Denied')
                    return False
            courses[i]=" ".join(crs)
            break
    file = open("courses.txt",'w')
    for line in courses:
        file.write(line)
    file.close()
    return True

def W_Print_Remove():
    file = open('outbox.txt','r')
    for line in file:
        l = line.split()
        if l[0]==account  and l[2]=='CONFIRM' and l[3]=='remove':
            print(line)
    file.close()
    
def W_Confirm_Remove_Request(student,course):
    file = open('outbox.txt','r')
    for line in file:
        l = line.split()
        if l[0]==account and l[1]==student and l[2]=='CONFIRM' and l[3]=='remove' and l[5]==course:
            file.close()
            return True
    file.close()
    return False

def W_Confirm_Remove(student,course):
    file = open('outbox.txt','r')
    flag = False
    for line in file:
        l = line.split()
        if l[0]==account and l[2]=='CONFIRM' and l[3]=='remove' and l[4]==student and l[5]==course:
            if l[-1]=='APPROVED':
                file.close()
                return 1
            elif l[-1]=='DENIED':
                file.close()
                return 2
        if l[1]==account and l[2]=='CONFIRM' and l[3]=='remove' and l[4]==student and l[5]==course:
            flag = True
    file.close()
    if flag:
        return 0
    file = open('outbox.txt','a')
    file.write('manager {} CONFIRM remove {} {}'.format(account,student,course))
    file.close()
    return 0

def S_Course_SignIn():
    course = input('Enter Course Name: ')
    file = open('courses.txt','r')
    courses = [line for line in file]
    file.close()
    flag = False
    for i in range(len(courses)):
        c = courses[i].split()
        if c[0]==course:
            if len(c[4:])<c[1]:
                if account in c[4:]:
                    print("Already signed up for course")
                    return False
                c.append(account)
                courses[i]=" ".join(c)
                flag = True
            else:
                print("Course at full capacity")
                return False
    if not flag:
        print("Course does not exist")
        return False
    file = open("courses.txt",'w')
    for line in courses:
        file.write(line)
    file.close()
    return True

def S_Average():
    file = open("students.txt",'r')
    for line in file:
        if line.split()[0]==account:
            print("Average: {}".format(line.split()[-1]))
            break
    file.close()
    
def W_Course_Average():
    course = input("Enter Course Name:")
    file = open("students.txt",'r')
    s,c = 0,0
    for line in file:
        l = line.split()
        if course in l:
            s+=l[l.index(course)+1]
            c+=1
    if c==0:
        print("Course does not exist or no students have signed up")
        return False
    print("{0} Average: {1:.2f}".format(course,s/c))
    return True

def S_View_Price():
    file = open("students.txt","r")
    courses = []
    for line in file:
        if line.split()[0]==account:
            courses = line.split()[4:-2:2]
    file.close()
    file = open("budget.txt","r")
    for line in file:
        if line.split()[0] in courses:
            print(line.strip())
    file.close()
def S_View_Sheet():
    file = open("students.txt","r")
    courses = []
    for line in file:
        if line.split()[0]==account:
            courses = line.split()[4:-2:2]
    file.close()
    file = open("course.txt","r")
    for line in file:
        if line.split()[0] in courses:
            if len(line.split()>2):
                print(line.split()[0],line.split()[3],line.split()[2])
    file.close()
    
def W_Add_To_Exam():
    student = input("Enter Student Name: ")
    course = input("Enter Course Name: ")
    if not W_Confirm_Exam_Request(student,course):
        print("Invalid Request")
        return False
    file = open("exams.txt",'r')
    exams = [line for line in file]
    file.close()
    for i in range(len(exams)):
        e = exams[i].split()
        if e[0]==course:
            if e[1]<len(e[3:]):
                e.append(student)
                exams[i] = " ".join(e)
            else:
                print("Exam is at full capacity")
                return False
    file = open("exams.txt",'w')
    for line in exams:
        file.write(line)
    file.close()
    return True
    
def W_Confirm_Exam_Request(student,course):
    file = open('outbox.txt','r')
    for line in file:
        l = line.split()
        if l[0]==account and l[1]==student and l[2]=='CONFIRM' and l[3]=='remove' and l[5]==course:
            file.close()
            return True
    file.close()
    return False
    
def Change_Budget():
    check=input('Enter the name of the course you would like to the change budget of.')
    File_O=open('courses.txt','r')
    line=File_O.readline()
    element=line.split(' ')
    while(line):
        if(element[0]==check):
            test=1
            File_O.close()
            break
        else:
            line=File_O.readline()
            element=line.split(' ')
            test=0
    if(test==0):
        print('The course name is invalid try again.')
        File_O.close()
        Change_Budget()
    newprice=input('Enter the new budget for this course.')
    file = open("budget.txt",'r')
    b = [line for line in file]
    file.close()
    for i in range(len(b)):
        temp = b[i].split(" ")
        if(temp[0]==check):
            temp[1]=newprice+'\n'
            b[i]=" ".join(temp)
            break
        
    print(temp)  
    file = open("budget.txt",'w')
    for line in b:
        file.write(line)
    file.close()
def Print_budget():
    check=input('Enter the name of the course you would like to the check budget of.')
    File_O=open('courses.txt','r')
    line=File_O.readline()
    element=line.split(' ')
    while(line):
        if(element[0]==check):
            test=1
            File_O.close()
            break
        else:
            line=File_O.readline()
            element=line.split(' ')
            test=0
    if(test==0):
        print('The course name is invalid try again.')
        File_O.close()
        Print_budget()
    File_O=open('budget.txt','r')
    line=File_O.readline()
    element=line.split(' ')
    while(line):
        if(element[0]==check):
            print(line)
            File_O.close()
            break
        else:
            line=File_O.readline()
            element=line.split(' ')
Main_Menu()
