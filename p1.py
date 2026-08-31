inventory =[]
while True:
    print("""
1. Add item
2. View inventory
3. Remove item
4. Exit""")
    try:
        ask = int(input("Select an option"))
        if ask == 1:
            add_item = input("Add any item : ")
            inventory.append(add_item)
            print(F"{add_item} is added to inventory")
        elif ask == 2:
            for i in inventory:
                print(i)
        elif ask == 3:
            try:
               remove = input("Enter the item you want to remove : ")
               inventory.remove(remove)
               print(f"{remove} is removed from inventory")
            except ValueError:
                print("item does not exist!")
        elif ask == 4:
            break
    except ValueError:
        print("Please enter valid option!")
        
        