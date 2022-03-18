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

    def createDLL(self, NodeValue):
        node = Node(NodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

    def insertDLL(self, nodeValue, location):
        if self.head is None:
            return "The DLL is not created yet"
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0
                node = self.head
                while index < location -1:
                    node = node.next
                    index += 1

                newNode.next = node.next
                newNode.prev = node
                newNode.next.prev = newNode
                node.next = newNode
    def traversal(self):
        if self.head is None:
            print("The DLL is empty")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def ReverseTraversal(self):
        if self.head is None:
            print("The DLL is empty")
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev

    def searchDLL(self, NodeValue):
        if self.head is None:
            return "The DLL does not exist"
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == NodeValue:
                    return tempnode.value
                tempnode = tempnode.next
            return "THE Node Value does not exist"


    def deleteNode(self, location):
        if self.head is None:
            return "The DLL does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("Node has been successfully deleted")
