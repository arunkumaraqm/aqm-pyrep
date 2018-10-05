class Numbers:
        def __init__(self):
                self.cur=0
                self.next=1

        def __iter__(self):
                return self

        def __next__(self):
                temp=self.next
                self.next+=self.cur
                self.cur=temp
                return self.cur

fib=Numbers()
limit=30

for i in fib:
        print(i)
        if i>limit:
                break
                
