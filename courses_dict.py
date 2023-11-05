courses = {}

while True:
    course_info = input()
    if course_info == "end":
        break

    course_name, student_name = course_info.split(" : ")

    # Check if the course already exists, if not, create it
    if course_name not in courses:
        courses[course_name] = []

    # Register the student in the course
    courses[course_name].append(student_name)

# Print the course information
for course_name, registered_students in courses.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")
