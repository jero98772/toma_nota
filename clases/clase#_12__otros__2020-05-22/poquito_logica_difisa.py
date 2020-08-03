import matplotlib.pyplot  as plt
class funtions():
	#permite modelar comportamientos crecientes
	def creesiente(self,alfa,beta,sigma,x):
		self.x=x
		self.alfa = alfa
		self.beta = beta
		self.sigma = sigma
		while self.x<1:
			self.x+=0.001
			self.y=self.x/10

			if self.alfa<=self.x<=self.beta:
				self.plot=(self.x-self.alfa)/(self.beta-self.alfa)
				print("alfa")
				print(self.plot)
				plt.plot(self.x,self.plot,"bo")
			elif self.beta<=self.x<=self.sigma:
				self.plot=(self.x-self.sigma)/(self.beta-self.sigma)
				print(self.plot)
				print("sigma")		
				plt.plot(self.x,self.plot ,"bo")
			elif self.x>alfa:
				plt.plot(self.x,1)

		plt.show()
	def reversetringular(self,alfa,beta,sigma,x):
		self.x=x
		self.alfa = alfa
		self.beta = beta
		self.sigma = sigma
		while self.x>0:
			self.x-=0.001
			self.y=self.x/10

			if self.alfa>=self.x>=self.beta:
				self.plot=1-(self.x-self.alfa)/(self.beta-self.alfa)
				print("alfa")
				print(self.plot)
				plt.plot(self.x,self.plot,"bo")
			elif self.beta>=self.x>=self.sigma:
				self.plot=1-(self.x-self.sigma)/(self.beta-self.sigma)
				print(self.plot)
				print("sigma")		
				plt.plot(self.x,self.plot ,"bo")
			elif self.x>alfa:
				plt.plot(self.x,1)

		plt.show()

f=funtions()
f.creesiente(0.2,0.5,0.8,1)
#f.reversetringular(0.8,0.5,0.2,1)
