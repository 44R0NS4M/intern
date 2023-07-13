from datetime import date
import psycopg2
conn=psycopg2.connect(database="invman",host="localhost",user="postgres",password="admin",port="5432")
cursor=conn.cursor()

cursor.execute("select * from prod")
inv=cursor.fetchall()

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
                updinv(inv)
            case 5:
                report()


    print(inv)

def addinv(i):
    
    id=i+100
    name=input("Enter product ")
    cat=input("Enter product category ")
    amt=int(input("Enter quantity "))
    price=int(input("Enter price of product "))
    print(i)
    
    cursor.execute(f"insert into prod values({id},'{name}','{cat}',{amt},{price})")
    conn.commit()
    cursor.execute("select * from prod")
    
    inv=cursor.fetchall()
    print(inv)
    conn.close()
    
    
    return i

def search():
    
    skey=input("Enter product category ")
    
    '''    
    for prod in inv:
        if cat == skey:
            print(prod)
        
        else:
            print("Product is not present")
    '''

    prod=[i for i in inv if i[2] ==skey ]
    print(prod)
        
        
    




def disp():
    print(inv)



def updinv(inv):
    
    skey=input("Enter product category ")
    for prod in inv:
        if prod[2]==skey:
            print(prod)
            pname=input("Enter product ")        
            if prod[1] == pname:
                qua=int(input("Enter new quantity "))
                if prod[3]>qua:

                    sold=prod[3]-qua
                    sale(prod,sold,prod[0])
                    
                cursor.execute(f"update prod set amt = {qua} where name = '{pname}'")
                conn.commit()
                cursor.execute("select * from prod")
                inv=cursor.fetchall()

            print(prod)
        else:
            print("Product is not present")
    

            
def sale(prod,sold,pid):
    cursor.execute("select * from psale")
    psale=cursor.fetchall()
    id=pid+1000
    cursor.execute("select id from cust")
    cid=cursor.fetchall()
    tdate=date.today()
    revenue=prod[4]*sold
    #name=prod[2]
    #psale['sold']=sold
    #psale['revenue']=revenue
    #sales.append(psale)
    cursor.execute(f"insert into psale values('{tdate}','{pid}',{sold},{revenue},{cid[0][0]})")
    conn.commit()
    
    print(psale)

def report():
    print(inv)
    print(sales)
menu()