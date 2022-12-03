import string

file = open('input')

score = 0
while True:
    try:
        letter = set.intersection(*(
            set(next(file).strip()) for _ in range(3)
        ))
        score += string.ascii_letters.index(list(letter)[0]) + 1
    except RuntimeError:
        print(score)
        break