def count_tribonacci_subarrays(n, arr):
    MOD = 10**9 + 7

    # Step 1: Tribonacci numbers generate karo (jitne 10^5 se chhote ho)
    trib_set = set()
    t0, t1, t2 = 0, 1, 1
    trib_set.update([t0, t1, t2])
    while True:
        t3 = t0 + t1 + t2
        if t3 > 1e5:
            break
        trib_set.add(t3)
        t0, t1, t2 = t1, t2, t3

    # Step 2: Array ke andar subarrays count karo jo sirf Tribonacci numbers se bane ho
    count = 0
    length = 0

    for num in arr:
        if num in trib_set:
            length += 1  # Tribonacci number mila
        else:
            # Agar pehle ek valid segment chal raha tha, to uska result add karo
            if length > 0:
                count = (count + (length * (length + 1)) // 2) % MOD
                length = 0  # Reset segment

    # Agar last me bhi ek valid segment bacha ho to use count karo
    if length > 0:
        count = (count + (length * (length + 1)) // 2) % MOD

    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    # First value N hai
    n = int(data[0])

    # Next N values array ke elements hain
    arr = list(map(int, data[1:n+1]))

    # Hamari function ko call karo
    result = count_tribonacci_subarrays(n, arr)
    
    # Final output print karo
    print(result)

if __name__ == "__main__":
    main()
