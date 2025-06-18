def can_partition_chocolates(n, chocolates):
    total = sum(chocolates)

    # Agar total odd hai to divide possible hi nahi
    if total % 2 != 0:
        return "NO"

    target = total // 2

    # DP array for subset sum
    dp = [False] * (target + 1)
    dp[0] = True  # 0 sum always possible

    for choco in chocolates:
        for j in range(target, choco - 1, -1):
            dp[j] = dp[j] or dp[j - choco]

    return "YES" if dp[target] else "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    chocolates = list(map(int, data[1:1+n]))

    result = can_partition_chocolates(n, chocolates)
    print(result)

if __name__ == "__main__":
    main()
