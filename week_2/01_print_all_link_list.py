class Node:
    def __init__(self, data):  # construct
        self.data = data
        self.next = None


node = Node(3)
# print(node.data)
first_node = Node(4)
node.next = first_node

# print(node.next.data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        # self.head.next = Node(data)  # 헤드의 뒤쪽에 붙이는것
        cur = self.head
        print("cur is", cur.data)
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        print("hihihi")

        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


Linked_list = LinkedList(3)
Linked_list.append(4)
# print(Linked_list.head.next)
