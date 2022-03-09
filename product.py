products = []
m = 0
print('建立菜單嚕~')
while True:
	name = input('請輸入餐點：(q=離開)')
	if name == 'q':
		break
	price = input('請輸入價格')
	products.append([name, price])
print(products)
while True:
	q = input('您有要詢問的嗎?餐點/價格/q(離開)')
	if q == '餐點':
		n = input('您要詢問什麼餐點:')
		for a in products:
			if n == a[0]:
				print(n, '的價格為', a[1])
				m += 1
		if m == 0:
			print('沒有賣這餐點喔~')
	elif q == '價格':
		n = input('您要詢問哪個價位:')
		for a in products:
			if n == a[1]:
				print(n, '價格的餐點有', a[0])
				m += 1
		if m == 0:
			print('沒有這價位的餐點喔~')					
	else:
		break
with open('products.csv', 'w') as f:
#encoding='utf-8'，為了修正亂碼問題，用utf-8通用的編碼
#with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
