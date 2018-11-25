# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:54:49 2018

@author: Baroz
"""

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

def Calc_Avg(course):
    