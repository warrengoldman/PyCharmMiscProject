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
    def __str__(self):
        next_data = self.next.data if self.next else "None"
        return f'{self.data} => {next_data}'

class BidirectionalNode (UnidirectionalNode):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None
    def __str__(self):
        prev_data = self.previous.data if self.previous else "None"
        return f'{prev_data} <= {super().__str__()}'