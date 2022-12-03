import string

letters = [
    set(line[:len(line) // 2]) & set(line[len(line) // 2:])
    for line in open('input')
]

print(
    sum(
        string.ascii_letters.index(list(letter)[0]) + 1
        for letter in letters
    )
)