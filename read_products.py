s=[]
with open('product_list.csv','r') as f:
	for line in f:
		if '商品,名稱' in line:
			continue
		p = line.strip().split(',')
		s.append(p)

print(s)