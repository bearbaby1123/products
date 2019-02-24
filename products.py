products = []
while True:
	name  = input('Product: ')
	if name == 'q':
		break
	price = input('Price:')
	products.append([name, price])

print(products)

for p in products:
	print('I bought a', p[0], 'for', p[1], 'dollars')
	
