
class bank:

    def __init__(self):
        self.master={}



    def menu(self):
        self.i=1
        ch=0
        while (ch!=4):
            ch=int(input("Enter your option\n1. Create\n2. Withdraw\n3. Deposit\n4. Exit\n"))
            match ch:
                case 1:    
                    self.creat(self.i)
                    self.i=self.i+1
                case 2:
                    self.withd()
                case 3:
                    self.depos()

        print(self.master)

    def creat(self,i):
        acc={}
        print("Enter Account details ")
        name=input("Enter Name\n")
        accid=1000+self.i
        bal=int(input("Enter Balance Amount (Minimum Rs.1000)\n"))
        if bal>1000:
            acc['name']=name
            #acc['accid']=accid
            acc['bal']=bal

            print(i)
        else:
            print("Balance must be over Rs.1000")

        print(acc)
        self.master[accid]=acc
        return self.i

    def withd(self):
        log=int(input("Enter account ID \n"))
        if log in self.master:
            acc=self.master[log].copy()
            wtd=int(input("Enter withdrawal amount \n"))
            acc['bal']-=wtd
            if acc['bal']>1000:
                self.master[log]=acc.copy()
            else:
                print("Balance must be over Rs.1000")

                print(acc)
        else:
            print("Cannot find ",log)

    def depos(self):
        log=int(input("Enter account ID\n"))
        
        acc=self.master[log]
        
        if log in self.master:
            acc=self.master[log].copy()
            dep=int(input("Enter deposit amount \n"))
            acc['bal']+=dep
            if acc['bal']>1000:
                self.master[log]=acc.copy()
            else:
                print("Balance must be over Rs.1000")
        else:
            print("Cannot find ",log)
            print(acc)
    

i=0
b=[]
while i!=1:
    b[i]=bank()
    b[i].menu()
