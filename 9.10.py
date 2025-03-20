from collections import Counter

def frequency(s):
    words = s.split()
    freq_dict = Counter(words)
    return sorted(freq_dict.items())

print(frequency("apple banana apple orange banana banana"))
