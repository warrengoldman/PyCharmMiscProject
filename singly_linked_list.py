
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def get_at(self, idx):
        if idx >= 0:
            element_list = self.get_element_list()
            if idx < len(element_list):
                return self.get_element_list()[idx]
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
        element_list = self.get_element_list()
        list_idx = len(element_list) - 1
        idx = 0
        while list_idx >= 0:
            current_node = element_list[idx]
            self.delete_element(current_node)
            self.insert_at(0, current_node)
            list_idx -= 1
            idx += 1

    def sort(self):
        element_list = self.get_element_list()
        element_list.sort()
        list_length = len(element_list)
        for i in range(list_length):
            if i == list_length:
                element_list[i-1].next = None
                break
            elif i != 0:
                self.set_node_order(element_list[i-1], element_list[i])

        self.head = element_list[0]
        return element_list[list_length-1]

    def get_list_str(self, str_list, data):
        if data is not None:
            str_list.append(str(data))
        if data and data.next is not None:
            self.get_list_str(str_list, data.next)
        return str_list

    def __str__(self):
        return str(self.get_list_str([], self.head))

    def get_element_list(self):
        element_list = []
        element = self.head
        while True:
            if element_list.__contains__(element):
                break
            element_list.append(element)
            if element.next is None:
                break
            element = element.next
        return element_list

    def set_node_order(self, previous_node, next_node):
        previous_node.next = next_node