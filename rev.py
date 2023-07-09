def rev():
    str=input()
    slen=len(str)
    for x in range(slen-1,-1,-1):
        print(str[x],end='')

print("Enter a number")
rev()