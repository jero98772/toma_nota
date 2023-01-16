#import matplotlib.pyplot as plt
#passed
#https://www.sololearn.com/learning/eom-project/1094/101
from sklearn.linear_model import LogisticRegression 

n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])
y = [int(x) for x in input().split()]
datapoint = [float(x) for x in input().split()]

model=LogisticRegression()
model.fit(X,y)
#plt.scatter(X,y)
#plt
pred=model.predict([datapoint])
print(*pred)