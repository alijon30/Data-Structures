class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class Circular:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node ==  self.tail.next:
                break


    def createCLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular singly linked list has been created"

    def insertCLL(self, nodeValue, location):
        if self.head is None:
            return "FUCK UP"
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextNode = tempnode.next
                tempnode.next = newNode
                newNode.next = nextNode

    def traverse(self):
        if self.head is None:
            return "The CLL is empty"
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    def search(self, nodeValue):
        if self.head is None:
            return "The CCL is empty"
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodeValue:
                    return tempnode.value
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    return "The Nodevalue does not exist in the CLL"
    def delete(self, location):
        if self.head is None:
            return "The CLL is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempnode = self.head
                index = 0
                while index< location -1:
                    tempnode = tempnode.next
                    index += 1
                nextNode = tempnode.next
                tempnode.next = nextNode.next

