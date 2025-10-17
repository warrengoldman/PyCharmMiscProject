from doubly_linked_list import DoublyLinkedList
from singly_linked_list import SinglyLinkedList

def main():
    test_single_linked_list()
    test_double_linked_list_sort()
    # test_double_linked_list_swap()
    # test_double_linked_list()
    # test_double_linked_list_objec
#    test_single_linked_list_traverse()
    #test_single_linked_list_getat()
    #test_single_linked_list_reverse()
    #test_double_linked_list_reverse()

def test_double_linked_list_object():
    ll = DoublyLinkedList()
    one = ll.create_node({"name": "James", "email": "james@gmail.com" })
    ll.append(one)
    two = ll.create_node("2")
    ll.append(two)
    one_dot_one = ll.create_node("1.1")
    ll.insert_at(1, one_dot_one)
    zero_dot_one = ll.create_node("0.1")
    ll.insert_at(0, zero_dot_one)
    zero_dot_zero_one = ll.create_node("0.01")
    ll.insert_at_head(zero_dot_zero_one)
#    ll.sort()
    print(ll)

def test_double_linked_list_sort():
    ll = DoublyLinkedList()
    four = ll.create_node("4")
    ll.append(four)
    two = ll.create_node("2")
    ll.append(two)
    one = ll.create_node("1")
    ll.append(one)
    three = ll.create_node("3")
    ll.append(three)
    print(ll)
    ll.sort()
    print(ll)

def test_double_linked_list_swap():
    ll = DoublyLinkedList()
    four = ll.create_node("4")
    ll.append(four)
    two = ll.create_node("2")
    ll.append(two)
    one = ll.create_node("1")
    ll.append(one)
    three = ll.create_node("3")
    ll.append(three)
    five = ll.create_node("5")
    ll.append(five)
    ll.swap(two, three)
    print(ll)

def test_double_linked_list_reverse():
    ll = DoublyLinkedList()
    four = ll.create_node("4")
    ll.append(four)
    two = ll.create_node("2")
    ll.append(two)
    one = ll.create_node("1")
    ll.append(one)
    three = ll.create_node("3")
    ll.append(three)
    five = ll.create_node("5")
    ll.append(five)
    ll.reverse()
    print(ll)

def test_double_linked_list():
    ll = DoublyLinkedList()
    one = ll.create_node("1")
    ll.append(one)
    two = ll.create_node("2")
    ll.append(two)
    one_dot_one = ll.create_node("1.1")
    ll.insert_at(3, one_dot_one)
    zero_dot_one = ll.create_node("0.1")
    ll.insert_at(0, zero_dot_one)
    zero_dot_zero_one = ll.create_node("0.01")
    ll.insert_at_head(zero_dot_zero_one)

    ll.delete_at(5)

    print(ll)

def test_single_linked_list():
    linked_list: SinglyLinkedList = SinglyLinkedList()
    one = linked_list.create_node("1")
    linked_list.append(one)
    linked_list.append(linked_list.create_node("2"))
    linked_list.append(linked_list.create_node("4"))
    head = linked_list.create_node("0")
    linked_list.insert_at(0, head)
    three = linked_list.create_node("3")
    linked_list.insert_at(3, three)
    linked_list.insert_at(5, linked_list.create_node("5"))
    tail = linked_list.create_node("6")
    linked_list.insert_at(8, tail)
    linked_list.append(three)
    linked_list.insert_at(0, three)

    linked_list.swap(three, head)
    linked_list.sort()
    print(linked_list)

def test_single_linked_list_getat():
    linked_list: SinglyLinkedList = SinglyLinkedList()
    one = linked_list.create_node("1")
    linked_list.append(one)
    linked_list.append(linked_list.create_node("2"))
    linked_list.append(linked_list.create_node("4"))
    node_two = linked_list.get_at(1)
    print(f"Node at index 1: {node_two}")

def test_single_linked_list_reverse():
    linked_list: SinglyLinkedList = SinglyLinkedList()
    one = linked_list.create_node("1")
    linked_list.append(one)
    linked_list.reverse()
    print(linked_list)
    linked_list.append(linked_list.create_node("2"))
    linked_list.reverse()
    print(linked_list)
    linked_list.append(linked_list.create_node("4"))
    print(linked_list)
    linked_list.reverse()
    print(linked_list)


def test_double_linked_list_reverse_simple():
    linked_list: DoublyLinkedList = DoublyLinkedList()
    one = linked_list.create_node("1")
    linked_list.append(one)
    linked_list.append(linked_list.create_node("2"))
    linked_list.append(linked_list.create_node("4"))
    print(linked_list)
    linked_list.reverse()
    print(linked_list)


def test_single_linked_list_traverse():
    linked_list: SinglyLinkedList = SinglyLinkedList()
    one = linked_list.create_node("1")
    linked_list.append(one)
    linked_list.append(linked_list.create_node("2"))
    linked_list.append(linked_list.create_node("4"))

    # while linked_list.hasNext():
    #     print(linked_list.next().data)

if __name__ == '__main__':
    main()