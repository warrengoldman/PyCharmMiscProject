from singly_linked_list import SinglyLinkedList, UnidirectionalNode

class BidirectionalNode (UnidirectionalNode):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None
    def __str__(self):
        prev_data = self.previous.data if self.previous else "None"
        return f'{prev_data} <= {super().__str__()}'

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
    def append(self, data):
        current = super().append(data)
        if current is not None:
            if self.head != current:
                data.previous = current
            elif self.head != data:
                data.previous = current

    def reverse(self):
        super().reverse()
        self.head.previous = None

    def insert_at(self, idx, data):
        previous = super().insert_at(idx, data)
        if previous is not None:
            data.previous = previous
            if data.next is not None:
                data.next.previous = data
        elif self.head == data:
            data.next.previous = data

    def set_prev_node(self, new_node, prev_node):
        new_node.previous = prev_node

    def create_node(self, data):
        return BidirectionalNode(data)

    def delete_element(self, data):
        if data is None:
            return
        super().delete_element(data)
        if data.previous is not None:
            data.previous.next = data.next
        if data.next is not None:
           data.next.previous = data.previous

    def sort(self):
        super().sort()
        self.head.previous = None

    def set_node_order(self, previous_node, next_node):
        super().set_node_order(previous_node, next_node)
        next_node.previous = previous_node