from singly_linked_list import LinkedList
from my_nodes import UnidirectionNode
def create_node(str):
    return UnidirectionNode(str)

def main():
    linkedList = LinkedList()
    one = create_node("1")
    linkedList.append(one)
    linkedList.append(create_node("2"))
    linkedList.append(create_node("4"))
    head = create_node("0")
    linkedList.insert_at(0, head)
    three = create_node("3")
    linkedList.insert_at(3, three)
    linkedList.insert_at(5, create_node("5"))
    tail = create_node("6")
    linkedList.insert_at(8, tail)
    linkedList.append(three)
    linkedList.insert_at(0, three)

    linkedList.swap(three, head)
    print(linkedList)
    linkedList.sort()
    print(linkedList)

if __name__ == '__main__':
    main()