import student
import os, time
import csv

class GradeManager:

    def __init__(self):
        self.curr_file = None
        self.students = {}
        self.subjects = []
    
    def make_new_file(self):
        name = input("Enter the name of the file : ")
        self.curr_file = name
        pass

    def open_saved_file(self):
        print("Saved files found...")
        print(os.listdir('saves/'))
        name = input("Enter the name of the file you wish to open : ")
        self.curr_file = name

        filename = "saves/"+name
        with open(filename,'r') as f:
            csvreader = csv.reader(f)
            fields = next(csvreader)
            self.subjects = fields[2:]
            for row in csvreader:
                id = row[0]
                name = row[1]
                grades = row[2:]

                self.students[id] = student.Student(name,id,dict(zip(self.subjects,grades)))
            
            

        print("File loaded successfully")
        pass

    def close_file(self):
        fields = ['ID', 'Name']
        fields.extend(self.subjects)

        rows=[]
        for  id in self.students.keys():
            id = id
            name = self.students[id].name
            row = [id,name]
            for sub in self.subjects:
                row.append(self.students[id].grades[sub])
            rows.append(row)

        filename = "saves/" + self.curr_file
        with open(filename,'w') as f:
            csvwriter = csv.writer(f)

            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        
        self.subjects.clear()
        self.students.clear()
        print("File saved successfully")
        pass

    def clear_screen(self):
        if os.name=='nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def add_new_record(self):
        id = input("Enter student ID : ")
        if id not in self.students.keys():
            name = input("Enter student name : ")
            grades = {}
            for sub in self.subjects:
                grade = int(input(f"Enter grade for student in {sub} (1-10): "))
                grades[sub] = grade

            new_student = student.Student(name,id,grades)
            self.students[id] = new_student
            print("Successfully added student ID "+id)
        else:
            print("Error: Student ID already exists!")

        time.sleep(1)
        pass

    def add_new_subject(self):
        subject = input("Enter 3-letter code for subject to add: ")
        if subject not in self.subjects:
            self.subjects.append(subject)
            for id in self.students.keys():
                grade = int(input(f"Enter the grade for student with ID {id} (1-10): "))
                self.students[id].grades[subject] = grade
            
            print("Successfully added "+subject)
        else:
            print("Error: Subject already exists!")
        
        time.sleep(1)
        pass

    def edit_student_record(self):
        id = input("Enter the ID of the student you wish to edit : ")
        if id not in self.students.keys():
            print("Error: No such student exists!")
        
        else:
            print("Press one of the following numbers:")
            print("1. Edit ID")
            print("2. Edit Name")
            print("3. Edit grades")
            choice = int(input("Enter your choice (1-3) : "))

            if choice == 1:
                id_new = input("Enter the new ID : ")
                if id_new in self.students.keys():
                    print("Error: This ID already exists!")
                else:
                    new_student = self.students[id]
                    new_student.id = id_new
                    self.students.pop(id)
                    self.students[id_new] = new_student
                    print("ID change successful")
            
            elif choice == 2:
                self.students[id].name = input("Enter the new name : ")
                print("Name change successful")

            elif choice == 3:
                sub = input("Enter the 3-letter code of the subject : ")
                if sub not in self.subjects:
                    print("Error: No such subject exists!")
                else:

                    new_grade = input("Enter the new grade : ")
                    self.students[id].grades[sub] = new_grade
                    print("Grade change successful")

            else:
                print("Error: Invalid choice!")

        time.sleep(1)
        pass

    def delete_student_record(self):
        if len(self.students) == 0:
            print("Error: No records to delete!")
        else:
            id = input("Enter student ID to remove : ")

            if id in self.students.keys():
                self.students.pop(id)
                print("Successfully removed student with ID "+id)

            else:
                print("Error: No such ID exists!")
        
        time.sleep(1)
        pass

    def delete_subject(self):
        subject = input("Enter 3-letter code for subject to remove: ")
        if subject not in self.subjects:
            print("Error: No such subject exists!")
        else:
            self.subjects.remove(subject)
            for id in self.students.keys():
                self.students[id].grades.pop(subject)

            print("Successfully removed subject "+subject)

        time.sleep(1)
        pass

    def view_student_stats(self):
        id = input("Enter student ID to look for : ")
        if id not in self.students.keys():
            print("Error : Invalid student ID!")

        else:
            stud = self.students[id]
            name = "Name".ljust(15," ")
            id = "ID".ljust(5," ")
            print(id,end='')
            print(name,end='')
            for sub in self.subjects:
                sub = sub.ljust(5," ")
                print(sub,end='')
            print()
            avg = 0
            id = id.ljust(5," ")
            name = stud.name.ljust(15," ")
            print(id,end='')
            print(name,end='')
            for sub in self.subjects:
                grade = str(stud.grades[sub]).ljust(5, " ")
                avg+=int(grade)
                print(grade,end="")
                
            print()
            avg /= len(self.subjects)

            print(f"Average Grade : {avg}\n")
            _ = input("Press any key to exit...")
            
        pass

    def view_subject_stats(self):
        sub = input("Enter 3-letter code of subject : ")
        if sub not in self.subjects:
            print("Error: Invalid subject!")
        else:

            avg = 0
            grade_groups = {i:0 for i in range(1,11)}
            for id in self.students.keys():
                score = self.students[id].grades[sub]
                grade_groups[score] += 1
                avg += int(score)

            avg /= len(self.students)
            print(f"Average Grade : {avg}")
            print("Grade Distribution : ")
            for i in grade_groups.keys():
                print(f"{i} - {grade_groups[i]}")

            _ = input("Press any key to exit")
        pass

    def view_overall_stats(self):
        pass

    def view_grades(self):
        if len(self.students) == 0:
            print("Error: No records to view!")
        else:
            name = "Name".ljust(15," ")
            id = "ID".ljust(5," ")
            print(id,end='')
            print(name,end='')
            for sub in self.subjects:
                sub = sub.ljust(5," ")
                print(sub,end='')
            print()

            for id in self.students.keys():
                stud = self.students[id]
                id = id.ljust(5," ")
                name = stud.name.ljust(15," ")
                print(id,end='')
                print(name,end='')
                for sub in self.subjects:
                    grade = str(stud.grades[sub]).ljust(5, " ")
                    print(grade,end="")
                
                print()
            
        _ = input("Press any key to exit...")
        pass

