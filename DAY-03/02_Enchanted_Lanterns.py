def calculate_wish_value(brightness):
    n = len(brightness)
    max_from_right = [0] * n
    min_from_left = [0] * n

    # Fill max_from_right
    max_from_right[-1] = brightness[-1]
    for i in range(n - 2, -1, -1):
        max_from_right[i] = max(brightness[i], max_from_right[i + 1])

    # Fill min_from_left
    min_from_left[0] = brightness[0]
    for i in range(1, n):
        min_from_left[i] = min(brightness[i], min_from_left[i - 1])

    # Calculate total wish value
    total_wish_value = 0
    for i in range(n):
        total_wish_value += abs(max_from_right[i] - min_from_left[i])

    return total_wish_value

if __name__ == '__main__':
    import sys
    input_lines = sys.stdin.read().splitlines()  # Robustly read all input lines
    n = int(input_lines[0])
    brightness = list(map(int, input_lines[1].split()))
    print(calculate_wish_value(brightness))
