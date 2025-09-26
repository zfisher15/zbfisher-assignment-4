#part 1
student_name = "Zian"
current_gpa = 4.0
study_hours = 15
social_points = 35
stress_level = 30

print(f"Welcome, {student_name}! Your current stats are:")
print("GPA:", current_gpa)
print("Study hours:", study_hours)
print("Social points:", social_points)
print("Stress level:", stress_level)
print()

light_load = 11
standard_load = 15
heavy_load = 19
print("Choose your course load:")
print("Light load: 11 credits")
print("Standard Load: 15 credits")
print("Heavy Load: 19 credits")
#part 2
load_choice = input("Your load choice: ")

if load_choice == "Light":
    print("You chose: Light load.")
elif load_choice == "Standard":
    print("You chose: Standard load.")
    current_gpa -= 0.5
elif load_choice == "Heavy":
    print("You chose: Heavy load.")
    current_gpa -= 1.0
else:
    print("Your input was invalid.")
#part 3
class_choice = input("Which class would you like to add: Math, English, or History")
class_list = ["Math", "English", "History"]

if class_choice in class_list:
    print(f"You chose {class_choice}. This class will require 2 hours of studying.")
    study_hours += 2
elif class_choice not in class_list:
    print("Invalid option")
if (class_choice == "English" and class_choice == "History") or (class_choice == "History" and not "Math"):
    social_points += 5


