master=[]



def menu():
    i=1
    ch=0
    while (ch!=4):
        ch=int(input("Enter your option\n1. Create\n2. Withdraw\n3. Deposit\n4. Exit\n"))
        match ch:
            case 1:
                
                creat(i)
                print(i)
                i=i+1
            case 2:
                withd()
            case 3:
                depos()

    print(master)

def creat(i):
    acc=[]
    print("Enter Account details ")
    name=input("Enter Name")
    accid=1000+i
    bal=int(input("Enter Balance Amount (Minimum Rs.1000)"))
    if bal>1000:
        acc.append(name)
        acc.append(accid)
        acc.append(bal)
        
        print(i)
    else:
        print("Balance must be over Rs.1000")

    print(acc)
    master.append(acc)
    return i

def withd():
    log=int(input("Enter account ID "))
    for i in range(0,len(master)):
        acc=master[i]
        for j in acc:
            if log==j:
                wtd=int(input("Enter withdrawal amount "))
                acc[2]-=wtd
                if acc[2]>1000:
                    master[i]=acc
                else:
                    print("Balance must be over Rs.1000")
                
                print(acc)

def depos():
    log=int(input("Enter account ID"))
    for i in range(0,len(master)):
        acc=master[i]
        for j in acc:
            if log==j:
                dep=int(input("Enter deposit amount "))
                acc[2]+=dep
                if acc[2]>1000:
                    master[i]=acc
                else:
                    print("Balance must be over Rs.1000")
                
                print(acc)

menu()
