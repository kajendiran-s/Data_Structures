#creating node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating linkedlist
class llist():

    #creating head node for the object
    def __init__(self):
        self.head = None
    
    #inserting at the begining
    def insetAtBeg(self,data):
        temp = Node(data)
        
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head.next
            self.head = temp
        
    #inserting at the end
    def insertAtEnd(self,data):
        temp = Node(data)

        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = temp
    
    #inserting at the givenposition
    def insertAtPos(self,data,pos):
        
        try:
            temp = Node(data)
            count = 1

            if self.head == None:
                self.head = temp

            else:
                curr = self.head
                while count < pos-1 and curr != None:
                    curr = curr.next
                    count += 1
                temp.next = curr.next
                curr.next = temp
        except Exception as e:
            print("Index out of range")

    #delete from begining
    def delAtBeg(self):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                temp = self.head
                self.head = self.head.next
                del temp
        except Exception as e:
            print(str(e))

    #delete from end
    def delAtEnd(self):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                prev = None
                curr = self.head
                while curr.next != None:
                    prev = curr
                    curr = curr.next
                prev.next = None
                del curr
        except Exception as e:
            print(str(e))
        
    #delete at given index
    def delAtPos(self,pos):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                count = 1
                curr = self.head
                while count < pos-1 and curr != None:
                    curr = curr.next
                    count += 1
                temp = curr.next
                curr.next = temp.next
                del temp
        except Exception as e:
            print(str(e))
    
    #traversing the linked list
    def traverse(self):
        curr = self.head
        
        while True:
            print(curr.data,"->")
            if curr.next == None:
                break
            curr = curr.next

    #length of the linked list
    def length(self,node):
        if node == None:
            return 0
        else:
            return  1 + self.length(node.next)





ele = llist()


while(True):
    print("Press\n1.Insert the node at the begining\n2.Insert the node at the given position\n3.Insert the node at the end\n4. Delete a node at starting\n5.Delete a node at the given position\n6.Delete a node at ending\n7.Traverse the list\n8.Length of the Linked List")
    option = int(input("Enter your option:\n"))

    match option:
        case 1: 
            data = int(input("Enter your data:\n"))
            ele.insetAtBeg(data)

        case 2:
            data = int(input("Enter your data:\n"))
            pos = int(input("Enter the position:\n"))
            ele.insertAtPos(data,pos)
            
        
        case 3:
            data = int(input("Enter you data:\n"))
            ele.insertAtEnd(data)

        case 4:
            ele.delAtBeg()
        
        case 5:
            pos = int(input("Enter the position to delete\n"))
            ele.delAtPos(pos)

        case 6:
            ele.delAtEnd()

        case 7:
            ele.traverse()

        case 8:
            if ele.head != None:
                print(ele.length(ele.head))
            else:
                print("Empty List")
        
    print("If you want to continue Press anything other than 0:")
    cont = input()

    if cont == 0:
        break