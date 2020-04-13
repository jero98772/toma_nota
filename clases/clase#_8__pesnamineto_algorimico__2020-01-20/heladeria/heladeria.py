class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        self.icecreem1 = []
        self.icecreem = []
        self.icecreem1.append(self.toppings)
        self.icecreem1.append(self.ingredients)
        for i in self.icecreem1:
            for j in i:
                self.icecreem.append(j)
        else:
            return self.icecreem
        """for ing in self.ingredients:
                for top in self.toppings:
                    self.icecreem.append(top)
            self.icecreem.append(ing)
            """

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
