products=[]

print('輸入完後輸入q以退出')

while True:
	item = input('please input product')
	if item == 'q':
		break
	price = input('please input price')
	products.append([item,price])


print(products)