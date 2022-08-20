import matplotlib.pyplot as plt
import numpy as np
import random 

def genrandomL(n,s):
	l=[]
	for i in range(s):
		l.append(random.radint(n))
	return l

size = int(input("size of X:\n"))
X=np.random.randint(low = 0, high = size, size = size) 
w =eval(input("W slope of line:\n"))#1
b =eval(input("B intercept of line:\n"))#0
y = [] 
for x in X:
	y.append(w*x+b)
print(y)
print(X)
plt.plot(X,y ,linewidth=2.0,color="b")
plt.ylabel('some numbers')
plt.show()

def objective(x):
	return x**2.0


def gradient_descent(objective, derivative, bounds, n_iter, step_size):
	solutions, scores = [],[]
	solution = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	for i in range(n_iter):
		gradient = derivative(solution)
		solution = solution - step_size * gradient
		solution_eval = solution**
		solutions.append(solution)
		scores.append(solution_eval)
		#print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
	return [solutions, scores]