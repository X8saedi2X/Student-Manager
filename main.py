from manager import StudentManager
from time import sleep


manager = StudentManager()
manager.load_from_json()


while True:
    command = input(f"what do you want to do ?  ")

    if command == "add_student":
        try :
            print(f" adding new student... ")
            name = input("enter the name: ")
            score = float(input("Enter score: "))   

            manager.add_student(name, score)
            manager.save_to_json()
            sleep(0.5)
        except ValueError as error:
            print(error)


    elif command == "show_student":
        manager.show_student()
        sleep(0.5)


    elif command == "search_student":
        try:
            search = int(input("please enter student id to find ... "))
            manager.search_student(search)
            sleep(0.5)
        except ValueError as error:
            print(error)


    elif command == "delete_student":
        try:
            search = int(input("please enter student id to delete... "))
            manager.delete_student(search)
            manager.save_to_json()
            sleep(0.5)
        except ValueError as error:
            print(error)


    elif command == "exit":
        sleep(0.5)
        if manager.exit(command):
            break


    else:
        print("invalid input \n please try again")
        sleep(2)

