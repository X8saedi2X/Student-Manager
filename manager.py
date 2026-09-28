from student import Student
import json


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self,name,score):
        if self.students:
            new_id = max(student.id for student in self.students) + 1
        else:
            new_id = 1

        new_student = Student(new_id, name, score)
        self.students.append(new_student)

    def show_student(self):
        for student in self.students:
            print(student.id , student.name , student.score)

    def search_student(self,id):
        find = False
        for student in self.students:
            if student.id == id:
                print(f"student is find \n {student.id} - {student.name} - {student.score} ")
                find = True 
                break
        if not find:
            print("student not find !!! ")

    def delete_student(self,id):
        find = False
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                find = True
                break
        if not find:
            print("student is not exict for delete !!! ")

    def exit (self,command):
        if command == "exit":
            return True
        else:
            print("invalid input")
            return False


    def load_from_json(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)

            for item in data:
                student = Student.from_dict(item)
                self.students.append(student)
        except FileNotFoundError:
            self.students = []

    def save_to_json(self):
        data =[]
        for student in self.students:
            data.append(student.to_dict())

        with open("students.json" , "w") as file:
            json.dump(data , file)



