import os 
# Read File
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# Let User Input
def user_input(products):
	while True:
		name  = input('Product: ')
		if name == 'q':
			break
		price = input('Price:')
		products.append([name, price])
	print(products)
	return products

# Print History
def print_products(products):
	for p in products:
		print(p[0], 'costs', p[1])

# Write File
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Product,Price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('These is such file')
		products = read_file(filename)
	else:
		print('No such file')
		products = []

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()