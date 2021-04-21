
global number_of_operations
global result
number_of_operations = 0
result = 0
def printResult():
    global result
    print("the final result is:")
    print(result)
    exit(0)

def performMultiplication():
    global result
    if number_of_operations == 0:
        print("Enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 * operand2
    else:
        print("Enter operand")
        operand = int(input())
        result *= operand
    return

def performIntegerDivision():
    global result
    if number_of_operations == 0:
        print("Enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 // operand2
    else:
        print("Ebter the operand")
        operand = int(input())
        result //= operand
    return

def performFloatDivision():
    global result
    if number_of_operations == 0:
        print("Enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 / operand2
    else:
        print("Enter the operand")
        operand = int(input())
        result /= operand
    return

def performSubtraction():
    global result
    if number_of_operations == 0:
        print("enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 - operand2
    else:
        print("Enter the operand")
        operand = int(input())
        result -= operand
    return

def performAddition():
    global result
    if number_of_operations == 0:
        print("Enter two operands")
        operand1, operand2 = [int(x) for x in input().split()]
        result = operand1 + operand2
    else:
        print("Enter the operand")
        operand = int(input())
        result += operand
    return


def operation():
    global number_of_operations
    operator = input("Enter the operator")
    if operator == '+':
        performAddition() 
    elif operator == '-':
        performSubtraction()
    elif operator == '/':
        performFloatDivision()
    elif operator == '//':
        performIntegerDivision()
    elif operator == '*':
        performMultiplication()
    elif operator == '=':
        printResult()
    number_of_operations += 1
    return

while(True):
    operation()
