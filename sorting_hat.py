student_names = input()
voldemort_encounter = False

while student_names != "Welcome!":

    if student_names == "Voldemort":
        print("You must not speak of that name!")
        voldemort_encounter = True
        break
    elif len(student_names) < 5:
        print(f"{student_names} goes to Gryffindor.")
    elif len(student_names) == 5:
        print(f"{student_names} goes to Slytherin.")
    elif len(student_names) == 6:
        print(f"{student_names} goes to Ravenclaw.")
    elif len(student_names) > 6:
        print(f"{student_names} goes to Hufflepuff.")

    student_names = input()

if not voldemort_encounter:
    print("Welcome to Hogwarts.")