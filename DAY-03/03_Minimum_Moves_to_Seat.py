def calculate_min_moves(seats, students):
    """
    Calculate the minimum number of moves required to assign each student to a seat.
    Parameters:
        seats (list): List of seat positions
        students (list): List of student positions
    Returns:
        int: Minimum number of moves
    """
    seats.sort()
    students.sort()
    
    total_moves = 0
    for i in range(len(seats)):
        total_moves += abs(seats[i] - students[i])
    
    return total_moves


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    seats = list(map(int, data[1:n+1]))
    students = list(map(int, data[n+1:2*n+1]))
    
    result = calculate_min_moves(seats, students)
    print(result)  # Fixed for Python 3

if __name__ == "__main__":
    main()
