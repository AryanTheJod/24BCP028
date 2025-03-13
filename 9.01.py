def count_lower_upper(a):
    i=0
    j=0
    for ch in a:
        if ch >= "A" and ch <= "Z":
            i+=1
        elif ch >= "a" and ch <= "z":
            j+=1
    print("i=",i,"j=",j)
    d={"A":i,
       "a":j}
    print(d)
count_lower_upper(a=str(input("Enter a string:")))

    
        
        
        
        
        
