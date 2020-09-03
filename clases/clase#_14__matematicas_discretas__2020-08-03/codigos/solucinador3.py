op=["+","*"]
def uno():
	num = 12375
	for i in range(num):
		for j in range(num):
			if 165 * i + j == num:	
				print(i,j)
uno()
