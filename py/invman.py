inv=[]

sales=[]

def menu():
    i=1
    ch=0
    while (ch!=6):
        ch=int(input("Enter your option\n1. Add\n2. Search\n3. Display\n4. Update\n5. Reports\n6. Exit\n"))
        match ch:
            case 1:
                addinv(i)
                print(i)
                i=i+1
            case 2:
                search()
            case 3:
                disp()
            case 4:
                updinv()
            case 5:
                report()


    print(inv)

def addinv(i):
    prod={}
    prod['name']=input("Enter product ")
    prod['cat']=input("Enter product category ")
    prod['amt']=int(input("Enter quantity "))
    prod['price']=int(input("Enter price of product "))
    print(i)
    print(prod)
    inv.append(prod)
    return i

def search():
    
    skey=input("Enter product category ")
    
    '''    
    for prod in inv:
        if prod['cat'] == skey:
            print(prod)
        
        else:
            print("Product is not present")
    '''

    prod=[i for i in inv if i['cat'] ==skey ]
    print(prod)
        
        
    




def disp():
    print(inv)

def updinv():
    
    skey=input("Enter product category ")
    for prod in inv:
        if prod['cat'] == skey:
            print(prod)
            pname=input("Enter product ")        
            if prod['name'] == pname:
                qua=int(input("Enter new quantity "))
                if prod['amt']>qua:
                    sold=prod['amt']-qua
                    sale(prod,sold)
                    prod['amt']=qua
                else:
                    prod['amt']=qua

            print(prod)
        else:
            print("Product is not present")

def sale(prod,sold):
    psale={}
    
    revenue=prod['price']*sold
    psale['name']=prod['name']
    psale['sold']=sold
    psale['revenue']=revenue
    sales.append(psale)

def report():
    print(inv)
    print(sales)
menu()