products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格: ') #需要2維清單
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