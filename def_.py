def calculator():
    def add(f_num, s_num):
        return f_num + s_num

    def subtract(f_num, s_num):
        return f_num - s_num

    def multiply(f_num, s_num):
        return f_num * s_num

    def divide(f_num, s_num):
        return f_num / s_num

    print("""Add(+)\nSubtract(-)\nMultiply(*)\nDivide(/)\n""")

    first_number = float(input("First_number: "))

    operator = input("Choice operator: ")
    second_number = float(input("Second_number: "))

    if operator == "+":
        print(add(first_number, second_number))

    elif operator == "-":
        print(subtract(first_number, second_number))

    elif operator == "*":
        print(multiply(first_number, second_number))

    elif operator == "/":
        print(divide(first_number, second_number))

    else:
        print("Wrong operator. Error: 1723")
    exit()


calculator()
