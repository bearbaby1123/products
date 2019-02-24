import os 

products =[]

#Check File
if os.path.isfile('products.csv'):
	print('These is such file')
	# Read File
	with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if 'Product,Price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
		print(products)
else:
	print('No such file')

# Let User Input
while True:
	name  = input('Product: ')
	if name == 'q':
		break
	price = input('Price:')
	products.append([name, price])

# Print History
print(products)
for p in products:
	print('I bought a', p[0], 'for', p[1], 'dollars')

# Write File
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

