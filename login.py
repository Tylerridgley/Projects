userName = input("Please create a username:\n")
passWord = input("Please create a password:\n")

def checkPass():
    requestedUserName = input("Enter your username:\n")
    requestedPassWord = input("Enter your password:\n")
    if requestedUserName == userName and requestedPassWord == passWord:
        print("You Have successfully logged in!")
        print("Welcome", userName)
        getCommand()
    elif requestedUserName != userName or requestedPassWord != passWord:
        print("Incorrect username or password, please try again")
        askUser()
       
def askUser():
    checkPass()

def getCommand():
    userCommand = input("Enter command messageMe, log off, or quit:")
    if userCommand == "messageMe":
        print("Hello, How are you?")
        getCommand()
    elif userCommand == "log off":
        print("You have successfully logged off")
        askUser()
    elif userCommand == "quit":
        quit
askUser()






    
