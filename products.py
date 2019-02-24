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

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

