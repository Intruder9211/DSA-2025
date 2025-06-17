def find_largest_number(arr):
    # Sort the array to get the two smallest numbers
    arr.sort()
    first_min = arr[0]
    second_min = arr[1]

    # Form two possible numbers by combining the digits
    num1 = int(str(first_min) + str(second_min))
    num2 = int(str(second_min) + str(first_min))

    # Return the maximum of the two
    return max(num1, num2)

if __name__ == '__main__':
    n = int(raw_input())  # Use input() instead of raw_input() in Python 3
    arr = list(map(int, raw_input().split()))
    result = find_largest_number(arr)
    print result  # Use print(result) in Python 3
