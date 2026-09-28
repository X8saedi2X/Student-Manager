from manager import StudentManager
from time import sleep
from utils import clean_text


manager = StudentManager()
manager.load_from_json()


while True:
    print("""
            menu ...
            1. add_student
            2. show_students
            3. search_student
            4. delete_student
            5. exit
""")
    command = input(f"what do you want to do ?  ")

    if command == "1":
        try :
            print(f" adding new student... ")
            name = clean_text(input("enter the name: "))
            score = float(input("Enter score: "))   

            manager.add_student(name, score)
            manager.save_to_json()
            sleep(0.5)
        except ValueError as error:
            print(error)


    elif command == "2":
        manager.show_students()
        sleep(0.5)


    elif command == "3":
        try:
            search = int(input("please enter student id to find ... "))
            manager.search_student(search)
            sleep(0.5)
        except ValueError as error:
            print(error)


    elif command == "4":
        try:
            search = int(input("please enter student id to delete... "))
            manager.delete_student(search)
            manager.save_to_json()
            sleep(0.5)
        except ValueError as error:
            print(error)


    elif command == "7":
        break


    else:
        print("invalid input \n please try again")
        sleep(2)








