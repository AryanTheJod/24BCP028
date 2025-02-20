def dict3():
    empdata={(1,28):50000,(1,63):25000,(2,72):30000}
    deptdata={}
    for k,v in empdata.items():
        print(k[0],k[1],v)
    d1={1:{"Max":2,"Min":3,"Sum":4}}
    for k,v in empdata.items():
        if k[0]==1:
            d1[0][0]==max(empdata)
            d1[0][1]==min(empdata)
            d1[0][2]==sum(empdata)
    for k,v in d1.items():
        print (k,v)
dict3()
