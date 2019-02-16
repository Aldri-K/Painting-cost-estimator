import time# imports the time module
#setting variables for functions
rooms= []
roomW= []
custNum =""
DOE = ""
noRooms = 0
roomName = ""
Walls = ""
price= 0
wallD = 0
area = 0


def welcome(): #creating fumction called welcome
    # global allows the function to access the variables outside the function
    global custNum
    global DOE
    global noRooms
    print("welcome")#displays welcome
    custNum = input("What is your customer number?: ")#takes an string as input
    #REMOVED TO DECREASE USER INPUT DOE = input("What was the data of the estimate (dd/mm/yy): ")
    DOE = time.strftime("%d/%m/%y")#gets the current date
    print("Date: ",DOE)
    noRooms = int(input("How many rooms require painting: "))
    roomInputs() # calls the roomInputs function
    
def roomInputs():#creates function called roomInputs
    # global allows the function to access the variables outside the function
    global noRooms
    global roomName
    global rooms
    global walls
    global roomW
    wallpaper = "" #setting an empty variable for later use
    for i in range (0,noRooms):# loops for the amount of rooms there are
        print("please enter the name of room",(i+1),": ")# i+1 one adds 1 to i to make easier to understand
        roomName = input()
        rooms.append(roomName)#adds roomName to the list rooms
        wallpaper = input("is there wallpaper in this room? Y/N: ")
        if wallpaper[0].upper == "Y":#if the first letter of wallpaper is "Y"
            price += 70# add 70 to price
        else:# else do nothing
            pass
        print("enter the number of walls in the",roomName,": ")
        walls = input()
        roomW.append(walls)
        roomW[i] = int(roomW[i])# changes the data type to integer after it is added to the list
    ADroomInputs()# calls the ADroomInputs

def ADroomInputs():#creates function called ADroomInputs
    # global allows the function to access the variables outside the function
    global noRooms
    global roomName
    global rooms
    global roomW
    global roomPrices
    global area

    for x in range(0,noRooms): # loops for the amount of rooms there are
        for i in range (0,roomW[x]):# loops for the amount of walls there are in that room
            print("What are the dimensions of the walls in ",rooms[x]," in metres: ")
            print("Wall: ",i+1)
            wallD = int(input("Height: "))#stores the height
            wallD *= int(input("Length: "))#multiplies the height by the length which is defined by the user
            area += wallD# adds the surface area of the wall to area
    pricing()#calls the pricing fucntion


    
def pricing():#creates function called pricing
    # global allows the function to access the variables outside the function
    global price
    global area
    empType = ""#creates empty variable for later use
    price = area*15#calculates the price which is £15 per a metre
    empType = input("Would you like an apprentice or a fully qualified worker? A/F?")#asking what type of employee they would like and stores the result
    if empType[0].upper() == "A":#if the capitalised first letter of empType is "A" then add 100 to price
        price += 100
    elif empType[0].upper() == "F":#if the capitalised first letter of empType is "F" then add 250 to price
        price += 250
    print("Total cost without VAT: £",price)#displays a string and the variable price
    price *= 1.2 #multiplies price by 1.2 to add the 20 VAT
    print("Total cose with VAT: £", price)#displays string and the price with VAT
    exORa()#calls function exORa

def exORa():#creates function exORa
    restart = input("would you like to generate another estimate? Y/N:")#stores input in the variable restart
    if restart[0].upper() == "Y":# if capitalised first letter of restart is "Y" then call the function welcome
        welcome()#calls the welcome
    elif restart[0].upper() == "N":# if capitalised first letter of restart is "N" then display "Thank you bye bye"
        print("Thank you")
    

    
    
welcome()#calls the welcome
