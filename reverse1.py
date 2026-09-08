s = "he is palying football"
b = s.split()

for i in range(len(b)):
    if i % 2 == 0:
        b[i] = b[i][::-1]

print(' '.join(b))

