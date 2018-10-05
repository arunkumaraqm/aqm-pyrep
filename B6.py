class Numbers:
        def __init__(self):
                self.cur=0
                self.next=1

        def __iter__(self):
                return self

        def __next__(self):
                self.next, self.cur = self.next+self.cur, self.next
                return self.cur

fib=Numbers()
limit=31

for i in fib:
        print(i)
        if i>limit:
                break
                
