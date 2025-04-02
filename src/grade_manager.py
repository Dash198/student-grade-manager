import student      # Contains the Student class
import os, time     # os for file operations and time for the delay (QOL)
import csv          # We use CSV files for persistent storage

class GradeManager:

    def __init__(self):     # Init function which stores current file name, students and subjects
        self.curr_file = None
        self.students = {}
        self.subjects = []
    
    def make_new_file(self):     # Function to make a new file (Note that this file is actually created ONLY once you save and exit)
        name = input("Enter the name of the file : ")
        self.curr_file = name

    def open_saved_file(self):  # Function to open a previously saved file or another CSV
        if not os.path.exists('saves') or len(os.listdir('saves/'))==0:     # Checking if the 'saves' directory exists and is non-empty
            print('No save files found!')
            time.sleep(1)
            return
        
        print("Saved files found...\n")
        save_files = os.listdir('saves/')
        for file in save_files:
            print(file)
        name = input("\nEnter the name of the file you wish to open : ")

        if name not in save_files:      # Another check to see if the file is in the given list
            print("Error: File does not exist!")
            time.sleep(1)
            return False
        
        self.curr_file = name

        filename = "saves/"+name

        # Load everything into the the students dictionary and subjects list
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
        return True

    def close_file(self):

        if not os.path.exists('saves'):     # If the 'saves' directory doesn't exist, make it
            os.makedirs('saves')

        # Put all data in the form of a list of list of objects 
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

        # Write to the file
        filename = "saves/" + self.curr_file
        with open(filename,'w') as f:
            csvwriter = csv.writer(f)

            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
        
        self.subjects.clear()
        self.students.clear()
        print("File saved successfully")
        pass

    def clear_screen(self):     # Function to clear the screen after a process is done (QOL)
        if os.name=='nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def add_new_record(self):       # Function to add a new record

        # Take all the necesarry field inputs from the user, note that the grade can be any number!
        id = input("Enter student ID : ")

        # Students must have unique ID
        if id not in self.students.keys():
            name = input("Enter student name : ")
            grades = {}
            for sub in self.subjects:
                grade = int(input(f"Enter grade for student in {sub} (1-10, or any number according to your grading system): "))
                grades[sub] = grade

            new_student = student.Student(name,id,grades)
            self.students[id] = new_student
            print("Successfully added student ID "+id)
        else:
            print("Error: Student ID already exists!")

        time.sleep(1)

    def add_new_subject(self):      # Function to add a new subject

        subject = input("Enter 3-letter code for subject to a        passdd: ")

        # Again, subject must be unique
        if subject not in self.subjects:
            self.subjects.append(subject)
            for id in self.students.keys():

                # Manual assignment of grade for each of the existing students
                grade = int(input(f"Enter the grade for student with ID {id} (1-10 or any other value depending on your system): "))
                self.students[id].grades[subject] = grade
            
            print("Successfully added "+subject)
        else:
            print("Error: Subject already exists!")
        
        time.sleep(1)

    def edit_student_record(self):      # Function to edit an existing student record


        id = input("Enter the ID of the student you wish to edit : ")

        if id not in self.students.keys():
            print("Error: No such student exists!")
        
        # The ID, Name and grades can be edited, but the ID must be unique again
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

    def delete_student_record(self):        # Function to delete a student record

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

    def delete_subject(self):       # Function to delete a subject field

        subject = input("Enter 3-letter code for subject to remove: ")
        if subject not in self.subjects:
            print("Error: No such subject exists!")
        else:
            self.subjects.remove(subject)
            for id in self.students.keys():
                self.students[id].grades.pop(subject)

            print("Successfully removed subject "+subject)

        time.sleep(1)

    def view_student_stats(self):       # Function to view the stats of a student, namely all scores and average score

        id = input("Enter student ID to look for : ")
        if id not in self.students.keys():
            print("Error : Invalid student ID!")
            time.sleep(1)

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

            print(f"Average Grade : {round(avg,2)}\n")
            _ = input("Press any key to exit...")

    def view_subject_stats(self):       # Function to view the stats for a subject, namely the average score, the score distribution and the top scorers (3 or less)

        if len(self.students) == 0:
            print("No students in system!")
            time.sleep(1)
            return
        
        sub = input("Enter 3-letter code of subject : ")
        if sub not in self.subjects:
            print("Error: Invalid subject!")
            time.sleep(1)

        else:

            avg = 0
            grade_groups = {str(i):0 for i in range(1,11)}
            scores=[]
            for id in self.students.keys():
                score = self.students[id].grades[sub]
                grade_groups[score] += 1
                avg += int(score)
                scores.append((int(score),id))

            scores.sort(reverse=True)

            avg /= len(self.students)
            print(f"Average Grade : {round(avg,2)}")
            print("Grade Distribution : ")
            for i in grade_groups.keys():
                if grade_groups[i] != 0:
                    print(f"{i} - {grade_groups[i]}")
            print()

            print("Top Scorers:")
            name = "Name".ljust(15," ")
            id = "ID".ljust(5," ")
            print(id,end='')
            print(name,end='')
            grade = "Grade".ljust(15," ")
            print(grade,end='')
            print()

            for i in range(min(len(scores),3)):
                id = scores[i][1]
                grade = scores[i][0]
                name = self.students[id].name
                name = name.ljust(15," ")
                id = id.ljust(5," ")
                grade = str(grade).ljust(5," ")
                print(id,end='')
                print(name,end='')
                print(grade,end='')
                print()

            _ = input("Press any key to exit...")

    def view_overall_stats(self):       # Function to display Overall Stats, i.e, the average, highest and lowest grade in each subject and top scorers (top 3 or less)

        if len(self.students) == 0:
            print("No students in system!")
            time.sleep(1)
            return

        def calcAvg(lst):           # Helper function to calculate average grade
            sum = 0 
            for x in lst:
                sum += int(x)

            return round((sum/len(lst)),2)

        def calcHighest(lst):       # Helper function to calculate highest grade
            highest = 0
            for x in lst:
                highest = max(highest, int(x))
            
            return highest

        def calcLowest(lst):        # Helper function to calculate lowest grade
            lowest = -1
            for x in lst:
                if lowest == -1:
                    lowest = int(x)

                else:
                    lowest = min(lowest, int(x))

            return lowest
        
        # A dictionary to store all the scores subjectwise
        all_sub_scores = {}     
        for sub in self.subjects:
            all_sub_scores[sub] = []
            for id in self.students.keys():
                all_sub_scores[sub].append(self.students[id].grades[sub])
        
        # Dictionary to store all the scores student-wise
        all_student_scores = {}
        for student_id in self.students.keys():
            all_student_scores[student_id] = []
            for sub in self.subjects:
                all_student_scores[student_id].append(self.students[student_id].grades[sub])

        # Store and sort the avg grade of the students
        avg_student_grades = [(calcAvg(all_student_scores[id]),id) for id in self.students.keys()]
        avg_student_grades.sort(reverse=True)


        # Print everything!
        print("Overall Statistics:\n")

        name = "Statistic".ljust(15," ")
        print(name,end='')
        for sub in self.subjects:
            sub = sub.ljust(5," ")
            print(sub,end='')
        print()

        name = "Avg. Grade".ljust(15," ")
        print(name,end='')
        for sub in self.subjects:
            avg = str(calcAvg(all_sub_scores[sub])).ljust(5," ")
            print(avg,end='')
        print()

        name = "Highest Grade".ljust(15," ")
        print(name,end='')
        for sub in self.subjects:
            avg = str(calcHighest(all_sub_scores[sub])).ljust(5," ")
            print(avg,end='')
        print()

        name = "Lowest Grade".ljust(15," ")
        print(name,end='')
        for sub in self.subjects:
            avg = str(calcLowest(all_sub_scores[sub])).ljust(5," ")
            print(avg,end='')
        print('\n')

        print("Top Scorers:")
        name = "Name".ljust(15," ")
        id = "ID".ljust(5," ")
        print(id,end='')
        print(name,end='')
        grade = "Avg. Grade".ljust(15," ")
        print(grade,end='')
        print()

        for i in range(min(len(all_student_scores),3)):
            id = avg_student_grades[i][1]
            grade = avg_student_grades[i][0]
            name = self.students[id].name
            name = name.ljust(15," ")
            id = id.ljust(5," ")
            grade = str(grade).ljust(5," ")
            print(id,end='')
            print(name,end='')
            print(grade,end='')
            print()


        _ = input("Press any key to exit...")
    
    def view_grades(self):              # Function to view all the grades
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

