mkls=[]
tot=0
for i in range(0,2):
    stud=[]
    print("Enter mark of student ", i+1)
    for j in range(0,2):
        mk = int(input("Enter your mark "))
        stud.insert(i,mk)
    mkls.append(stud)
    
print(mkls)

for i in range(2):
    tot=sum(mkls[i])
    print("Marks of Student ",i,"= ",tot)
    avg=tot/5
    print("Average marks of student ",i,"= ",avg)    

print(mkls)
print(avg)

"""
mkls=[[] for i in range(5)]
tot=0
for i in range(0,5):
    print("Enter mark of student ", i+1)
    for j in range(0,5):
        mk = int(input("Enter your mark "))
        mkls[i].append(mk)
    
print(mkls)

for i in range(5):
    tot=sum(mkls[i])
    print("Marks of Student ",i,"= ",tot)
    avg=tot/5
    print("Average marks of student ",i,"= ",avg)    

print(mkls)
print(avg)
"""