from asyncio import run

numbers = list()

limit = 100

async def iteration(minIteration, maxIteration, limit):
    primes = list()
    for i in range(minIteration, maxIteration):
        for j in range(2, limit):
            if i % j == 0 and j != i:
                break
            continue
        else:
            primes.append(i)
    return primes
    
previous = 0
results = list()
plus = list()
for i in range(0, 999999, 100):
    results.append(run(iteration(previous, i, 500)))
    previous = i
    
for i in results:
    for k in i:
        plus.append(k)
    
print(plus[10001])
