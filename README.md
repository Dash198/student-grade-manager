# Student Grade Manager

## Description:
A simple yet quite versatile CLI based system to manage grades for students. Add, edit or delete student records, subject grade fields, view stats for each student and subject and effortlessly save and load the grade sheets as CSV files!

## Installation
Ensure that Python is installed in the system, preferably Python 3.6+.

Then navigate to the `src` directory throuh the terminal, and run the following command to start the application:

`python main.py`

or

`python3 main.py`

## Design Choices
### Programming Language
- Python is simple to use and has a lot of useful libraries, hence it is ideal

### Object Oriented Approach
- Uses Classes and Objects for all the functions, which keeps all the functions organized and easy to use via objects created even from other files.

### Unique Identifier
- Uses the Student ID as the *unique identifier* as it is guaranteed to be unique.

### CSV Storage
- Records are stored in a CSV file which is loaded at the start and saved at the end.
- Records are not saved after they are made, they are only saved after we exit the file, so the "autosave" feature is absent as it may get too slow.
- Hence if the application encounters an error, all the unwritten data is lost, although we can implement an autosave at the end of each operation by making a copy of the current records in a global variable which is written to the file once the process ends.

### CLI Based Interaction
- Easier to implement, the program does not require GUI as it is small enough to run from the terminal conveniently.

### Algorithms and Libraries Used
- Uses dictionaries and lists for convenient and efficient data handling.
- Libraries:
  - `os`: For file and directory management.
  - `time`: To add a QOL feature of a small delay before moving on.
  - `enum`: To enumerate the different menu states which can be displayed.
  - `csv`: For CSV file handling.

## Main Features
- Add, update or delete student records, identified by their ID.
- Add or delete subjects, store and edit grades for each student.
- View statistics for each student, namely all their grades and their average grade to track their performance.
- View statistics for each subject, the average grade, the grade distribution and top scorers.

## Key Learnings
- Better understanding of Object-Oriented Programming (OOP) in Python.
- Gained experience in modular program structuring.
- Gained a better understanding on user input, data storage and operations to create, read, edit and delete data.