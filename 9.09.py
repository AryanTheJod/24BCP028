def count_alpha_digits(s):
    alpha_count = sum(c.isalpha() for c in s)
    digit_count = sum(c.isdigit() for c in s)
    return alpha_count, digit_count

print(count_alpha_digits("Hello123"))
