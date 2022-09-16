import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data=pd.read_csv("data2.csv")
print(data)
x=len(data)
for i in data.keys():
	print(x,len(data[i]))
	#fig, ax = plt.subplots()
	"""x=data["fecha"]
	try:
		y=list(map(int,data[i]))
	except:
		y=data[i]
	plt.title(i)
	plt.plot(x,y)
	#plt.show()
	plt.savefig(i)
	"""