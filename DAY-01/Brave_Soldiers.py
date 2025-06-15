def count_brave_soldiers(N):
    # Ek list banate hain jisme assume karte hain ke sabhi number prime hain
    # Initially, maan lete hain sabhi number 0 se N tak prime hain (True)
    is_prime = [True] * (N + 1)

    # 0 aur 1 kabhi bhi prime nahi hote, toh unhe False kar dete hain
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes algorithm use karte hain taaki efficiently prime number find kar sakein
    for i in range(2, int(N**0.5) + 1):
        # Agar current number i prime hai
        if is_prime[i]:
            # Toh uske sabhi multiples ko prime nahi maan sakte, isliye unhe False kar do
            for j in range(i*i, N + 1, i):
                is_prime[j] = False

    # Ab is_prime list mein jaha jaha True hai, woh number prime hai
    # Total True values ka count hi brave soldiers ka count hai
    brave_count = sum(is_prime)
    return brave_count

# Input lete hain user se
N = int(input())

# Function call karke brave soldiers ka count print karte hain
print(count_brave_soldiers(N))
