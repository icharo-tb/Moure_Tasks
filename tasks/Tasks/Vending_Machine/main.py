import sys
#------------------COIN ARRAY------------------

coins_list = []

while True:
    coins = input('Enter a coin of value 1, 2 or 0.50 (Type -done- when finished): ')
    if coins not in ['1','2','0.5','done']:
        print('Error: This machine does not accept coins over 2€')
        coins_list.clear()
        break
    elif coins == 'done':
        break

    coins_list.append(coins)

if len(coins_list) == 0:
    sys.exit()
else:
    float_coins = [float(i) for i in coins_list]
    total = sum(float_coins)

#-----------------PRODUCT_LIST-----------------

product_list = {
    'Coke Can': 1,
    'Fanta Can': 1,
    'Water Bottle': 0.5,
    'Doritos Bag': 2
}

product_selection = input(f'Select a product from here: {product_list} (Type 1,2,3 or 4 depeding on your choice)')

for k,v in product_list.items():
    product_list[k] = float(v)

if product_selection == '1':
    price = product_list['Coke Can']
    change = total -price
    if change < 0:
        print('Not enough money. Please, insert more coins.')
    else:
        print(f'You chose Coke Can, your change is {change}.')
elif product_selection == '2':
    price = product_list['Fanta Can']
    change = total -price
    if change < 0:
        print('Not enough money. Please, insert more coins.')
    else:
        print(f'You chose Fanta Can, your change is {change}.')
elif product_selection == '3':
    price = product_list['Water Bottle']
    change = total -price
    if change < 0:
        print('Not enough money. Please, insert more coins.')
    else:
        print(f'You chose Water Bottle, your change is {change}.')
elif product_selection == '4':
    price = product_list['Doritos Bag']
    change = total -price
    if change < 0:
        print('Not enough money. Please, insert more coins.')
    else:
        print(f'You chose Doritos Bag, your change is {change}.')