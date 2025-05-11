vowels = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5,
}

text = input()

total = sum([vowels[ch] for ch in text if ch in vowels])
print(total)
