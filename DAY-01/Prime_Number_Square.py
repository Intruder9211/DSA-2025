# Enter your code here. Read input from STDIN. Print output to STDOUT
def generate_primes(limit):
    # Sieve of Eratosthenes se prime numbers banate hain
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

# Input lena
N = int(input())

# 1300000 tak prime generate karna safe hai (100000th prime tak)
primes = generate_primes(1300000)

# 1-based indexing, isliye N-1
nth_prime = primes[N - 1]

# Output: us prime ka square
print(nth_prime * nth_prime)
                            
