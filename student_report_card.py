class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


def main():
    name = input("Enter student name: ")
    student = Student(name)

    while True:
        entry = input("Enter a grade (or 'done' to finish): ")
        if entry.lower() == 'done':
            break
        try:
            grade = float(entry)
            student.add_grade(grade)
        except ValueError:
            print("Please enter a valid number.")

    avg = student.average_grade()
    print(f"\n{student.name}'s average grade is {avg:.2f}")


if __name__ == "__main__":
    main()
