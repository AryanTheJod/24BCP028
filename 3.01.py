x = str(input("Enter a string :"))
a = x.count("a") + x.count("A")
e = x.count("e") + x.count("E")
i = x.count("i") + x.count("I")
o = x.count("o") + x.count("O")
u = x.count("u") + x.count("U")
tot = a + e + i + o + u
print("There are ", tot, " vowels in the string.")
