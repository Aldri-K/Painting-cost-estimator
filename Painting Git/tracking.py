
def search():# creates function called search
    file = open("paintingJobs.txt","r")#save the text file in the variable file and only allow me to read from it
    estSearch = input("Enter the estimate numnber you are looking for:\n")#takes the input and saves it in estSearch
    found = False#sets found to false
    for eachline in file:#creates from loop to loop for each line in the text file
        line = eachline.split(",")#splits eachline where there is a comma
        if estSearch == line[0]:#if estSearch equals line[0]
            found = True#set found to true
            #displays the string and a section of line
            print("Estimate Number:",line[0])
            print("Customer ID:",line[2])
            print("Estimate Total:",line[3])
            print("Estimate Date:",line[1])
            if line[4] == "E":#if line[4] is "E"
                print("Status: Estimate")#display "Status: Estimate"
            elif line[4] == "A":#if line[4] is "A"
                print("Status: Accepted")#display "Status: Accepted"
            elif line[4] == "N":#if line[4] is "N"
                print("Status: Not Accepted")#display "Status: Not Accepted"
            break# stops the loop
        #else do nothing
        else:
            pass

    if found == False:# if found is Fasle
        print("The estimate you are searching for cannot be found"
              "\nWould you like to try again Y/N:\n")#asks the user if they would like to try again
        again = input()#stores the input in again
        if again[0].upper() == "Y":# if the first capitalised letter of again is "Y"
            search()#call the function search
        #else do nothing
        else:
            pass
    #else do nothing
    else:
        pass
    restart()#call function restart

def outPayments():#creates function called outPayments
    #setting empty variables
    estNum = ""
    CustID = ""
    FinalT= ""
    AmountP = ""
    AmountOut = ""
    Totout = 0
    file = open("paintingJobs.txt","r")#save the text file in the variable file and only allow me to read from it
    outstanding = []#creates list outsanding
    for eachline in file:# loops for the amount of lines in file
        line = eachline.split(",")#slpits  the line by the comma and saves it in teh variable called line
        if line[4] == "A" and line[5]<line[3]:#if line[4] is "A" and line[5] is less than line[3]
            outstanding.append(eachline)#add the line to the list outstanding
        #else do nothing
        else:
            pass
    #display the strings in the middle of 15 spaces 
    print("{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}".format("Estimate Number","Customer ID","Final Total","Amount Paid","Amount Outstanding"))
    for item in outstanding:#loops for the amount of items in outstanding
        line = item.split(",")# splits the items where there is a comma and saves it in a list line
        #setting the value of variables to sections of the list line
        estNum = line[0]
        CustID = line[2]
        FinalT= int(line[3])
        AmountP = int(line[5])
        AmountOut = FinalT-AmountP
        Totout += int(AmountOut)
        # displaying the variables in a space of 15
        print("{0:^15}{1:^15}{2:^15}{3:^15}{4:^15}".format(estNum,CustID,FinalT,AmountP,AmountOut))
    Totout = str(Totout)
    print("{0:>60}{1:^15}".format("Total Amount Outstanding: ",Totout))
    restart()# calls function restart

def revenue():#creates function called revenue
    revenue = 0#sets the value of revenue to 0
    file = open("paintingJobs.txt","r")#save the text file in the variable file and only allow me to read from it
    for eachline in file:# loops for the amount of lines in the file
        line = eachline.split(",")#splits the line where there is a comma
        num = line[5]#setting the value of num to the fifth item in the list line
        num = num[:-1]#removing the last character from the variable num
        if line[4] == "A" and num==line[3]:#if line[4] equals "A" and num is equal to line[3]
            revenue += int(line[3])#add the integer value of line[3] to revenue
        #else do nothing
        else:
            pass
    print("The company revenue is £",revenue)#display "The company revenue is £" and the variable revenue
    restart()#calls function restart


def restart():#creates function called restart
    restart = input("would you like to start again? Y/N: \n")#takes input and saves it in the variable restart
    if restart[0].upper() == "Y":#if the first capitalised letter of restart is "Y"
        start()#call the function start
    #else do nothing
    else:
        pass


def start():#creates function called start
    print("Welcome\n")#displays welcome message
    option = input("Would you like to:\na.search for an estimate\nb.Display outstanding payments\nc.Display total revenue\nQ.Quit\n")#saves input into the varialbe option
    if option[0].upper() == "A":#if the first upper case letter of option is "A"
        search()#calls the function search
    elif option[0].upper() == "B":#if the first upper case letter of option is "B"
        outPayments()#calls the function outPayments
    elif option[0].upper() == "C":#if the first upper case letter of option is "C"
        revenue()#calls the function revenue
    elif option[0].upper() == "Q":#if the first upper case letter of option is "Q"
        pass#do nothing

start()#calls the function start                 
    
