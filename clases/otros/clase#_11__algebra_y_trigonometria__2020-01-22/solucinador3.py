op=["+","*"]
def uno():
	num = 1764
	for i in range(num):
		for j in range(num):
			if i + j== 85 or j*i == 85:
				if i+j == num or i*j == num:
					print(i,j)
#respuesta al problema yeiiii 
def dos():
	num = 700
	num2 = 200
	for i in range(num):
		for j in range(num):
			if (i**2) + (j**2) == 0 :
				print("nada no da") 
def tres():
	num = 700
	num2 = 200
	num3 = 500 
#no da con negativos 
	for i in range(1000,-10000):
		#for j in range(-10000,10000):
		if (i**2) + (num*i) + 120000 == 0 :
			print(i,j) 
#debe dar 300 y 400
tres()
