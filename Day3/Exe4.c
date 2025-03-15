def check_key(student_details):
    if find_key in student_details:
        print(f"{find_key}: was found")
    else:
        print(f"{find_key}: was not found")

student_details={
    "name":"Praveen",
    "id": 121,
    "branch":"ECE",
    "year":202
    
}

find_key=input("Enter a key to search:")
check_key(student_details);
