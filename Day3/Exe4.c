student_details={
    "name":"Praveen",
    "id": 121,
    "branch":"ECE",
    "year":2026
    
}
name=student_details["name"];
id=student_details["id"];
branch=student_details["branch"];
year=student_details["year"];

student_details["blood_group"]="A+ve"
find_key=input("Enter a key to search:")
if find_key in student_details:
    print(f"{find_key}: was found")
print(f"{find_key}: was not found")
