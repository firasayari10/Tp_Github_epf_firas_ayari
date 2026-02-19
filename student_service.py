from student import Student

class StudentService:
    def __init__(self):
        self._students: list[Student] = []

    def printList(self):
        if not self._students:
            print("No students found.")
            return
        print("Students:")
        for s in self._students:
            print(f"- {s.student_id}: {s.name}")

    def addStudent(self, student: Student):
        if any(s.student_id == student.student_id for s in self._students):
            print(f"Student id {student.student_id} already exists.")
            return False
        self._students.append(student)
        return True

    def removeStudent(self, student_id: str):
        for s in self._students:
            if s.student_id == student_id:
                self._students.remove(s)
                return True
        print(f"Student id {student_id} not found.")
        return False
    def export_csv(self, file_path: str):
        """Export students to a CSV file."""
        import csv
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name"])
            for s in self._students:
                writer.writerow([s.student_id, s.name])
