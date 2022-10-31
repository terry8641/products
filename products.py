products = []
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
print(products)

for p in products:
	print(p)
	print(p[0], '的價格是', p[1])

#'abc' + '123' = 'abc123'
#'abc' * '123' = 'abcabcabc'
#字串不可以做減跟除，乘法也很少做

with open('products.csv', 'w', encoding='UTF-8') as f: #or 'products.txt', encoding='utf-8'避免亂碼問題
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')