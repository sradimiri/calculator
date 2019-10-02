first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))
operation = input("Please enter the operation: ")

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "/":
    print(first_num / second_num)
elif operation == "*":
    print(first_num * second_num)
else:
    print("Error!")