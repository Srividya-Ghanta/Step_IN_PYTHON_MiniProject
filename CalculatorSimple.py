'''
@Brief: Function to perform Addition Operation
@Parameter : integer operand1, integer operand2
@return: Sum of the operands
'''

def performAddition(operand1, operand2):
    return (operand1 + operand2)

'''
@Brief: Function to perform Suntraction Operation
@Parameter : integer operand1, integer operand2
@return: difference between the two operands
'''

def performSubtraction(operand1, operand2):
    return (operand1 - operand2)

'''
@Brief: Function to perform Float division Operation
@Parameter : integer operand1, integer operand2
@return: floating point quotient of the two operands
'''

def performFloatDivision(operand1, operand2):
    return (operand1 / operand2)

'''
@Brief: Function to perform Integer division Operation
@Parameter : integer operand1, integer operand2
@return: quotient of the operands
'''

def performIntegerDivision(operand1, operand2):
    return (operand1 // operand2)

'''
@Brief: Function to perform Modulous Operation
@Parameter : integer operand1, integer operand2
@return: remainder of the two operands
'''

def performModulous(operand1, operand2):
    return (operand1 % operand2)

'''
@Brief: Function to perform Multiplication Operation
@Parameter : integer operand1, integer operand2
@return: product of the two operands
'''

def performMultiplication(operand1, operand2):
    return (operand1 * operand2)

'''
@Brief: Function to read from a file the result calculated in previous execution
@Parameter : None
@return: None
'''

def printPreviousResult():
    with open("Memory.txt", "r") as file:
        prevResult = int(file.read())
        print(prevResult)

'''
@Brief: Function to perform power Operation
@Parameter : integer operand1, integer operand2
@return: base rised to the power of the exponent
'''

def performPowerOperation(base, exponent):
    return (base ** exponent)

'''
@Brief: Function to print the final result
@Parameter : integer result value
@return: None
'''
def printResult(result):
    print("The result of the operation is:",result)
    return

'''
@Brief: Function to take the operator as the input
@Parameter : None
@return: None
'''

def operation():
    operator =  input("Enter the operation you want to perform: ")
    if operator == "+":
        print("Enter the operands to perform Addition")
        operand1, operand2 = [int(x) for x in input().split()]
        result = performAddition(operand1, operand2)
    elif operator == "-":
        print("Enter the operand to perform subtraction")
        operand1, operand2 = [int(x) for x in input().split()]
        result = performSubtraction(operand1, operand2)
    elif operator == '/':
        print("Enter the operands to perform float division")
        operand1, operand2 = [int(x) for x in input().split()]
        result = performFloatDivision(operand1, operand2)
    elif operator == '//':
        print("Enter the operands to perform integer division")
        operand1, operand2 = [int(x) for x in input().split()]
        result = performIntegerDivision(operand1, operand2)
    elif operator == "%":
        print("Enter the operand to perform moduloue operation")
        operand1, operand2 = [int(x) for x in input().split()]
        result = performModulous(operand1, operand2)
    elif operator == "*":
        print("Enter the operands to perform multiplication")
        operand1, operand2 = [int(x) for x in input().split()]
        result = performMultiplication(operand1, operand2)
    elif operator == "**":
        print("Enter the base and exponent for the power operation")
        base, exponent = [int(x) for x in input().split()]
        result = performPowerOperation(base, exponent)
    elif operator == "M":
        printPreviousResult()
    elif operator == "E":
        exit()
    if operator != "M": # After every calculation store the result in a file
        printResult(result)
        with open("Memory.txt","w") as file:
            file.write(str(result))
    return

'''
@Brief: Main function
@Parameter : None
@return: None
'''

def main():
    while(True):
        operation()

if __name__ == '__main__':
    main()
    