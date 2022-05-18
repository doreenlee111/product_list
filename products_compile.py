#讀取檔案是否存在


def import_file(file):
	products=[]
	import os
	if os.path.isfile(file):
		print('檔案在!!')
		with open(file,'r') as f:
			for line in f:
				if '商品,名稱' in line:
					continue
				x = line.strip().split(',')
				products.append(x)
	else:
		print('檔案不在!!')
	return products

#讓user輸入資料
def user_input(products):
	print('如要離開請輸入q')
	while True:
		a = input('請輸入商品名稱')
		if a == 'q':
			break
		b = input('請輸入價錢')
		products.append([a,b])
	return products

#印出所有購買紀錄
def print_products(products):
	for v in products:
		print('商品是',v[0],'價格是',v[1])


#寫入檔案
def products_write(file, products):
	with open(file,'w') as t:	
		print('商品,價格')
		for c in products:
			t.write(c[0] +',' + c[1]+ '\n')	



products = import_file(file)
products = user_input(products)
print_products(products)
products_write(file, products)