class Menu:
		def __init__(self):
				self.mydict = {}

		def __setitem__(self, mykey, myval):
				if mykey in self.mydict.keys():
						raise Exception

				self.mydict[mykey]=myval

		def __iter__(self):
				return iter(self.mydict.items())

m=Menu()
m['Idly']=10
m['Vada']=20

for item, cost in m:
		print(item,cost)
