products = [
    [1, 'Hand Bag', 50],
    [2, 'Scented Candles', 25],
    [3, 'Wooden Decor', 80],
    [4, 'Small Rug', 120],
    [5, 'Photo Frame', 30]
]

print('Handicraft Store')

for product in products:
    num = product[0]
    name = product[1]
    price = product[2]
    print(str(num) + ' - ' + name + ' - ' + str(price) + ' SAR')

choice = input('Enter product number: ')

if choice == '1':
    price = 50
elif choice == '2':
    price = 25
elif choice == '3':
    price = 80
elif choice == '4':
    price = 120
elif choice == '5':
    price = 30
else:
    print('Wrong number')
    price = 0

if price > 0:
    tax = price * 0.15
    total = price + tax
    print('Price with tax: ' + str(total))