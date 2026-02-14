def add_student(name):
    with open("students.txt", "a") as file:
        file.write(name +"\n")


def view_students():
    with open("students.txt", "r") as file:
        students=file.readlines()
        for student in students:
            print(student.strip())

def delete_student(name):
    with open("students.txt", "r") as file:
        students=file.readlines()

    found=False

    with open("students.txt", "w") as file:
        for student in students:
            if student.strip()!= name:
                file.write(student)
            else:
                found=True

    if found:
        print(f"{name} deleted successfully.")
    else:
        print(f"{name}not found.")


def menu():
    while True:
        print("\n1. Add Student")
        print("2. View students")
        print("3. Delete Student")
        print("4. EXit")
        choice=input("Choose option: ")

        if choice=="1":
            name=input("Enter student name:")
            add_student(name)
        elif choice=="2":
            view_students()
        elif choice=="3":
            name=input("Enter the name of the student to be deleted:n")
            delete_student()
        elif choice=="4":
            print("Goodbye!")
            break
        else:
            print("inavlid choice")

if __name__=="__main__":
    menu()