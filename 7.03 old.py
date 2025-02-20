def dict3():
    empdata={(1,28):50000,(1,63):25000,(2,72):30000}
    deptdata={}
    for k,v in empdata.items():
        if k[0] not in deptdata:
            deptdata[k[0]]=[v]
        else:
            deptdata[k[0]].append(v)
    for key in deptdata:
        deptdata[key]={"Max":max(deptdata[key]),"Min":min(deptdata[key]),"Total":sum(deptdata[key])}
    print(deptdata)
dict3()
