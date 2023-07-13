import psycopg2
conn=psycopg2.connect(database="invman",host="localhost",user="postgres",password="admin",port="5432")
cursor=conn.cursor()


ch=1
i=100
while ch == 1:
    id = i+1
    name=input("Enter product name")
    cat=input("Enter category")
    amt=int(input("Enter amount available"))
    price=int(input("Enter price"))
    cursor.execute(f"insert into prod values({id},'{name}','{cat}',{amt},{price})")
    conn.commit()
    cursor.execute("select * from prod")
    print(cursor.fetchall())
conn.close()