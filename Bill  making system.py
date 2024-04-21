n=int(input("Enter the no of items "))
p=int(input("Enter the tax rate(if any) "))
if(p!=0):

    item = []
    price = []
    for i in range(0, n):
        item.append(input("Enter the item name "))
    for i in range(0, n):
        price.append(int(input("Enter the item prices ")))
    s = sum(price)
    total = s + ((s * p) / 100)
    print("************BILL************")
    print("Item Name \t Price")
    for i in range(0, n):
        print(item[i], "\t \t", price[i])
    print("Total \t\t", total)
    print("-----------------------------")
else:

    item = []
    price = []
    for i in range(0, n):
        item.append(input("Enter the item name "))
    for i in range(0, n):
        price.append(int(input("Enter the item prices ")))
    s = sum(price)
    print("************BILL************")
    print("Item Name \t Price")
    for i in range(0, n):
        print(item[i], "\t\t", price[i])
    print("Total \t\t", s)
    print("-----------------------------")


