
def convert(s):
    return " ".join(sorted(set(s.split())))

print(convert("banana apple orange banana apple"))