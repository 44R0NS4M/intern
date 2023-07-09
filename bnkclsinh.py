
class bank:


    def menu(self):
        i=0
        acc=[]
        
        
        ch=0
        while (ch!=4):
            ch=int(input("Enter your option\n1. Create\n2. Withdraw\n3. Deposit\n4. Exit\n"))
            match ch:
                case 1:
                    
                    tp=int(input("Enter the type of account\n1. Savings\n2. Current"))
                    if tp == 1:
                        acc.append(savings(i+1))    
                        
                    else:
                        acc.append(current(i+1))    
                        
                    i+=1
                    print(acc)
                    for k in acc:
                        k.disp()
                case 2:
                    id=int(input("Enter your ID\n"))
                    for j in acc:
                        acctp=type(j)
                        print(acctp)
                        if acctp is savings:
                            if id == j.master['accid']:
                                print(j.master)
                                j.withd()
                        elif acctp is current:
                            if id == j.master['accid']:
                                print(j.master)
                                j.withd()
                    
                case 3:
                    id=int(input("Enter your ID\n"))
                    for j in acc:
                        
                        if id == j.master['accid']:
                            print(j.master)
                            j.depos()
                    

        #print(self.master)

class account:

    def __init__(self,i):
        #self.minim=minim
        self.i=i
        self.master={}
        
        print("Enter Account details ")
        name=input("Enter Name\n")
        accid=1000+self.i
        bal=int(input(f"Enter Balance Amount\n"))

        self.master['accid']=accid
        self.master['name']=name
        self.master['bal']=bal

            
        

        #print(acc)
        #self.master[accid]=acc
        print(self.master)
        
    def disp(self):
        print(self.master)

    def withd(self):
        
        
        acc=self.master.copy()
        wtd=int(input("Enter withdrawal amount \n"))
        acc['bal']-=wtd
        if acc['bal']>1000:
            self.master=acc.copy()
        else:
            print("Balance must be over Rs.1000")
            print(self.master)
        

    def depos(self):
        
        
        
        acc=self.master.copy()
        dep=int(input("Enter deposit amount \n"))
        acc['bal']+=dep
        if acc['bal']>1000:
            self.master=acc.copy()
        else:
            print("Balance must be over Rs.1000")
            print(self.master)
    

    
class savings(account):
    def __init__(self,i):
        self.i=i
        self.minim=1000
        super().__init__(self.i)


    def withd(self):
        
        
        acc=self.master.copy()
        wtd=int(input("Enter withdrawal amount \n"))
        acc['bal']-=wtd
        if acc['bal']>self.minim:
            self.master=acc.copy()
            print(self.master)
        else:
            print(f"Balance must be over Rs.{self.minim}")
            print(acc)
            print(self.master)
        

    

class current(account):
    def __init__(self,i):
        self.i=i
        self.minim=-500
        super().__init__(self.i)
        
    def withd(self):
        
        
        acc=self.master.copy()
        wtd=int(input("Enter withdrawal amount \n"))
        acc['bal']-=wtd
        if acc['bal']>self.minim:
            self.master=acc.copy()
            print(self.master)
        else:
            print(f"Balance must be over Rs.{self.minim}")
            print(acc)
            print(self.master)
        


b=bank()
b.menu()

