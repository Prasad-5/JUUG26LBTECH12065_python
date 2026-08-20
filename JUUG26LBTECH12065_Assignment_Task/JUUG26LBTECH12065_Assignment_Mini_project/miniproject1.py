#Mini Project: Unit converter or bill generator
products = []

for i in range(4):
    name = input(f"Enter product {i+1} name: ")
    price = int(input(f"Enter price of {name}: "))
    products.append([name, price])

print("\n----- BILL -----")

total = 0

for item in products:
    print(item[0], "=", item[1])
    total += item[1]

print("----------------")
print("Total Bill =", total)
