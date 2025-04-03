f = open("C:\\Users\\24BCP028\\Desktop\\Marks 2.csv")

'''while content:
    content=f.readline()
    i+=1
    print(content)'''
All_data=f.readlines()
Filter=[lines.strip().split(",") for lines in All_data]
Empty_dictionary={}
column=len(Filter[0])
for i in range(column):
    Empty_dictionary[Filter[0][i]=[lines[i] for lines in Filter[1:]]]
f.close
print(Empty_dictionary)
