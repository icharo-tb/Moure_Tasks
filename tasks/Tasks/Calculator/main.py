def calculator(file):

    with open(file) as f:
        fl = f.readlines()

    operations_list = []

    for operations in fl:
        operations_list.append(operations)

    for operation in operations_list:
        op = operation.strip()

        operators = op.split(' ')

        num1,operator,num2 = operators[0],operators[1],operators[2]

        # add
        if operator == '+':
            result = float(num1)+float(num2)
            print(f"{num1} {operator} {num2} = {result}")
        # substract
        elif operator == '-':
            result = float(num1)-float(num2)
            print(f"{num1} {operator} {num2} = {result}")
        # multiply
        elif operator == '*':
            result = float(num1)*float(num2)
            print(f"{num1} {operator} {num2} = {result}")
        # divide
        elif operator == '/':
            result = float(num1)/float(num2)
            print(f"{num1} {operator} {num2} = {result}")
        else:
            print('Calculator only accepts: + - * /')
    return ''
pass

print(calculator('operations.txt'))