from student import Student
from student_service import StudentService

def main():
    service = StudentService()
    while True:
        command = input("Enter command (list, add, remove, exit): ").strip()
        if command == "list":
            service.printList()
        elif command == "add":
            student_id = input("ID: ")
            name = input("Name: ")
            service.addStudent(Student(student_id, name))
        elif command == "remove":
            student_id = input("ID to remove: ")
            service.removeStudent(student_id)
        elif command == "exit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
