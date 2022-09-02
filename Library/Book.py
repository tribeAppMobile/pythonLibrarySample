import os # OS related - find file
import pickle

# Book Class ( Parent / Super / Base Class)
class Book():
	def __init__(self, name, author, isbn, category):
		# Properties
		# Book Name
		# Author
		# ISBN
		# __ : private, _ : protected
		self.__name = name
		self.__author = author
		self.__isbn = isbn
		self._category = category

	# Get/Set Function (Member functions)
	# Book Name
	def getName(self):
		return self.__name
	def setName(self, new_name):
		self.__name = new_name
	# Author
	def getAuthor(self):
		return self.__author
	def setAuthor(self, new_author):
		self.__author = new_author
	# ISBN
	def getISBN(self):
		return self.__isbn
	def setISBN(self, new_isbn):
		self.__isbn = new_isbn

	def readFile(self, filename):
		if (os.path.exists(filename)):
			file = open(filename, 'rb') # read as binary file
			if (file):
				# read all contents from file and save into data
				data = pickle.load(file)
				self.__name = data.getName()
				self.__author = data.getAuthor()
				self.__isbn = data.getISBN()
				file.close()

	def writeFile(self, filename):
		file = open(filename, 'wb') # write as binary file
		if (file):
			pickle.dump(self, file)
			file.close()

	def toString(self):
		return f'[Book Instance: {self.__name} - {self.__isbn}]'

# SubClass / Child Class / Derived class
class ActionBook(Book):
	def __init__(self, name, author, isbn):
		super().__init__(name, author, isbn, 'Action')

	def getCategory(self):
		return self._category

	# Invalid self.__name because private variable
	# def getMyName(self):
	# 	return self.__name







