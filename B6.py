class Numbers:
        def __init__(self):
                self.cur=0
                self.next=1

        def __iter__(self):
                return self

        def __next__(self):
                self.next, self.cur = self.next+self.cur, self.next
                return self.cur

def main():
        fib=Numbers()

        while True:
                for i,_ in zip(mygenerator, range(10)):
                        print(i)

                yn=input("Continue ? : ")
                if yn!='Y' and yn!='y':
                        break

main()

                
