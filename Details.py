class Student:
    def _init_(self, reg_no, surname, year_of_study, dob, fees_paid):
        self.reg_no = reg_no
        self.surname = surname
        self.year_of_study = year_of_study
        self.dob = dob  # Just store as string
        self.fees_paid = fees_paid
    
    def display_info(self):
        print("\nStudent Information:")
        print(f"1. Registration Number: {self.reg_no}")
        print(f"2. Surname: {self.surname}")
        print(f"3. Year of Study: {self.year_of_study}")
        print(f"4. Date of Birth: {self.dob}")
        print(f"5. Fees Paid: ${self.fees_paid}")

def get_student_info():
    print("Enter student details:")
    reg_no = input("Registration Number: ")
    surname = input("Surname: ")
    year_of_study = input("Year of Study: ")
    dob = input("Date of Birth (e.g., 15-05-2000): ")
    fees_paid = input("Fees paid this semester: ")
    
    return Student(reg_no, surname, year_of_study, dob, fees_paid)

# Main program
print("STUDENT INFORMATION SYSTEM")
student = get_student_info()
student.display_info()