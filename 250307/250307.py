def closestPrimes(left: int, right: int) -> list[int]:
    #Sieve of Eratosthenes
    findPrimes = [True] * (right + 1)
    findPrimes[0] = findPrimes[1] = False
    for i in range(2, int(right**0.5) +1):
        if findPrimes[i]:
            findPrimes[i*i: right + 1 : i] = [False] * len(range(i*i, right + 1, i))
    primes = [i for i, p in enumerate(findPrimes) if p]
    
    min = [-1,-1,10000000]
    for i, v in enumerate(primes):
        if primes[i] >= left and i + 1 < len(primes):
            if min[2] > primes[i+1] - primes[i]:
                min = [primes[i], primes[i+1], primes[i+1] - primes[i]]
    return [min[0], min[1]]

        


closestPrimes(1,20)
