from collections import Counter

def validate_password(password):
    """
    Validates the password according to the conditions:
    1. All numbers must appear an even number of times.
    2. At least one number must appear exactly twice.
    Also determines the most frequent number (smallest if tie).
    """
    freq = Counter(password)

    all_even = all(count % 2 == 0 for count in freq.values())
    has_exactly_two = any(count == 2 for count in freq.values())

    # Find the most frequent number (choose smallest in case of tie)
    max_freq = max(freq.values())
    most_frequent = min(key for key in freq if freq[key] == max_freq)

    if all_even and has_exactly_two:
        return "VALID", most_frequent
    else:
        return "INVALID", most_frequent


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])  # First input is the integer N
    password = list(map(int, data[1:]))  # Remaining input is the password array

    # Call user logic function
    validation_result, most_frequent_element = validate_password(password)

    # Print the output
    print(validation_result)
    print(most_frequent_element)

if __name__ == "__main__":
    main()
