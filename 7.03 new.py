def dict3():
    empdata={(1,28):50000,(1,63):25000,(2,72):30000}
    deptdata={}
    for k,v in empdata.items():
        print(k[0],k[1],v)
        if k[0] not in deptdata:
            deptdata[k[0]]={"Max":v,"Min":v,"total":v}
        else:
            if v > deptdata[k[0]]["Max"]:
                deptdata[k[0]]["Max"]=v
            elif v< deptdata[k[0]]["Min"]:
                deptdata[k[0]]["Min"]=v
            deptdata[k[0]]["total"]+=v
    print(deptdata)

dict3()
