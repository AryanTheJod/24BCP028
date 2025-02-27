def aorb():
    s1={"aryan","amin","bruh","bhai"}
    s2=set()
    s3=set()
    for ele in s1:
        if ele.startswith("a"):
            s2.add(ele)
        elif ele.startswith("b"):
            s3.add(ele)
    print(s2)
    print(s3)
aorb()

