from doubly_linked_list import DoublyLinkedList
from singly_linked_list import SinglyLinkedList
from my_nodes import UnidirectionalNode, BidirectionalNode
def create_node(aStr):
    return UnidirectionalNode(aStr)
def create_bi_node(aStr):
    return BidirectionalNode(aStr)

def main():
    # test_single_linked_list()ct()
    # test_double_linked_list_sort()
    # test_double_linked_list_swap()
    # test_double_linked_list_reverse()
    # test_double_linked_list()
    # test_double_linked_list_objec
#    test_single_linked_list_traverse()
    test_single_linked_list_getat()

def test_double_linked_list_object():
    ll = DoublyLinkedList()
    one = create_bi_node({"name": "James", "email": "james@gmail.com" })
    ll.append(one)
    two = create_bi_node("2")
    ll.append(two)
    one_dot_one = create_bi_node("1.1")
    ll.insert_at(1, one_dot_one)
    zero_dot_one = create_bi_node("0.1")
    ll.insert_at(0, zero_dot_one)
    zero_dot_zero_one = create_bi_node("0.01")
    ll.insert_at_head(zero_dot_zero_one)
#    ll.sort()
    print(ll)

def test_double_linked_list_sort():
    ll = DoublyLinkedList()
    four = create_bi_node("4")
    ll.append(four)
    two = create_bi_node("2")
    ll.append(two)
    one = create_bi_node("1")
    ll.append(one)
    three = create_bi_node("3")
    ll.append(three)
    ll.sort()
    print(ll)

def test_double_linked_list_swap():
    ll = DoublyLinkedList()
    four = create_bi_node("4")
    ll.append(four)
    two = create_bi_node("2")
    ll.append(two)
    one = create_bi_node("1")
    ll.append(one)
    three = create_bi_node("3")
    ll.append(three)
    five = create_bi_node("5")
    ll.append(five)
    ll.swap(two, three)
    print(ll)

def test_double_linked_list_reverse():
    ll = DoublyLinkedList()
    four = create_bi_node("4")
    ll.append(four)
    two = create_bi_node("2")
    ll.append(two)
    one = create_bi_node("1")
    ll.append(one)
    three = create_bi_node("3")
    ll.append(three)
    five = create_bi_node("5")
    ll.append(five)
    ll.reverse()
    print(ll)

def test_double_linked_list():
    ll = DoublyLinkedList()
    one = create_bi_node("1")
    ll.append(one)
    two = create_bi_node("2")
    ll.append(two)
    one_dot_one = create_bi_node("1.1")
    ll.insert_at(3, one_dot_one)
    zero_dot_one = create_bi_node("0.1")
    ll.insert_at(0, zero_dot_one)
    zero_dot_zero_one = create_bi_node("0.01")
    ll.insert_at_head(zero_dot_zero_one)

    ll.delete_at(5)

    print(ll)

def test_single_linked_list():
    linked_list: SinglyLinkedList = SinglyLinkedList()
    one = create_node("1")
    linked_list.append(one)
    linked_list.append(create_node("2"))
    linked_list.append(create_node("4"))
    head = create_node("0")
    linked_list.insert_at(0, head)
    three = create_node("3")
    linked_list.insert_at(3, three)
    linked_list.insert_at(5, create_node("5"))
    tail = create_node("6")
    linked_list.insert_at(8, tail)
    linked_list.append(three)
    linked_list.insert_at(0, three)

    linked_list.swap(three, head)
    linked_list.sort()
    print(linked_list)

def test_single_linked_list_getat():
    linked_list: SinglyLinkedList = SinglyLinkedList()
    one = create_node("1")
    linked_list.append(one)
    linked_list.append(create_node("2"))
    linked_list.append(create_node("4"))
    node_two = linked_list.get_at(1)
    print(f"Node at index 1: {node_two}")

def test_single_linked_list_traverse():
    linked_list: SinglyLinkedList = SinglyLinkedList()
    one = create_node("1")
    linked_list.append(one)
    linked_list.append(create_node("2"))
    linked_list.append(create_node("4"))

    # while linked_list.hasNext():
    #     print(linked_list.next().data)

if __name__ == '__main__':
    main()