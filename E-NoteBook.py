import os
def display_menu():
    print("\nWelcome to Python E - Note:\n")
    print("Press 1 for Generate Note")
    print("Press 2 for View Note")
    print("Press 3 for Exit\n")

def generate_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    filename = f"{title.lower().replace(' ', '_')}.txt"
    with open(filename, 'w') as file:
        file.write(content)

    print(f"\nNote '{title}' generated successfully!")

def view_notes():
    print("\nList of Available Notes:")
    for file_name in os.listdir():
        if file_name.endswith(".txt"):
            with open(file_name, 'r') as file:
                print(f"\n--- {file_name} ---\n{file.read()}")

def handle_invalid_input():
    print("Invalid input! Please enter a valid option.")

if __name__ == "__main__":
    while True:
        display_menu()

        choice = input("Enter your choice : ")
        
        if choice == "1":
            generate_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting the E-Note Book. Goodbye!")
            break
        else:
            handle_invalid_input()

        input("\nPress Enter to continue...")