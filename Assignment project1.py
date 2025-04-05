item = []
def add_item():
    BarCode = input("Bar Code :")
    name = input("Enter name :")
    ctg = input("Enter Catagory :")
    price = input("Enter price : ")
    A = {"BarCode":BarCode, "name":name, "ctg":ctg, "price":price}
    item.append(A)

def view_item():
    for i in item:
        print("Bar Code :{} , Name : {}, Catagory : {}, Price : {}".format(i["BarCode"], i["name"], i["ctg"], i["price"]))
        

def search_item(BarCode):
    for i in item :
        if (BarCode == i["BarCode"]):
            print("Bar Code :{} , Name : {}, Catagory : {}".format(i["BarCode"], i["name"], i["ctg"], i["price"]))
            break
    else:
        print("Item not found")    

def delete_item(BarCode):
    for i in range(len(item)):
        if (BarCode == item[i]["BarCode"]):
            item.pop(i)
            print("Item removed")
            break

    else:
        print("Item not found!!")



while(True):
    print("Welcome to item storage facility.","How can I help you?")  
    print("1. Add item")  
    print("2. View item")  
    print("3. Search item")  
    print("4. Delete item") 
    print("0. Exit")  
    choice = int(input("Enter your choice :"))

    match(choice):
        case 1:
            add_item()

        case 2:
            view_item()

        case 3:
            BarCode = input("Enter Bar code :")
            search_item(BarCode)

        case 4:
            BarCode = input("Enter Bar Code :")
            delete_item(BarCode)


        case 0:
            print("Have a nice day. Thank you <3") 
            break  

        case _:
            print("invalid choice")  