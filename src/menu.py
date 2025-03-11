from grade_manager import GradeManager

class Menu:

    def __init__(self):
        self.fileOpen = False
        self.running = True
        self.gm = GradeManager()
    
    def displayMenu(self):

        if not self.fileOpen:

            print("MENU:")
            print("\n1. Make a new grade file\n2. Open a saved grade file\n3. Exit")
            choice = input("Enter your choice (1-3) : ")
        
        else:
            print(f"MENU - {self.gm.curr_file} :")
            print("\n1. Add a new student\n2. Edit grade for a student\n3. Delete student record\n4. Exit")
            choice = input("Enter your choice (1-4) : ")
        
        return choice
    
    def processChoice(self,choice):

        if not self.fileOpen:

            if choice == 1:
                name = input("Enter the name for the new grade file: ")
                self.gm.open_file(name)
                self.fileOpen = True
            
            elif choice == 2:
                self.gm.display_saved_files
                name = input("Enter the name of the file you wish to open: ")
                self.gm.open_file(name)
                self.fileOpen = True
            
            elif choice == 3:
                self.running = False

            else:
                print("Error: Enter a valid choice!")

        else:
            
            if choice == 1:
                self.gm.add_student()
            
            elif choice == 2:
                self.gm.edit_grade()

            elif choice == 3:
                self.gm.delete_record()



menu = Menu()

def start():

    while menu.running:
        menu.displayMenu()

