class Person():
	def __init__(self, name, age, address, phone):
		self.name = name
		self.age = age
		self.address = address
		self.phone = phone

	def getName(self):
		return self.name

	def setName(self, new_name):
		self.name = new_name

	def toString(self):
		return f'[Name={self.name}, Age={self.age}, Address={self.address}, Phone={self.phone}]'

person1 = Person('Hendra', 40, 'Medan Cemara', '123456789')
print(person1.toString())
# person1.setName('Justin')
# print(person1.toString())

# NOT copy by value
person2 = person1 # person2 has the same reference to person1
person2.setName('Justin')
print(person1.toString())
print(person2.toString())
