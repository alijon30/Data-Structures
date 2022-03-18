
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode ==  self.tail:
                    self.tail = newNode
    def traverse(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def search(self, nodeValue):
        if self.head is None:
            print("The Linked List is empty")
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The Node value does not exist in SSL"

    def delete(self, location):
        if self.head is None:
            return "The SSL is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index += 1

                nextnode = tempnode.next
                tempnode.next = nextnode.next
                
