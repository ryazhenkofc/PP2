def gen(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = map(int, input().split())

for i in gen(a, b):
    print(i)