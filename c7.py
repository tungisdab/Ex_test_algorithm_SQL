class Student:
    def __init__(self, name, age, math, physical, chemistry):
        self.name = name
        self.age = age
        self.math = math
        self.physical = physical
        self.chemistry = chemistry
        self.avg = self.calculate_avg()
        self.rank = self.calculate_rank()
    
    def calculate_avg(self):
        return round((self.math + self.physical + self.chemistry) / 3, 2)
    
    def calculate_rank(self):
        avg = self.avg
        if avg >= 8.0:
            return "GIOI"
        elif avg >= 6.5:
            return "KHA"
        elif avg >= 5.0:
            return "TB"
        else:
            return "YEU"

class ManagerStudent:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def find_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None
    
    def get_gioi_students(self):
        return [student for student in self.students if student.rank == "GIOI"]
    
    def sort_students(self):
        self.students.sort(key=lambda student: (student.name, student.avg))
    
    def smartSearch(self, content):
        results = []

        exact_matches = [student for student in self.students if student.name == content]
        results.extend(exact_matches)

        partial_matches = [student for student in self.students if all(char in student.name for char in content)]
        results.extend([student for student in partial_matches if student not in results])

        return results

if __name__ == "__main__":
    manager = ManagerStudent()
    
    students_data = [
        ("Hùng", 18, 9, 8, 7),
        ("Tuấn", 18, 7, 8, 7),
        ("Khánh", 18, 5, 6, 5),
        ("Mai Anh", 18, 4, 5, 5),
        ("Huế", 18, 8, 9, 7),
        ("Linh", 18, 6, 6, 7),
        ("Ngọc", 18, 9, 9, 9),
        ("Hà", 18, 5, 4, 6),
    ]
    
    for data in students_data:
        manager.add_student(Student(*data))
    
    student = manager.find_student_by_name("Hùng")
    if student:
        print(f"Found student: {student.name}, AVG: {student.avg}, Rank: {student.rank}")
    else:
        print("Student not found")
    
    gioi_students = manager.get_gioi_students()
    print("Students with rank GIOI:")
    for student in gioi_students:
        print(f"{student.name}, AVG: {student.avg}")
    
    manager.sort_students()
    print("Sorted students:")
    for student in manager.students:
        print(f"{student.name}, AVG: {student.avg}")

    search_results = manager.smartSearch("A")
    print("Smart search results:")
    for student in search_results:
        print(f"{student.name}, AVG: {student.avg}")
        

