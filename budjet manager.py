from datetime import datetime
def balance():
    with open("income.txt","r") as file:
         output = 0
         for i in file:
            data = i
            output += int(data)
    return output
def total():
    with open ("expense.txt","r") as list:
        total = 0
        for i in list:
          data = (i.strip().split(":"))[0]
          total += int(data)
    return total
def show():
    with open("expense.txt","r") as file:
        print("Expense : Category : Date : time")
        for i in file:
            print(i)
    t = total()
    print(f"Total expense = {t}")
def add_expense():
    try:
        a = int(input("Add your expense :"))
        b = input("Which category")
        now = datetime.now()
        with open("expense.txt","a") as file:
          file.write(f"{a} : {b} : {now.date()} : {now.time()} \n")
    except ValueError :
        print("Expense must be in number and category in text!")
def show_summary(): 
    a = total()
    b = balance() - total()
    print(f"""Total expense : {a}
Balance left : {b}""")
while True:
        try:
          print("""1. Add Income
2. Add Expense
3. View Transactions
4. Show Balance
5. Show Summary
6. Exit""")
          ask = int(input("Choose any option : "))
          if ask == 1:
                a = input("Add income")
                with open("income.txt","a") as file:
                  file.write(f"{a} \n")
                  print(f"{a} is added to income.")
          elif ask == 2:
            if total() <= 0.8*balance():
               add_expense()
            else:
                a = "80%"
                print(f"Warning You hae exceeded {a} of your income")
          elif ask == 3:
              show()
          elif ask == 4:
              a = balance()
              b = total()
              print(f"Balance left = {a-b}Rs")
          elif ask == 5:
              show_summary()
          elif ask == 6:
              break
          else:
              print("Invalid option!")
        except ValueError:
          print("Please choose a valid option(1-6)!")
