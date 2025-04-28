student_records = {}

def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grades = input("Enter grades (comma-separated): ")
    attendance = input("Enter attendance percentage: ")
    student_records[id] = {"name": name, "grades": grades, "attendance": attendance}
    
def update_student():
    id = input("Enter student ID to update: ")
    if id in student_records:
        field = input("Enter field to update (name/grades/attendance): ")
        value = input(f"Enter new {field}: ")
        student_records[id][field] = value
    else:
        print("Student not found")
        
def display_records():
    for id, info in student_records.items():
        print(f"ID: {id}, Name: {info['name']}, Grades: {info['grades']}, Attendance: {info['attendance']}")

while True:
    choice = input("\n1. Add Student\n2. Update Record\n3. Display Records\n4. Exit\nChoice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        update_student()
    elif choice == '3':
        display_records()
    elif choice == '4':
        break
    else:
        print("Invalid choice")