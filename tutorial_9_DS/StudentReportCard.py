# from file
# database
# from user input

# name, age, phone, email, subjects with marks

# student = {
#     "name": "Ramesh",
#     "age": 22,
#     "contacts": ["98765", "ramesh@gmail.com"],
#     # "contacts": {
#     #     "phones": [7876557,9877665],
#     #     "emails": ["ramesh@gmail.com"],
#     #     "address": ["Ghaziabad", "Pune"]
#     # }
#     "subjects": {
#         "Math": 78, "Eng": 81, "Computer": 83, "EVS": 79
#         }
# }

# student2 = {
#     "name": "Mahesh",
#     "age": 21,
#     "contacts": ["98765", "mahesh@gmail.com"],
#     "subjects": {
#         "Math": 67, "Eng": 68, "Computer": 86, "EVS": 73
#         }
# }


# students = [student, student2]


students = [
    {
        "name": "Ramesh",
        "age": 22,
        "contacts": ["98765", "ramesh@gmail.com"],
        "subjects": {
            "Math": 78, "Eng": 81, "Computer": 83, "EVS": 79
        }
    },
    {
        "name": "Mahesh",
        "age": 21,
        "contacts": ["98765", "mahesh@gmail.com"],
        "subjects": {
            "Math": 67, "Eng": 68, "Computer": 86, "EVS": 73
        }
    }    
]



for i in range(len(students)):
    # print(students[i])
    # print(students[i]["name"])
    # print("----")
    print(f"\n\t\tStudent {i+1} Details")
    print("-"*40)
    print(f'Name: {students[i]["name"]}\t\tAge: {students[i]["age"]}')
    print("-"*40)
    print("Contact Details")
    print(f'\tPhone: {students[i]["contacts"][0]}')
    print(f'\tEmail: {students[i]["contacts"][1]}')
    print("-"*40)
    for key in students[i]["subjects"]:
        print(f'Subject: {key}\t\tMarks: {students[i]["subjects"][key]}')
    print("-"*40)
