class Account():
	# constructor need 3 parameters
	def __init__(self, username, password, name):
		self.__username = username
		self.__password = password
		self.__name = name

	def getName(self):
		return self.__name

	# Edit name function
	def setName(self, new_name):
		self.__name = new_name

	def setPassword(self, new_password):
		if (len(new_password) > 0):
			self.__password = new_password

	def checkAuthentication(self, username, password):
		return (self.__username.lower() == username.lower() and 
				self.__password == password)

	def getUsername(self):
		return self.__username

