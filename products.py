import os # operating system

products = []
if os.path.isfile('products.csv'): #尋找並讀取檔案
	print('yeah! 找到檔案了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳到下一個迴圈的意思，break與continue都一定在迴圈內
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案.....')






#讓使用者輸入
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

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# Note:
# 'abc' + '123' = 'abc123'
# 'abc' * '123' = 'abcabcabc'
# 字串不可以做減跟除，乘法也很少做

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #or 'products.txt', encoding='utf-8'避免亂碼問題
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')