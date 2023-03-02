# Program stores studnets name and list of courses,
# and grades in a dictionary
# Auhtor : Clare Tubridy

student = {
        "name":"Mary",
        "modules": [
            {
                "courseName":"Programming",
                "grade": 45
            },
            {
                "courseName":"History",
                "grade": 99
            }
        ]
}

print("Student: {student['name']}")

for module in student["modules"]:
    print(f"\t {module['courseName']}\t {module['grade']}")
