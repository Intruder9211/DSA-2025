import sys
input = sys.stdin.read

def countValidPartitions(E, N):
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + E[i]

    count = 0

    for length in range(1, (N // 2) + 1):
        len_alpha = length
        len_gamma = length
        len_beta = N - len_alpha - len_gamma

        if len_beta < 1:
            continue

        sum_alpha = prefix[len_alpha]
        sum_beta = prefix[len_alpha + len_beta] - prefix[len_alpha]
        sum_gamma = prefix[N] - prefix[N - len_gamma]

        if sum_alpha + sum_gamma > sum_beta:
            count += 1

    return count

if __name__ == "__main__":
    data = input().split()
    N = int(data[0])
    E = list(map(int, data[1:]))
    result = countValidPartitions(E, N)
    print(result)
