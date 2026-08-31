print("Welcome to our ATM!")
user1 = "MR.Mahesh"
PIN1 = 6794
balance1 = 6400
CB1 = balance1
user2 = "MR.Jinwoo"
PIN2 = 1822
balance2 = 8200
CB2 = balance2
user3 = "MR.Edward"
PIN3 = 4983
balance3  = 15500
CB3 = balance3
pin = int(input("enter your PIN"))
service = "blank"
if pin == PIN1 :
    print(f"Welcome{user1}")
    service = input("Which service do you want to use")
elif pin == PIN2 :
        print(f"Welcome{user2}")
        service = input("Which service do you want to use") 
elif pin == PIN3 :
          print(f"Welcome{user3}")
          service = input("Which service do you want to use")
else :
       print("Entered PIn is incorrect")
        
if service == "Check balance" and pin == PIN1:
       print(f"your balnce is {balance1}")
elif service == "Check balance" and pin == PIN2:
       print(f"your balnce is {balance2}")
elif service == "Check balance" and pin == PIN3:
       print(f"your balnce is {balance3}")
else :
       print("Error!")

if service == "Deposit money" and pin == PIN1:
       deposit = int(input("Enter deposit value"))
       CB1 = balance1 + deposit
       print(f"current balance left = {CB1}")
elif service == "Deposit money" and pin == PIN2:
       deposit = int(input("Enter deposit value"))
       CB2 = balance2 + deposit
       print(f"current balance left = {CB2}")
elif service == "Deposit money" and pin == PIN3:
       deposit = int(input("Enter deposit value"))
       CB3 = balance3 + deposit
       print(f"current balance left = {CB3}")
else :
       print("error")

if service == "Withdraw money" and pin == PIN1:
       withdraw = int(input("Enter the amount you want to wtihdraw"))
       CB1 = balance1 - withdraw
       print(f"current balance left = {CB1}")
elif service == "Withdraw money" and pin == PIN2:
      withdraw =  int(input("Enter the amount you want to wtihdraw "))
      CB2 = balance2 - withdraw
      print(f"current balance left = {CB2}")
elif service == "Withdraw money" and pin == PIN3:
     withdraw = int(input("Enter the amount you want to wtihdraw"))
     CB3 = balance3 - withdraw
     print(f"current balance left = {CB3}")
else :
       print("Error!")



if service == "Change pin" :
       oldpin = int(input("Enter old pin"))

       if oldpin == PIN1 :
              newpin1 =int(input("Enter new pin"))
              PIN1 = newpin1
       elif oldpin == PIN2 : 
            newpin2 =int(input("Enter new pin"))
            PIN2 = newpin2
       elif oldpin == PIN3 :
            newpin3 =int(input("Enter new pin"))
            PIN3 = newpin3