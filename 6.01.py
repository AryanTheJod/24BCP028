nob=0
nog=0
name=(('Aryan','atg','forreal'),'bruh','dotcare',('jj','kk'))
for el in name:
    
    if isinstance(el,tuple):
        i=0
        while i < len(el):
            i+=1
            nob+=1
    else:
        nog+=1
print("numer of bois =",nob)
print("number of girls =",nog)
