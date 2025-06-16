class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

def user_logic(linked_list):
    
    if linked_list.head is None or linked_list.head.next is None:
        return 1

    
    values = []
    current = linked_list.head
    while current:
        values.append(current.data)
        current = current.next

    n = len(values)
    if n < 2:
        return 1

    # Determine initial direction
    if values[0] == values[1]:
        return 0
    increasing = values[0] < values[1]

    for i in range(1, n - 1):
        if values[i] == values[i + 1]:
            return 0
        # Expect opposite direction each time
        if increasing and values[i] < values[i + 1]:
            return 0
        if not increasing and values[i] > values[i + 1]:
            return 0
        increasing = not increasing

    return 1


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    values = map(int, data[1:])
    ll = LinkedList()
    for value in values:
        ll.push(value)
    result = user_logic(ll)
    print(result)

if __name__ == "__main__":
    main()
