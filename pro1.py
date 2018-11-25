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
    
def Average_Grade():
    file = open("students.txt",'r')
    count, total = 0,0
    for line in file:
        count+=1
        total+=int(line.split(' ')[-1])
    return total/count 

def Average_Grade():
    course = input("Enter course name: ")
    if Validate_Course(course):
        return Calc_Avg(course)
    
def Validate_Course(course):
    file = open("courses.txt",'r')
    for line in file:
        if course == line.split(' ')[0]:
            return True
    return False
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
def Calc_Avg(course):
    
def M_login():
    print('') 
    print('press 1 to add new student\n press 2 to add new course\n press 3 to delete course\n press 4 to add more places to course\n press 5 for student averages\n')
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
        Average_Grade()
    else:
        print('try again')
        M_login()
        
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



DeleteCourse()
