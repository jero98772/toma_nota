import os
import pandas as pd
folder="txt/"	
folders=os.listdir(folder)
for i in folders:
	dataframe=pd.read_csv(folder+i,sep="\t")
	diccionary={}
	for i in dataframe.index:
		#print(dataframe["# Feature"][i],dataframe["Unique Ids"][i],dataframe["Placements"][i])
		if dataframe["Unique Ids"][i]=="na":
			val1=0
		else:
			val1=int(dataframe["Unique Ids"][i])
		if dataframe["Placements"][i]=="na":
			val2=0
		else:
			val2=int(dataframe["Placements"][i])
		feature=dataframe["# Feature"][i]
		if feature in diccionary:
			diccionary[feature]=[diccionary[feature][0]+val1,diccionary[feature][1]+val2]
		else:
			diccionary[feature]=[val1,val2]
	print(diccionary)
		