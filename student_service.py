"""Service layer for student management operations."""

from student import Student


class StudentService:
    """Handles student operations (interface only)."""

    def printList(self) -> None:
        pass

    def addStudent(self, student: Student) -> None:
        pass

    def removeStudent(self, student_id: str) -> None:
        pass
