class UnidirectionalNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __lt__(self, other):
        return str(self.data) < str(other.data)
    def __gt__(self, other):
        return str(self.data) > str(other.data)
    def __eq__(self, other):
        if other is None:
            return False
        return str(self.data) == str(other.data)
    def __str__(self):
        next_data = self.next.data if self.next else "None"
        return f'{self.data} => {next_data}'

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def get_at(self, idx):
        element_ctr = 0
        if idx >= 0:
            current = self.head
            while idx > element_ctr:
                element_ctr += 1
                if current.next is None:
                    return None
                current = current.next
            return current
        return None

    def get_index(self, data):
        current = self.head
        current_index = 0
        while current:
            if current == data:
                return current_index
            current_index += 1
            current = current.next
        return -1

    def delete_element(self, data):
        current_element = self.head
        if current_element == data:
            self.head = current_element.next
        else:
            while True:
                if current_element is None:
                    previous_element = None
                    break
                if current_element.next == data:
                    previous_element = current_element
                    break
                current_element = current_element.next
            if previous_element is not None:
                previous_element.next = None if current_element.next is None else current_element.next.next

    def delete_at(self, idx):
        current_element = self.head
        current_idx = 0
        while True:
            if current_idx == idx:
                self.delete_element(current_element)
                break
            if current_element is None:
                break
            current_element = current_element.next
            current_idx += 1

    def is_in_list(self, data):
        current_element = self.head
        while True:
            if current_element == data:
                return True
            if current_element is None or current_element.next is None:
                return False
            current_element = current_element.next

    def insert_at(self, idx, data):
        if self.is_in_list(data):
            return None
        current_element = self.head
        previous_element = None
        current_idx = 0
        while True:
            if current_idx == idx:
                if previous_element is not None:
                    previous_element.next = data
                else:
                    self.head = data
                data.next = current_element
                break
            if current_element.next is None:
                data.next = None
                current_element.next = data
                break
            previous_element = current_element
            current_element = current_element.next
            current_idx += 1
        return previous_element

    def insert_at_head(self, data):
        return self.insert_at(0, data)

    def append(self, data):
        if self.is_in_list(data):
            return None
        if self.head is None:
            self.head = data
            return data
        else:
            current = self.head
            while current.next:
                if current == data:
                    return None
                current = current.next
            current.next = data
            return current

    def swap(self, element1, element2):
        element1_index = self.get_index(element1)
        element2_index = self.get_index(element2)
        self.delete_element(element1)
        self.delete_element(element2)
        if element1_index < element2_index:
            self.insert_at(element1_index, element2)
            self.insert_at(element2_index, element1)
        else:
            self.insert_at(element2_index, element1)
            self.insert_at(element1_index, element2)

    def reverse(self):
        node = self.head
        next_node = None
        while node.next is not None:
            new_node = self.create_node(node.data)
            new_node.next = next_node
            node = node.next
            self.set_prev_node(new_node, node)
            next_node = new_node
        new_node = self.create_node(node.data)
        new_node.next = next_node
        self.head = new_node
        self.set_prev_node(self.head, None)

    def set_prev_node(self, new_node, prev_node):
        pass

    def create_node(self, data):
        return UnidirectionalNode(data)

    def sort(self):
        if self.head is None or self.head.next is None:
            return
        current = self.head
        sort_complete = False
        while not sort_complete:
            sort_complete = True
            while current and current.next:
                if current > current.next:
                    sort_complete = False
                    temp = current.next
                    self.swap(current, current.next)
                    current = self.head
                current = current.next
            current = self.head

    def get_list_str(self, str_list, data):
        if data is not None:
            str_list.append(str(data))
        if data and data.next is not None:
            self.get_list_str(str_list, data.next)
        return str_list

    def __str__(self):
        return str(self.get_list_str([], self.head))

    def set_node_order(self, previous_node, next_node):
        previous_node.next = next_node