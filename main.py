def add_student(name):
    with open("students.txt", "a") as file:
        file.write(name +"\n")


def view_students():
    with open("students.txt", "r") as file:
        students=file.readlines()
        for student in students:
            print(student.strip())

def menu():
    while True:
        print("\n1. Add Student")
        print("2. View students")
        print("3. EXit")
        choice=input("Choose option: ")

        if choice=="1":
            name=input("Enter student name:")
            add_student(name)
        elif choice=="2":
            view_students()
        elif choice=="3":
            print("Goodbye!")
            break
        else:
            print("inavlid choice")

if __name__=="__main__":
    menu()