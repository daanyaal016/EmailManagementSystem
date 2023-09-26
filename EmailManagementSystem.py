#creates the text file
f = open("emails.txt", "a")

#creates menu
def Menu():
    print("Menu")
    print("-"*40)
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    
#This gets input from the user and shows information about the given name/data
def EmailLookup(records):
    #input from user for the name of a person
    name = input("Enter a name: ")
    
    #Print the email as well as with the name of the person only if it is in the records
    if name not in records:
        print("The specified name was not found")
    else:
        #Print the name and the email
        print("Name:", name)
        print("Email:", records[name])

#Adds new records in the dictionary      
def addNewRecord(records):
    #takes input for name and email to be added in the records
    name = input("Enter name: ")
    email = input("Enter email address: ")
    
    #if the name does not already exist in the record dictionary, add the name and the email in the dictionary only
    if name in records:
        print("That name already exists")
    else:
        #email is stored as the value
        records[name] = email
        print("Name and address have been added")

#The email of the person is changed with this function 
def changeEmail(records):

    #taking input from the user for the name and the new email address
    name = input("Enter name: ")
    newEmail = input("Enter the new address: ")
    
    # if the data is in the records, update the dictionary with the new email address only 
    if name not in records:
        print("The specified name was not found")
    else:
        records[name] = newEmail

        # print the updated information
        print("Information updated")

#the already existing record from the dictionary will be deleted with this function  
def deleteRecord(records):
    #For deleting the data, taking name as input
    name = input("Enter name: ")
    
    # delete the record if the name is in the record
    if name not in records:
        print("The specified name was not found")
    else:
        del records[name]
        #print information deleted message
        print("Information deleted")

#load data of email from the file through this function  
def loadDataFromFile():

    #list to store the data read from the file
    lines = []
    
    #in read mode opening the text file containing emails
    with open("emails.txt", "r") as f:

        lines = f.readlines()
    
    #dictionary for the records
    records = {}

    for line in lines:

        # email will store the two values that have been stored in the list
        email = line.split(":")
        
        #Among values stored in email, store them in dictionary
        records[email[0].strip()] = email[1].strip()
        
    #Return records dictionary
    return records
    
#function to save the data in the file
# function takes the records dictionary as the input parameter
def saveDatatoFile(records):

    #open the file in write mode
    with open("emails.txt", "w") as f:
        #write it in the file already created for each value stored in the records dictionary
        for i in records:
            f.write(i)

            #colon after writing name in the file
            f.write(":")
            
            #now after colon write the email stored as the value in the dictionary
            f.write(records[i])

            #new line after each record
            f.write("\n")
            
    print("Information saved")
    
#function for the main part of the program
def main():

    #Read data from the file and store it in the dictionary records
    records = loadDataFromFile()
    
    while True:

        #displaying the main menu to the user through this function
        Menu()
        
        print()
        
        #Take input as the choice from the main menu from the user
        choice = int(input("Enter your choice: "))
        
        #For the choice made by the user call the function already defined 
        if choice == 1:
            EmailLookup(records)
            print()
        elif choice == 2:
            addNewRecord(records)
            print()
        elif choice == 3:
            changeEmail(records)
            print()
        elif choice == 4:
            deleteRecord(records)
            print()
        elif choice == 5:
            saveDatatoFile(records)
            break
        else:
            print("Invalid input")
            print()
main()
