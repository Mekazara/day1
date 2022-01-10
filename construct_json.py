import json
is_false = False
global num
while is_false == False:
    text = input("Hello. Do you want to enter student's info? 'y' or 'n': ")
    text = text.lower()
    if text == 'y':
        is_false = True
        num = int(input("How many students do you want to add?: "))
    elif text == 'n':
        print("Good bye!")
i = 0
while i != num:
    name = input("Student's name: ")
    age = input("Age: ")
    level = input("Grade level: ")
    address = input("Home address: ")
    phone_number = input("Phone number: ")
    e_mail = input("E-mail: ")
    subjects = input("Enter subjects following space: ").split()
    i = i + 1

student_info = {
    'name': name,
    'age': age,
    'level': level,
    'address': address,
    'ph_num': phone_number,
    'e_mail': e_mail,
    'subjects': subjects
}
students = []
for st in range(num):
    students.append(student_info)

with open('students.json', 'w') as json_file:
    json.dump(students, json_file, indent=2)
