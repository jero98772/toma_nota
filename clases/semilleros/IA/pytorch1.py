#https://www.youtube.com/watch?v=4mfAThgACg8

import torch 
from sklearn.datasets import fecth_openml
from sklearn.metrics import accuracy_score

import numpy as np
cin=784
hidden=100
out=10
epochs=100
learning_rate=0.9
log_each=10

nn=torch.nn.Sequential(torch.nn.Linear(cin,hidden),torch.nn.RelU(),torch.nn.Linear(hidden,out))
outputs=nn(torch.rand(64,cin))
nn.to("cuda")

mnist=fecth_openml("mnist_784",version=1)
X,Y=mnist["data"],mnist["target"]
print(X.shape,Y.shape)
X_train, X_test, y_train, y_test = X[:60000] / 255., X[60000:] / 255., Y[:60000].astype(np.int), Y[60000:].astype(np.int)

softmax = lambda x:torch.exp(x)/torch.exp(x).sum(axis=-1,keepdims=True) 
def crossEntropy(out,target):
	logist=out[torch.arange(len(out)),target]
	loss=-logist+torch.log(torch.sum(torch.exp(out),axis=-1))
	return loss.mean()
def evaluate(x):
    model.eval()
    y_pred = model(x)
    y_probas = softmax(y_pred)
    return torch.argmax(y_probas, axis=1)


Xt=torch.from_numpy(X_train).float().cuda()
yt=torch.from_numpy(y_train).long().cuda()

for e in range(1, epochs+1): 
	y_pred = nn(X_t)
	loss = cross_entropy(y_pred, Y_t)
	l.append(loss.item())
	model.zero_grad()
	loss.backward()
	with torch.no_grad():
		for param in model.parameters():
			param -= lr * param.grad
	if not e % log_each:
		print(f"Epoch {e}/{epochs} Loss {np.mean(l):.5f}")

y_pred = evaluate(torch.from_numpy(X_test).float().cuda())
accuracy_score(y_test, y_pred.cpu().numpy())