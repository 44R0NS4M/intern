#str="hello world, hi world, hello world"

str=input("Enter String")
subs=input("Enter substring to check")

slen=len(str)
count=0
subslen=len(subs)

y=0 
x=0
while y<slen:
    if str[y] == " ":
        word=str[x:y]
        print(word)
        if word==subs:
            count+=1
        x=y+1
    elif y==slen-1:
        word=str[x:y+1]
        print(word)
        if word==subs:
            count+=1
    y+=1

print(count)




"""
x=0
for y in range(len(str)):
    if str[y] == " ":
        word=str[x:y]
        print(word)
        if word==subs:
            count+=1
        x=y+1
    elif y==slen-1:
        word=str[x:y+1]
        print(word)
        if word==subs:
            count+=1
        

print(count)
"""





"""
slen=len(str)
subslen=len(subs)
count=0

for inc in range(0,slen-1):
    inc=str.index(subs)
    print(inc)
    count+=1
    inc=inc+subslen
    str=str[inc:slen-1]

print(count)
"""






"""
slen=len(str)
count=0
subslen=len(subs)
for y in range(len(str)-1):
    if str[y:y+subslen] == subs:
        print(y)
        count+=1
        print(str[y:y+subslen])


print(count)
"""