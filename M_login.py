

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




