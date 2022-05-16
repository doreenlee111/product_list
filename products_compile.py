#讀取檔案是否存在
products=[]
import os
if os.path.isfile('product_l.csv'):
	print('檔案在!!')
	with open('product_l.csv','r') as f:
		for line in f:
			if '商品,名稱' in line:
				continue
			x = line.strip().split(',')
			products.append(x)
else:
	print('檔案不在!!')

#讓user輸入資料
print('如要離開請輸入q')

while True:
	a = input('請輸入商品名稱')
	if a == 'q':
		break
	b = input('請輸入價錢')
	products.append([a,b])

#印出所有購買紀錄
for v in products:
	print('商品是',v[0],'價格是',v[1])


#寫入檔案
with open('product_l.csv','w') as t:
	t.write('商品,價格'+'\n')
	for c in products:
		t.write(c[0] +',' + c[1]+ '\n')
