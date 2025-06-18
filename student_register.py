def register_students():
    try:
        number_students = int(input("How many students are registering? "))
    except FileNotFoundError:
        print("Please enter a valid number.")
        return
    with open("reg_form.txt", "w") as file:
        for i in range(number_students):
            student_id = input(f"Enter student ID {i + 1}: ")
            file.write(f"{student_id}\n")

    print(f"\n{number_students} Registered Students")

register_students()
