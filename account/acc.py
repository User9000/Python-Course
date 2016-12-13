

class Account:
	
	def __init__(self,filepath):
		self.path = filepath
		with open(self.path, 'r') as file:
			self.balance=int(file.read())
	
	def withdraw(self,amount):
		self.balance = self.balance-amount
	
	def deposit(self,amount):
		self.balance = self.balance + amount
		
	def commit(self):
		with open(self.path, 'w') as file:
			file.write(str(self.balance))
	
#inheritance in Python
#Checking inherits everything from Account

class Checking(Account):
	
	def __init__(self,filepath,fee):
		self.fee = fee
		Account.__init__(self,filepath)
	
	def transfer(self,amount):
		self.balance = self.balance-amount -self.fee
	
	
	
checking = Checking("balance.txt",1)
checking.transfer(90)

print(checking.balance)
checking.commit()

