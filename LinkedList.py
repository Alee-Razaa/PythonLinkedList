class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def show_elements(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_element(self, index):
        current = self.head
        for i in range(index):
            if not current:
                return None
            current = current.next
        return current.data if current else None

    def get_index(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return "Value not found"

    def update_element(self, previous_value, new_value):
        current = self.head
        while current:
            if current.data == previous_value:
                current.data = new_value
                return
            current = current.next

    def delete_element(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

        print(f"Node with value {value} not found in the list")

    def delete_at_first(self):
        if self.head:
            self.head = self.head.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def add_after_element(self, target_value, new_value):
        current = self.head
        while current:
            if current.data == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Element with value {target_value} not found in the list")

    def add_before_element(self, target_value, new_value):
        if not self.head:
            print("The list is empty")
            return

        if self.head.data == target_value:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.data == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        print(f"Element with value {target_value} not found in the list")

    def add_at_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_at_last(self, value):
        self.append(value)

    def delete_at_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def search(self, target):
        current = self.head
        position = 0
        while current:
            if current.data == target:
                return f"Found at position {position}"
            current = current.next
            position += 1
        return f"{target} is not in the List"

    def count(self):
        return self.length()

    def delete_first_occurrence_of_element(self, target):
        self.delete_element(target)

    def delete_last_occurrence_of_element(self, target):
        if not self.head:
            return

        last_occurrence = None
        prev = None
        current = self.head

        while current:
            if current.data == target:
                last_occurrence = prev
            prev = current
            current = current.next

        if last_occurrence:
            if last_occurrence == self.head:
                self.head = self.head.next
            else:
                last_occurrence.next = last_occurrence.next.next
        else:
            print(f"{target} is not in the list")

    def delete_all_occurrences_of_element(self, target):
        while self.head and self.head.data == target:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.data == target:
                current.next = current.next.next
            else:
                current = current.next

    def middle_element(self):
        if not self.head:
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def nth_element(self, n):
        current = self.head
        for _ in range(n):
            if not current:
                return f"{n}th element does not exist"
            current = current.next
        return current.data if current else None

    def rotate(self):
        if not self.head or not self.head.next:
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = self.head
        self.head = self.head.next
        last.next.next = None