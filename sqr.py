import random
i=0
lst=[]
for i in random.randint(1,100):
    lst=lst+[i]

i=0
lst1=[]
while i < len(lst):
    lst1=lst1+(lst[i])**2

for ele in lst1:
    print(ele)
    
    
