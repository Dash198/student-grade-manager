from grade_manager import GradeManager      # GradeManager handles all most/all of the commands
from enum import Enum, auto                 # Library to manage different Menu states
import time         # To add some delay before switching

class MenuState(Enum):      # Enumeration which defines the diffferent types of printable menu states
    START = auto()
    FILE_VIEW = auto()
    EDIT = auto()
    STATS = auto()

class Menu:

    def __init__(self):             # Init function
        self.current_state = MenuState.START
        self.running = True
        self.gm = GradeManager()
    
    def displayMenu(self):          # Function which displays the current menu depending on its state

        if self.current_state == MenuState.START:
            print("MENU:")
            print("\n1. Make a new grade file\n2. Open a saved grade file\n3. Exit")
            choice = input("\nEnter your choice (1-3) : ")
        
        elif self.current_state == MenuState.FILE_VIEW:
            print(f"FILE MENU - {self.gm.curr_file} :")
            print("\n1. View grades\n2. Edit Students and Grades\n3. View Statistics\n4. Save and Exit")
            choice = input("\nEnter your choice (1-3) : ")
        
        elif self.current_state == MenuState.EDIT:
            print(f"EDITING - {self.gm.curr_file} :")
            print("\n1. Add a student record\n2. Add a new subject\n3. Edit a student record\n4. Delete a student record\n5. Delete a subject\n6. Quit editing")
            choice = input("\nEnter your choice (1-6) : ")
        
        elif self.current_state == MenuState.STATS:
            print(f"STATISTICS - {self.gm.curr_file} :")
            print("\n1. View for a specific student\n2. View for a specific subject\n3. View for all students and subjects\n4. Exit")
            choice = input("\nEnter your choice (1-4) : ")
        print()

        return choice
    
    def processChoice(self,choice):     # Processor function which calls the appropriate function

        try:
            choice = int(choice)
        
        except ValueError:
            print("Error: Invalid Choice!")
            time.sleep(1)
            return

        if self.current_state == MenuState.START:

            if choice == 1:
                self.gm.make_new_file()
                self.current_state = MenuState.FILE_VIEW
            
            elif choice == 2:
                if self.gm.open_saved_file():
                    self.current_state = MenuState.FILE_VIEW
            
            elif choice == 3:
                self.running = False

            else:
                print("Error: Enter a valid choice!")
                time.sleep(1)

        elif self.current_state == MenuState.FILE_VIEW:
            if choice == 1:
                self.gm.view_grades()

            elif choice == 2:
                self.current_state = MenuState.EDIT
            
            elif choice == 3:
                self.current_state = MenuState.STATS
            
            elif choice == 4:
                self.gm.close_file()
                self.current_state = MenuState.START
            
            else:
                print("Error: Enter a valid choice!")
                time.sleep(1)

        elif self.current_state == MenuState.EDIT:
            if choice == 1:
                self.gm.add_new_record()
                pass
            
            elif choice == 2:
                self.gm.add_new_subject()
                pass
            
            elif choice == 3:
                self.gm.edit_student_record()
                pass
            
            elif choice == 4:
                self.gm.delete_student_record()
                pass

            elif choice == 5:
                self.gm.delete_subject()
                pass

            elif choice == 6:
                self.current_state = MenuState.FILE_VIEW
            
            else:
                print("Error: Enter a valid choice!")
                time.sleep(1)

        elif self.current_state == MenuState.STATS:
            if choice == 1:
                self.gm.view_student_stats()
                pass
            
            elif choice == 2:
                self.gm.view_subject_stats()
                pass
            
            elif choice == 3:
                self.gm.view_overall_stats()
                pass

            elif choice == 4:
                self.current_state = MenuState.FILE_VIEW

            else:
                print("Error: Enter a valid choice!")
                time.sleep(1)


# Menu object
menu = Menu()

def start():

    # This loop of take input, process, update runs as long as we don't exit
    while menu.running:
        choice = menu.displayMenu()
        menu.processChoice(choice)
        menu.gm.clear_screen()

