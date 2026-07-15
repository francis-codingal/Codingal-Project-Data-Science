# School Class Organiser
classmates = ["Francis", "Gowtham", "Viki", "Pradeep"]
print("Class List:", classmates)

print("Total students in class:",len(classmates))
print("First students:",classmates[0])
print("Last students:",classmates[-1])
print("First three students:",classmates[0:3])

classmates.append("Dinesh")
print("\n After adding Dinesh to the class list:", classmates)
classmates.remove("viki")
print("\n After removing Viki from the class list:", classmates)
classmates.sort()
print("\n Sorted alphabetically:",classmates)
classmates.reverse()
print("\n Reversed order:",classmates)

teacher={"Name":"Mr Francis", "Subject":"Computer Science", "Experience":"6 Years"}
print("\n Teacher Information:", teacher)

print("Subject:", teacher["Subject"])
print("Experience:", teacher.get("Experience","Not found"))
teacher["Experience"]=6
teacher["Email"]="francissantos.codingal@gmail.com"
teacher.pop("Experience")
print("Updated Teacher Information:", teacher)

roll_numbers=[1,2,3,4,5]
names=["Francis", "Pradeep", "Gowtham", "Viki", "Dinesh"]
student_directory=dict(zip(roll_numbers, names))
print("\n Student Directory:",student_directory)
print("Student at Roll 3:",student_directory[3])

