import os  #operating system

#讀取檔案
def read_file(filename):
	products = []
	if os.path.isfile(filename):#尋找當下路徑是否有這個檔案，若為其他路徑則須提供完整路徑


		with open(filename, 'r') as f:
			for line in f:
				if '商品,價格' in line:  #跳過商品價格
					continue 
				[name, price] = line.strip().split(',')
				products.append([name, price])
	else:
		print('找不到檔案')
	return products

#建立新菜名與價格
def user_input(products):
	
	print('建立菜單嚕~')
	while True:
		name = input('請輸入餐點：(q=離開)')
		if name == 'q':
			break
		price = input('請輸入價格')
		products.append([name, price])
	print(products)
	return products

#詢問菜名與價格
def ques_menu(products):
	m = 0
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

#寫入檔案
def wirte_file(filename, products):

	with open(filename, 'w') as f:
	#encoding='utf-8'，為了修正亂碼問題，用utf-8通用的編碼
	#with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


products = read_file('products.csv')
products = user_input(products)
ques_menu(products)
wirte_file('products.csv', products)