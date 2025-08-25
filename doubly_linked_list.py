from singly_linked_list import LinkedList
class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    def append(self, data):
        current = super().append(data)
        data.previous = current
