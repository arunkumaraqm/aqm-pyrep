class Menu:
        def __init__(self):
                self.mydict = {}

        def __setitem__(self, mykey, myval):
                if mykey in self.mydict.keys():
                        raise Exception
                
                self.mydict[mykey]=myval

        def __iter__(self):
                self.mykeys = self.mydict.__iter__()
                return self

        def __next__(self):
                curkey = self.mykeys.__next__()
                curval = self.mydict[curkey]
                return curkey+'\t\t'+str(curval)


m=Menu()
m['Idly']=10
m['Vada']=20
for i in m:
        print(i)
