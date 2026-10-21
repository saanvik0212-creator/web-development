classmates = ["sahasra", "Aanvi", "Tanvi", "Neha", "Rose", "Fiana"]
print("Class list:", classmates)
classmates[2]="Heyy"

print(len(classmates))
print(classmates[2:5])
classmates.append("Saanvi")
classmates.remove("Neha")
print("Newlist:",classmates)
classmates.sort()
print("classmates")
classmates.reverse()
print("updated list:",classmates)

teachers ={
    "name": "Mrs. supriya",
    "subject": "Math",
    "experience": 7

}
print("\nTeacher profile:", teachers)
print("Subject:", teachers["subject"])
print(teachers.get("experience", "not found"))

roll_numbers = [1, 2, 3, 4, 5]
names = ["Ajith", "Riya", "Sima", "Tanai", "Vrishty"]
answer = dict(zip(roll_numbers, names))
print("\nanswer:", answer)
print("Student at roll 4:",answer[4])


