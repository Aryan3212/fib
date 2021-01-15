
# using a generator to get fibonacci
def fib():
    b = 0
    a = 1
    while True:
        res = b
        b,a=a,a+b
        yield res

fibonacci = fib()

for i in range(100):
    print(next(fibonacci))