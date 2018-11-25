import pro1
import course_resize
import course_grade_avg
import GradeAvg


def Main_Menu():
    print('')
    choice = int(input(''))
    if choice==1:
        pro1.InputCourse()
        print('Manager')
    elif choice==2:
        print('Worker')
    elif choice==3:
        course_resize.Increase_Seats()
        print('Student')
    else:
        print('Invalid Choice')
Main_Menu()