from collections import Counter

def user_logic(n1, flowers, n2, herbs):
    """
    Determines which flowers Lily should note based on their frequency compared to herbs.
    """
    flower_counts = Counter(flowers)
    herb_counts = Counter(herbs)

    result = []
    for flower in flowers:
        if flower_counts[flower] > herb_counts.get(flower, 0):
            result.append(flower)
    return result if result else [-1]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n1 = int(data[0])
    flowers = list(map(int, data[1:n1 + 1]))
    n2 = int(data[n1 + 1])
    herbs = list(map(int, data[n1 + 2:n1 + 2 + n2]))

    result = user_logic(n1, flowers, n2, herbs)

    if result == [-1]:
        print(-1)
    else:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
