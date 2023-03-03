# WAP to store the student information in a dictionary as a key-value pair. The program should keeps the
# records of 10 students and display the name and marks of 10 students in decreasing order.

students = []
for i in range(10):
    name = input("Enter name of student: ")
    marks = int(input("Enter marks: "))
    students.append({'name': name, 'marks': marks})

# sort students by marks in descending order
students.sort(key=lambda x: x['marks'], reverse=True)

# write student information to a file
with open("students.txt", "w") as f:
    for student in students:
        f.write("Name: " + student['name'] + "\n")
        f.write("Marks: " + str(student['marks']) + "\n")
        f.write("---\n")