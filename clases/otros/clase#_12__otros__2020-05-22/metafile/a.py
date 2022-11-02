from b import bb
print(bb)
print(str(bb))
bb["ssid"]="gueeey"
def writetxt(name,content):
	"""
	writetxt(name,content) , write in txt file something  
	"""
	content =str(content)
	with open(name, 'w') as file:
		file.write(content)
		file.close()
writetxt("b.py","bb="+str(bb))