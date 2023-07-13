

def vowchk(str):
    vowels="aeiou"
    for i in str:
        for j in vowels:
            if i==j:
                return 1
    
    
    
    
    
    """
    for i in str:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            print(i)
    """ 
    

str=input("Enter a string ")
vowchk(str)