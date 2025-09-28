from clear import clearSYS
import random
from typing import List

class Student(object):


    def __init__(self, name: str, number: int) -> None:

        self.name: str = name
        self.scores: List[int] = []
        for count in range(number):
            self.scores.append(0)

    def getName(self) -> str:

        return self.name
  
    def setScore(self, i: int, score: int) -> None:

        self.scores[i - 1] = score

    def getScore(self, i: int) -> int:

        return self.scores[i - 1]
   
    def getAverage(self) -> float:

        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self) -> int:
        return max(self.scores)
 
    def __str__(self) -> str:
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other: "Student") -> bool:
        return self.name == other.name

    def __lt__(self, other: "Student") -> bool:
        return self.name < other.name

    def __ge__(self, other: "Student") -> bool:
        return self.name >= other.name

def randScore(student: Student) -> None: 
    for i in range(1, len(student.scores) + 1):
        student.setScore(i, random.randint(70, 100))

def printStudentNames(students: List[Student]) -> None:
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student.getName()}")
    print()

def main() -> None:
    clearSYS()

    names: List[str] = ["Ken", "John", "Alice", "Bob", "Eve", "Habiba", "Tyler", "Nadia", "Water", "Kian", "Branch", "Rihanna", "Thompson", "Evelyn", "Bernard", "Hamish", "Benson", "Arran", "Stafford", "Jada", "Irwin", "Nannie", "Hill", "Hugh", "Hoover", "Poppie", "Duran", "Scarlet", "Holder", "Madiha", "Donaldson", "Stevie", "Baxter", "Myrtle", "Middleton", "Joshua", "Hess", "Mila", "Mercado", "Brendan", "Howard", "Kendra", "Walker", "Blanche", "Barnes", "Cameron", "Mullen", "Jamal", "Acevedo", "Maximus", "Rivers", "Chiara", "Finley", "Betsy", "Friedman", "Lincoln", "Blevins", "Jonah", "Beck", "Bailey", "Campbell", "Jaime", "Jefferson", "Jordan", "Paul"]
    studentCount: int = 10
    subjects: int = 5

    students: List[Student] = [Student(random.choice(names), subjects) for _ in range(studentCount)]
    for student in students:
        randScore(student)

    random.shuffle(students)
    print("Students (shuffled):")
    printStudentNames(students)

    students.sort()
    print("Students (sorted):")
    printStudentNames(students)

if __name__ == "__main__":
    main()