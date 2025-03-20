def generate_tuples(start, end):
    return [(x, x*2, x*3) for x in range(start, end+1)]

print(generate_tuples(1, 5))