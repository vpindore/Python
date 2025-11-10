students = { 'name1': 80,
            'name2': 90,
             'name3': 70,
             'name4': 75
             }

while(True):
    studnetName = input("Enter a Student's Name:")
    if(studnetName == ''):
        break
    else:
        if studnetName in students:
            marks = students[studnetName]
            print(f"{studnetName}'s marks: {marks}");
        else:
            print(f"Student not found");

print("Goodbye")

