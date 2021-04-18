class Budget:
    
    def __init__(self, category):
        self.category = category
        self.amount = 0   
            
    def deposit(self, amount):
        self.amount += amount
        print(f"You have deposited {amount} to the {self.category} category")
        print(self.check_balance())
        
    def withdraw(self, amount):
        if amount <= self.amount and amount > 0:
            self.amount -= amount
            print(f"You have withdrawn {amount} from the {self.category} category")
            print(self.check_balance())
        else:
            print(f"Insufficient balance in {self.category} category\n")    
                 
        
    def transfer(self, destination, amount):
        if amount <= self.amount and amount > 0:
            self.amount -= amount
            destination.amount += amount
            print(f"You've successfully transferred {amount} from the {self.category} category to {destination.category} category")
            print(f"The current balance of the {self.category} category is {self.amount} while that of {destination.category} is {destination.amount}\n")
        else:
            print(f"Insufficient balance in {self.category} category, can not complete transfer\n")
    
    def check_balance(self):
        return f"The current balance of the {self.category} category is {self.amount}\n"



#Tests

#food_budget = Budget("food")
#clothings_budget = Budget("clothings")
#entertainment_budget = Budget("entertainment")

#food_budget.deposit(4500)
#clothings_budget.deposit(7000)
#entertainment_budget.deposit(2000)

#food_budget.deposit(1300)
#clothings_budget.withdraw(1000)
#entertainment_budget.transfer(clothings_budget, 900)
#print(entertainment_budget.check_balance())

#food_budget.withdraw(0)
