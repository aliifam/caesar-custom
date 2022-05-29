class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_last(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        new_node = Node(value)
        head = self.head
        while head.next is not None:
            head = head.next
        head.next = new_node

    def as_array(self):
        values_as_array = []
        head = self.head
        while head is not None:
            values_as_array.append(head.value)
            if head.next is None:
                break
            head = head.next
        return values_as_array
