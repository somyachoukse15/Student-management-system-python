students=[]
def add_student():
    name = input("Enter name: ").strip()
    roll = input("Enter roll number: ").strip()
    branch = input("Enter branch: ").strip()

    student ={
        "name": name,
        "roll" : roll,
        "branch" : branch,
    }

    students.append(student)
    print("Student added successfully!\n")

def view_student():
    if len(students)==0:
        print("No student found.\n")
        return
    
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Branch: {s['branch']}")
        print()

def search_student():
    roll = input("Enter roll number to search: ").strip()

    for s in students:
        if s["roll"]==roll:
            print(f"Found: {s}\n")
            return
        
    print("Student not found.\n")  

def main():
    while True:
        print("1) Add Student")
        print("2) View Student")
        print("3) search Student")
        print("4) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")

main()