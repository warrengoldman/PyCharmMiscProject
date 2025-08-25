from singly_linked_list import SinglyLinkedList
class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
    def append(self, data):
        current = super().append(data)
        if self.head != current:
            data.previous = current
        elif self.head != data:
            data.previous = current

    def insert_at(self, idx, data):
        previous = super().insert_at(idx, data)
        if previous is not None:
            data.previous = previous
            if data.next is not None:
                data.next.previous = data
        elif self.head == data:
            data.next.previous = data

    def delete_element(self, data):
        if data is None:
            return
        super().delete_element(data)
        if data.previous is not None:
            data.previous.next = data.next
        if data.next is not None:
           data.next.previous = data.previous

    def sort(self):
        last_element = super().sort()
        self.head.previous = None
        last_element.next = None

    def set_node_order(self, previous_node, next_node):
        super().set_node_order(previous_node, next_node)
        next_node.previous = previous_node