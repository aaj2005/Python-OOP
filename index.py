import datetime
class People:
	def __init__(self, first,last,phone,money):
		self.firstName = first
		self.lastName = last
		self.phoneNumber = phone
		self.money = money
	def fullname(self):
		return '{} {}'.format(self.firstName,self.lastName)

	def __repr__(self):
		return self.fullname()
	def __len__(self):
		return len(self.fullname())
	@classmethod
	def totalPeople(cls):
		return Employee.empCount + Customer.custCount


class Employee(People):
	empCount = 0
	bonus = 1.04

	def __init__(self, first,last,phone,pay,money):
		super().__init__(first,last,phone,money)
		self.email = "{}.{}@banking.com".format(self.firstName,self.lastName)
		self.pay = pay 
		Employee.empCount+=1

	def setBonus(self,amount):
		self.bonus=amount

	def setRaise(self):
		self.pay *= self.bonus
	
	@classmethod
	def len(cls):
		return cls.empCount

class Customer(People):
	interest = 1.001
	custCount= 0

	def __init__(self, first,last,phone,email,money):
		super().__init__(first,last,phone,money)
		self.email = email
		Customer.custCount+=1
	
	@staticmethod
	def if25():
		if datetime.datetime.now().day == 25:
			return True
		else:
			return False

	def addInterest(self):
		if Customer.if25():
			self.money *=  self.interest
	@classmethod
	def len(cls):
		return cls.custCount


emp_1= Employee("James","Smith",30014322,15000,2100)
emp_2= Employee("Adam","Tyler",12912120,15000,900)

cust_1= Customer("Sam","Chui",15923844, 'Sam.Chui@email.com',10000)

emp_2.setBonus(1.05)

emp_2.setRaise()
emp_1.setRaise()
Customer.interest = 1.0001
cust_1.addInterest()

print("Customer Count -->",Customer.len())
print("Employee Count -->",Employee.len())
print("Total Count -->",People.totalPeople())
print("Customer 1 Fullname Count -->",len(cust_1))
print("Customer 1 Money -->",cust_1.money)




