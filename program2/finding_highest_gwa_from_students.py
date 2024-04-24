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


        for student, grade in info_record.items():
            float_grade = float(grade)
            if highest_gwa is None or float_grade < float(highest_gwa):
                highest_gwa_student = student
                highest_gwa = grade
        return highest_gwa_student, highest_gwa
    
#output highest gwa student from the file with their name and their gwa using tkinter
def show_result():
    directory = "students_and_gwa.txt"
    student, gwa = get_highest_gwa(directory)
    result_label.config(text=f"{student} has achieved the highest GWA of {gwa}")

root = tk.Tk()
root.title("Highest GWA of Student with their name Finder")

main_frame = tk.Frame(root, bg="#EEE9BF")
main_frame.pack(fill="both", expand=True)

title_label = tk.Label(main_frame, text="Highest GWA Finder", font=("Lexend", 36, "bold"), bg="#EEE9BF", fg="black")
title_label.pack(pady=20)

button_frame = tk.Frame(main_frame, bg="#EEE9BF")
button_frame.pack(pady=20)

find_button = tk.Button(button_frame, text="Find Highest GWA", command=show_result, font=("Lexend", 18, "bold"), bg="#8B8970", fg="black")
find_button.pack(side="left", padx=10)

result_label = tk.Label(button_frame, text="", font=("Lexend", 18, "bold"), bg="#EEE9BF", fg="crimson")
result_label.pack(side="left", padx=10)

root.mainloop()


    
