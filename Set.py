import math

class Set:
	def __init__(self, defList = []):
		self.list = defList

	def contains(self, elem):
		for i in self.list:
			if i == elem:
				return True
				break
		return False

	def Add(self, elem):
		if not self.list.__contains__(elem):
			self.list.append(elem)

	def Remove(self, elem):
		if elem in self.list:
			self.list.remove(elem)

	def Size(self):
		return len(self.list)

	def __and__(self, SetB):
		newList = []
		for i in SetB.list:
			for  j in self.list:
				if i == j and not newList.__contains__(j):
					newList.append(j)
		newSet = Set(newList)
		return newSet

	def __or__(self, SetB):
		newList = []
		for i in SetB.list:
			newList.append(i)
		for j in self.list:
			if not newList.__contains__(j):
				newList.append(j)
		newSet = Set(newList)
		return newSet

	def __sub__(self, SetB):
		newList = []
		for i in self.list:
			if not SetB.list.__contains__(i):
				newList.append(i)
		newSet = Set(newList)
		return newSet

	def __iter__(self):
		for i in self.list:
			yield i
