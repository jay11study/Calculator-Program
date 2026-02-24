# Result Check
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("""Enter one of the operator:
+
-
*
/
""")

if operation == "+":
    result = num1 + num2
    print("You have selected + Operation")
    print("Result = ", result)

elif operation == "-":
    result = num1 - num2
    print("You have selected - Operation")
    print("Result = ", result)

elif operation == "*":
    result = num1 * num2
    print("You have selected * Operation")
    print("Result = ", result)

elif operation == "/":
    if num2 == 0:
        print("Division by zero is not allowed !!")
    else:
        result = num1 / num2
        print("You have selected / Operation")
        print("Result = ", result)

else:
    print("Please enter the valid operator !! ")
    
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")
