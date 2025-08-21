from singly_linked_list import LinkedList
from my_nodes import UnidirectionalNode
def create_node(aStr):
    return UnidirectionalNode(aStr)

def main():
    linked_list: LinkedList = LinkedList()
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
    print(linked_list)
    linked_list.sort()
    print(linked_list)

if __name__ == '__main__':
    main()