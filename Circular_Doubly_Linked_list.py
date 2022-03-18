
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, Nodevalue):
        newNode = Node(Nodevalue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The Circular Doubly linked list is created"

    def insert(self, NodeValue, location):
        if self.head is None:
            return "The CDOubly has not been created"
        else:
            newNode = Node(NodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next =  newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                newNode.next = tempnode.next
                newNode.prev = tempnode
                newNode.next.prev = newNode
                tempnode.next = newNode
            return "The Node has been inserted"

    def traversal(self):
        if self.head is None:
            return "The Circular does not exist"
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break


    def ReverseTraversal(self):
        if self.head is None:
            return "The CIrcular does not exist"
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev


    def search(self, NodeValue):
        if self.head is None:
            return "The CDL is empty"
        else:
            node = self.head
            while node:
                if node.value == NodeValue:
                    return node.value
                if node == self.tail:
                    return "The Node value does not exist"
                node = node.next

    def delete(self, location):
        if self.head is None:
            return "The DLS is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                node = self.head
                index = 0
                while index < location -1:
                    node = node.next
                    index += 1
                node.next = node.next.next
                node.next.prev = node
            print("Node has been successfully deleted")
