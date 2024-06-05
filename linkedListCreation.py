class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def toString(self):
        return "Name: " + self.name + ", CGPA: " + str(self.cgpa)


class Node:
    def __init__(self, student, next=None, pre=None):
        self.data = student
        self.next = next
        self.pre = pre


class LinkedList:
    def __init__(self):
        self.front = None  # Points to the first node
        self.back = None   # Points to the last node
    
    def push_front(self, data):
        node = Node(data, self.front)
        if self.front is None:
            self.back = node  # If the list is empty, set both front and back to the new node
        else:
            self.front.pre = node
        self.front = node

    def push_back(self, data):
        node = Node(data, None, self.back)
        if self.back is None:
            self.front = node  # If the list is empty, set both front and back to the new node
        else:
            self.back.next = node
        self.back = node
    
    def pop_front(self):
        if self.front is None:
            print("List is Empty")
            return
        elif self.front == self.back:
            rm = self.front
            self.front = self.back = None
            del rm
        else:
            rm = self.front
            self.front = self.front.next
            self.front.pre = None
            del rm
    
    def display_front(self):
        current = self.front
        while current is not None:
            print(current.data.toString())
            current = current.next

    def display_back(self):
        current = self.back
        while current is not None:
            print(current.data.toString())
            current = current.pre


# Example usage
lst = LinkedList()
lst.push_front(Student("John", 3.5))
lst.push_front(Student("Bill", 3.5))
lst.push_front(Student("Steve", 3.5))
lst.pop_front()


print("\nDisplay from back:")
lst.display_back()
print("Display from front:")
lst.display_front()
