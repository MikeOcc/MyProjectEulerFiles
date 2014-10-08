#
#  Pickle Example
#


import pickle

class account:
	def __init__(self, id, balance):
		self.id = id
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
	def withdraw(self, amount):
		self.balance -= amount

myac = account('123', 100)
myac.deposit(800)
myac.withdraw(500)

fd = open( "archive01", "w" ) 
pickle.dump( myac, fd)
fd.close()

myac.deposit(200)
print myac.balance

fd = open( "archive01", "r" ) 
myac = pickle.load( fd )
fd.close()

print myac.balance

myac.deposit(1200)

fd = open( "archive01", "w" ) 
pickle.dump( myac, fd)
fd.close()

print myac.balance