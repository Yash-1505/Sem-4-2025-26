import sys

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Student(Person):
    def __init__(self, name, enrollment_number):
        super().__init__(name)
        self.enrollment_number = enrollment_number
        self.roll_no = None
        self.division = None
        self.lab_batch = None
        self.program = None
        self.academic_batch = None

    def __str__(self):
        div_name = self.division.name if self.division else "NA"
        batch_name = self.lab_batch.name if self.lab_batch else "NA"
        return f"[ID: {self.enrollment_number}] {self.name} | Roll: {self.roll_no} | Div: {div_name} | Batch: {batch_name}"

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        self.is_class_teacher = False

    def mark_attendance(self, division, date, present_roll_nos):
        print(f"\n[Attendance] Teacher {self.name} marking for {division.name} on {date}")
        division.log_attendance(date, present_roll_nos)

    def __str__(self):
        role = "Class Teacher" if self.is_class_teacher else "Subject Teacher"
        return f"[Teacher] {self.name} ({self.subject}) - {role}"

class LabBatch:
    def __init__(self, name, capacity=25):
        self.name = name
        self.capacity = capacity
        self.students = []

    def is_full(self):
        return len(self.students) >= self.capacity

    def add_student(self, student):
        if not self.is_full():
            self.students.append(student)
            student.lab_batch = self
            return True
        return False

class Division:
    def __init__(self, name, capacity=50):
        self.name = name
        self.capacity = capacity
        self.students = []
        self.class_teacher = None
        self.lab_batches = [] 
        self.attendance_log = {}

    def set_class_teacher(self, teacher):
        self.class_teacher = teacher
        teacher.is_class_teacher = True

    def _get_next_lab_batch(self):
        for batch in self.lab_batches:
            if not batch.is_full():
                return batch
        new_batch_name = f"{self.name}{len(self.lab_batches) + 1}"
        new_batch = LabBatch(new_batch_name)
        self.lab_batches.append(new_batch)
        return new_batch

    def add_student(self, student):
        if len(self.students) < self.capacity:
            student.roll_no = len(self.students) + 1
            self.students.append(student)
            student.division = self
            
            lab_batch = self._get_next_lab_batch()
            lab_batch.add_student(student)
            return True
        return False
    
    def log_attendance(self, date, present_roll_nos):
        self.attendance_log[date] = present_roll_nos
        print(f"Attendance logged: {len(present_roll_nos)} students present.")

    def __str__(self):
        ct_name = self.class_teacher.name if self.class_teacher else "None"
        return f"Div {self.name} [{len(self.students)}/{self.capacity}] (CT: {ct_name})"

class Semester:
    def __init__(self, number):
        self.number = number
        self.divisions = [] 

    def add_division(self, division):
        self.divisions.append(division)

    def get_target_division(self):
        valid_divs = [d for d in self.divisions if len(d.students) < d.capacity]
        if not valid_divs:
            return None
        valid_divs.sort(key=lambda d: len(d.students))
        return valid_divs[0]

    def optimize_divisions(self):
        print(f"\n--- Optimizing Divisions for Semester {self.number} ---")
        small_divs = [d for d in self.divisions if len(d.students) < 10]
        
        if not small_divs:
            print("No small divisions needing optimization.")
            return

        for small_div in small_divs:
            print(f"Detected small division: {small_div.name} ({len(small_div.students)} students)")
            students_to_move = list(small_div.students) 
            
            remaining_students = []
            
            potential_targets = [d for d in self.divisions if d != small_div]
            for student in students_to_move:
                moved = False
                for target in potential_targets:
                    if target.add_student(student):
                        print(f"Moved {student.name} from {small_div.name} to {target.name}")
                        moved = True
                        break
                if not moved:
                    remaining_students.append(student)
            
            if not remaining_students:
                print(f"Removing empty division {small_div.name}")
                if small_div in self.divisions:
                    self.divisions.remove(small_div)
            else:
                print(f"Could not fully merge {small_div.name}, {len(remaining_students)} students remain. Kept division.")

class AcademicBatch:
    def __init__(self, year_range):
        self.year_range = year_range
        self.semesters = []
        self.student_counter = 0

    def generate_enrollment_number(self):
        prefix = self.year_range.split('-')[0]
        self.student_counter += 1
        return f"{prefix}{self.student_counter:03d}"

    def add_semester(self, semester):
        self.semesters.append(semester)
    
    def get_semester(self, number):
        for s in self.semesters:
            if s.number == number:
                return s
        return None

class Program:
    def __init__(self, name):
        self.name = name
        self.academic_batches = []

    def add_batch(self, batch):
        self.academic_batches.append(batch)
    
    def get_batch(self, year_range):
        for b in self.academic_batches:
            if b.year_range == year_range:
                return b
        return None

programs = []
teachers = []

def get_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return -1

def find_program(name):
    for p in programs:
        if p.name == name:
            return p
    return None

def create_program():
    name = input("Enter Program Name (e.g., B.Tech): ")
    if find_program(name):
        print("Program already exists!")
    else:
        programs.append(Program(name))
        print(f"Program '{name}' created.")

