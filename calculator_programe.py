# making a claculator program that uses addition, subtraction, multiplication and division

# This is the first input that the user will enter
first_number_input = input("Enter the first number: ")

# this is the opertion that the user will enter
operation_input =input( "Enter the operation you want to perform (+, -,* ,/): ")

# This is the second input that the user will enter
second_number_input = input("Enter the second number: ")

#this is the output/answer that the user will get after the operation is performed
if operation_input == "+":
    result = int(first_number_input) + int(second_number_input)
elif operation_input == "-": 
    result = int(first_number_input) - int(second_number_input)
elif operation_input == "*":
    result: int = int(first_number_input) * int(second_number_input)
elif operation_input == "/":
    result = int(first_number_input) / int(second_number_input)
else:
   print("Invalid operation")

   # answer
print(f"The result of {first_number_input} {operation_input} {second_number_input} is: {result}")
