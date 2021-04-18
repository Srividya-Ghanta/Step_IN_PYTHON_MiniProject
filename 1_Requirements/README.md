# Introduction
Calculator is the best friend for all of us when it comes to solving any mathematical problems.The program is designed to act like a “handheld calculator” with the usual standard functions like addition, subtraction, multiplication, division, exponentiation.

# Environment and Interface Requirements
* This section describes the external influences imposed on the calculator program.

## Hardware Requirements
* The program shall be usable on any system which supports the python interpretor and shall not require any particular hardware.

## Software Requirements
* The program shall be written in Python scripting language.The program shall use only standard python  modules to perform mathematical calculations.

## User Interface
* The console is the interface being used. Once the program started, it shall display a prmpt >>.The user can then type a sequence of numbers and operators similar to regualr calculator. The program will display the calculated answer to the entered problem in the line following the input line.

# Data flow Diagram
 The data flow diagram which identifies the major functions required of the calculator program and shows their relationship to each other.

 ![](dataflow.jpg)

 # Major Operations Performed

 ## 1. Input
 * Accept input from the user via the terminal, validate that input, and then send that input to the calculate function. All user interaction with the program will occur through this function.

 ## 2. Calculate
 * Perform calculations based on the operator provided and update the result.

 ## 3. Output
 * Display the calculated result in the terminal.

 # Functions Used in the Application

 # SWOT Analysis

 ![](SWOT.png)

 # High-Level Requirements

 |ID|Description|Domain|Status|
 |--|-----------|------|------|
 |HR_01|Input Should be taken from the console|Technical|TBI|
 |HR_02|Output should be displayed in the console|Technical|TBI|
 |HR_03|Termianate execution on noticing "=" oprator as input|Techinal|TBI|
 |HR_04|The user should be prmpted to enter the input on every interation|Techinal|TBI|
 |HR_05|The result should be the calculated value of all the oprations given by user|Techinal|TBI|
 |HR_06|Division by zero should be detected|Scenario|TBI|
 |HR_07|Only decimal of floating values have to be taken as inputs|Scenario|TBI|
 |HR_08|Calculations done in previous executions have to be maintaned in memory|Teachnical|FUTURE|

 # Low-Level Requirements

 |ID|Description|Domain|HR_ID|Status|
 |--|-----------|------|-----|------|
 |LR_01|A function to take input from the CLI have to be defined|technical|HR_01|TBI|
 |LR_02|A function to print the final result to the CLI have to be defined|Technical|HR_02|TBI|
 |LR_03|A conditional statement to match the "=" operator have to be defined|Technical|HR_03|TBI|
 |LR_04|A while loop have to be defoned to rum until "=" operator is identified|Technical|HR_04|TBI|
 |LR_05|A global variable have to be declared to hold the modified result every time an operation is performed|Technical|HR_05|TBI|
 |LR_06|A Testcase have to be declared to throw an error on occurence of division by zero|Scenario|HR_06|TBI|
 |LR_07|A conditional statement have to be defined to check the operands|Scenario|HR_07|TBI|
 |LR_08|A file have to be maintained that can be read when previous calculations are required|Technical|HR-08|FUTURE|