def create_batch():
    if not programs:
        print("Create a Program first.")
        return
    
    prog_name = input("Enter Program Name to add batch to: ")
    program = find_program(prog_name)
    if not program:
        print("Program not found.")
        return
    
    year_range = input("Enter Batch Year Range (e.g., 2024-2028): ")
    if program.get_batch(year_range):
        print("Batch already exists.")
    else:
        new_batch = AcademicBatch(year_range)
        program.add_batch(new_batch)
        print(f"Batch '{year_range}' added to {prog_name}.")

def create_semester():
    prog_name = input("Enter Program Name: ")
    program = find_program(prog_name)
    if not program:
        print("Program not found.")
        return
    
    batch_year = input("Enter Batch Year Range: ")
    batch = program.get_batch(batch_year)
    if not batch:
        print("Batch not found.")
        return

    sem_num = get_int_input("Enter Semester Number: ")
    if batch.get_semester(sem_num):
        print("Semester already exists.")
    else:
        batch.add_semester(Semester(sem_num))
        print(f"Semester {sem_num} added.")

def create_division():
    prog_name = input("Enter Program Name: ")
    program = find_program(prog_name)
    if not program: return
    
    batch_year = input("Enter Batch Year Range: ")
    batch = program.get_batch(batch_year)
    if not batch: return

    sem_num = get_int_input("Enter Semester Number: ")
    semester = batch.get_semester(sem_num)
    if not semester: 
        print("Semester not found.")
        return

    div_name = input("Enter Division Name (e.g., A, B): ")
    
    for d in semester.divisions:
        if d.name == div_name:
            print("Division already exists.")
            return

    new_div = Division(div_name)
    semester.add_division(new_div)
    print(f"Division {div_name} added to Semester {sem_num}.")

def enroll_student():
    name = input("Enter Student Name: ")
    
    prog_name = input("Enter Program Name: ")
    program = find_program(prog_name)
    if not program: return
    
    batch_year = input("Enter Batch Year Range: ")
    batch = program.get_batch(batch_year)
    if not batch: 
        print("Batch not found.")
        return

    sem_num = get_int_input("Enter Semester Number to enroll in: ")
    semester = batch.get_semester(sem_num)
    if not semester: 
        print("Semester not found.")
        return

    enroll_no = batch.generate_enrollment_number()
    student = Student(name, enroll_no)
    student.program = program
    student.academic_batch = batch
    
    target_div = semester.get_target_division()
    if target_div:
        target_div.add_student(student)
        print(f"Enrolled successfully: {student}")
    else:
        print("Enrollment Failed: No divisions available or all are full.")

def assign_teacher():
    t_name = input("Enter Teacher Name: ")
    subject = input("Enter Subject: ")
    teacher = Teacher(t_name, subject)
    teachers.append(teacher)
    
    assign_now = input("Assign as Class Teacher? (y/n): ")
    if assign_now.lower() == 'y':
         print("Select Division to assign to:")
         prog_name = input("  Program: ")
         program = find_program(prog_name)
         if program:
             batch_year = input("  Batch: ")
             batch = program.get_batch(batch_year)
             if batch:
                 sem_num = get_int_input("  Semester: ")
                 semester = batch.get_semester(sem_num)
                 if semester:
                     div_name = input("  Division Name: ")
                     for d in semester.divisions:
                         if d.name == div_name:
                             d.set_class_teacher(teacher)
                             print(f"Assigned {t_name} as Class Teacher for Div {div_name}")
                             return
    print("Teacher created.")

def display_report():
    if not programs:
        print("No data.")
        return
    for p in programs:
        print(f"\nProgram: {p.name}")
        for b in p.academic_batches:
            print(f"  Batch: {b.year_range}")
            for s in b.semesters:
                print(f"    Semester {s.number}")
                for d in s.divisions:
                    print(f"      {d}")
                    for stud in d.students:
                        print(f"        - {stud}")

def optimize_classes():
    prog_name = input("Enter Program Name: ")
    program = find_program(prog_name)
    if not program: return
    batch_year = input("Enter Batch Year Range: ")
    batch = program.get_batch(batch_year)
    if not batch: return
    sem_num = get_int_input("Enter Semester Number: ")
    semester = batch.get_semester(sem_num)
    if not semester: return
    
    semester.optimize_divisions()

def main():
    while True:
        print("\n=== School Management System ===")
        print("1. Add Program")
        print("2. Add Batch")
        print("3. Add Semester")
        print("4. Add Division")
        print("5. Enroll Student")
        print("6. Add/Assign Teacher")
        print("7. Display All Reports")
        print("8. Optimize Classes (Merge Small)")
        print("9. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1': create_program()
        elif choice == '2': create_batch()
        elif choice == '3': create_semester()
        elif choice == '4': create_division()
        elif choice == '5': enroll_student()
        elif choice == '6': assign_teacher()
        elif choice == '7': display_report()
        elif choice == '8': optimize_classes()
        elif choice == '9': 
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()