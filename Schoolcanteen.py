orders = []
order1 = input("Enter order 1 : ")
orders.append(order1)
order2 = input("Enter order 2 : ")
orders.append(order2)
order3 = input("Enter order 3 : ")
orders.append(order3)
order4 = input("Enter order 4 : ")
orders.append(order4)
order5 = input("Enter order 5 : ")
orders.append(order5)


print("Original orders", orders)
order6 = input("Enter additional order : ")
orders.append(order6)
print("Updated orders", orders)

order7 = input("Enter priority order : ")
orders.append(order7)
orders.insert(0,order7)
print("Updated orders", orders)

