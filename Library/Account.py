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

	def checkAuthentication(self, username, password):
		return self.__username == username and self.__password == password

	def getUsername(self):
		return self.__username

