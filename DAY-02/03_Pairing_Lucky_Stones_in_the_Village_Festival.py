import sys

def find_lucky_stone_pairs(p, n, m, stones):
    # Step 1: Filter stones divisible by either N or M
    lucky_stones = []
    for stone in stones:
        if stone % n == 0 or stone % m == 0:
            lucky_stones.append(stone)

    # Step 2: Count all unique pairs (i, j) where i < j
    count = 0
    for i in range(len(lucky_stones)):
        for j in range(i + 1, len(lucky_stones)):
            count += 1

    return count

def main():
    input = sys.stdin.read
    data = input().strip().split()

    p = int(data[0])  # Number of stones
    n = int(data[1])  # Special number N
    m = int(data[2])  # Special number M
    stones = list(map(int, data[3:]))  # List of stones

    # Call user logic function and print the output
    result = find_lucky_stone_pairs(p, n, m, stones)
    print(result)

if __name__ == "__main__":
    main()
