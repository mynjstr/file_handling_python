#pseudocode
#create a file with 20 student names and their gwa
#import tkinter
import tkinter as tk
#output highest gwa student from the file
#read students_and_gwa.txt 
def get_highest_gwa(directory):
    with open(directory, "r") as students_and_gwa_file:
        info = students_and_gwa_file.read()
        info_record = eval(info)
        highest_gwa = None
        highest_gwa_student = None

#find highest gwa student and their gwa

        for student, grade in info_record.items():
            float_grade = float(grade)
            if highest_gwa is None or float_grade < float(highest_gwa):
                highest_gwa_student = student
                highest_gwa = grade
        return highest_gwa_student, highest_gwa

#output highest gwa student from the file with their name and their gwa using tkinter

    
