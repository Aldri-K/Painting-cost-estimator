
def start(): # creates function called start
    #creating variables
    EmpId = 0
    EmpName = ""
    EmpNum = 0
    EmpQual = ""
    print("Employee details: \n")
    # validating information, if it is invalid it will re-ask the user to enter the information

    while len(str(EmpId)) <= 1: # while the length of EmpId is less than or equal to 1 this will loop
        EmpId = input("please enter the employee's ID (Employee's for digit code): ")

    while len(EmpName) <= 0: # while the length of EmpName is less than or equal to 0 this will loop
        EmpName = input("please enter the employee's name: ")

    while len(str(EmpNum)) < 11:# while the length of EmpNum is less than 11 this will loop
        EmpNum = int(input("please enter the employee's telephone number: "))

    while EmpQual != "AP" and EmpQual != "FQ": # while EmpQual isn't equal to "AP" and EmpQual isn't equal to "FQ"
        EmpQual = input("What is the employee's qualification level?: ")
        EmpQual = EmpQual.upper() # capitalising the variable
    if EmpQual[0] == "A":# if the first letter of EmpQual is "A"
        EmpQual = "Apprentice" # sets the value of EmpQual to "Apprentice"
    elif EmpQual[0] == "F":# if the first letter of EmpQual is "F"
        EmpQual = "Fully Qualified"# sets the value of EmpQual to "Fully Qualified"

    #displaying variables with strings
    print ( "Employee ID:",EmpId,
            "\nEmployee name: ", EmpName,
            "\nEmployee telephone number: ", EmpNum,
            "\nEmployee Qualification:",EmpQual)
    
    infoCheck() #calls the infoCheck function

def infoCheck():# creates function called infoCheck
    Check = input("Is this information correct? Y/N: ")
    if Check[0].upper() == "Y": #the first letter of the variable check is capitalised and checked if it equal to "Y"
        print("Thank you for providing this information")
    else:# if the first if statement is false it will do everything under the else statement
        print("please re-enter your information")
        start()
        
    
#calling the function
start()



