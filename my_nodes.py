class UnidirectionalNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __lt__(self, other):
        return str(self.data) < str(other.data)
    def __gt__(self, other):
        return str(self.data) > str(other.data)
    def __eq__(self, other):
        return str(self.data) == str(other.data)

class BidirectionalNode (UnidirectionalNode):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None