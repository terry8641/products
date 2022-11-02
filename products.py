import os # operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue #跳到下一個迴圈的意思，break與continue都一定在迴圈內
				name, price = line.strip().split(',')
				products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q': #quit
			break
		price = input('請輸入商品價格: ') #需要2維清單
		price = int(price)
	#法一
	#	p = []
	#	p.append(name)
	#	p.append(price)
	#	products.append(p)
	#法二
	# 	p = [name, price]
	#	products.append(p)
	#法三
		products.append([name, price])
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

																	# Note:
																	# 'abc' + '123' = 'abc123'
																	# 'abc' * '123' = 'abcabcabc'
																	# 字串不可以做減跟除，乘法也很少做

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: #or 'products.txt', encoding='utf-8'避免亂碼問題
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #尋找並讀取檔案
		print('yeah! 找到檔案了!')
		products = read_file('products.csv')
	else:
		print('找不到檔案.....')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()