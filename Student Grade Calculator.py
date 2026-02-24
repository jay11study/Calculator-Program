# Student Grade Calculator
name = input("Enter student name: ")

mark1 = float(input("Enter mark 1 (0-100): "))
mark2 = float(input("Enter mark 2 (0-100): "))
mark3 = float(input("Enter mark 3 (0-100): "))

total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

# Grade logic
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Printing Result
print(f"\n{name}")
print(f"Total: {total}/300")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
