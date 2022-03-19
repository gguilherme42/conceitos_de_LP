
name = input("Student name: ").strip().lower()
age = int(input(f"{name}'s age: "))
average = float(input(f"{name}'s average: "))
level = input(f"{name}'s level: ")

student_data = [name, age, average, level]
print(student_data)
