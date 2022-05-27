class LinkedList:
    head = None
    length = 1

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
        self.length += 1

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def insert(self, element, index):
      i=0
      node = self.head
      prev_node = self.head

      while i < index:
        prev_node = node
        node = node.next_node
        i+=1

      prev_node.next_node = self.Node(element, next_node=node)
      self.length += 1

      return element

    def delete(self, index):
      i = 0
      node = self.head
      prev_node = self.head

      while i < index:
        prev_node = node
        node = node.next_node
        i += 1

      prev_node = node.next_node
      self.length -= 1

      del node

      return element

    def get(self, index):
      i=0
      node = self.head

      while i < index:
        node = node.next_node
        i+=1

        return node

linked_list = LinkedList()
print('-------------')
linked_list.append(10)
linked_list.append(7)
linked_list.append(5)
linked_list.append(3)
linked_list.insert(5,1)

linked_list.out()
print('len=',linked_list.length)