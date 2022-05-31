class LinkedList:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def insert(self, element, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(element, next_node=node)

        return element

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node
        i = 0
        node = self.head
        prev_node = node

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element
        del node

        return element

    def get(self, index):
        i = 0
        node = self.head

        while i < index:
            node = node.next_node
            i += 1

        return node

    def get_length(self):
        if not self.head:
            return 0

        i = 1
        node = self.head
        while node.next_node:
            i+=1
            node = node.next_node

        return i


linked_list = LinkedList()
print('-------------')
linked_list.append(10)
linked_list.append(7)
linked_list.append(5)
print('---------добавили 10 7 5----')
linked_list.out()
print('length=',linked_list.get_length())
linked_list.delete(1)
print('-------- и удалили 1 -----')
linked_list.out()
print('length=',linked_list.get_length())
linked_list.insert(8, 1)
print('------ и вставили 8,1  -------')
linked_list.out()
print('length=',linked_list.get_length())