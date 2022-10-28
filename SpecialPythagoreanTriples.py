from asyncio import run

async def iteration(aMin, bMin, cMin, aMax, bMax, cMax):
    for c in range(cMin, cMax):
        for b in range(bMin, bMax):
            for a in range(aMin, aMax):
                if (a**2)+(b**2)==(c**2) and a+b+c==1000:
                    print(a, b, c)
                    break

for i in range(100, 10000, 100):
    run(iteration(i-100, i-100, i-100, i, i, i))
