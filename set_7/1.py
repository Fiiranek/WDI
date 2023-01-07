class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"Node(val={self.val} next={self.next})"


class Set:
    def __init__(self):
        self.head = None

    def insert(self, new_val):
        new_node = Node(new_val)
        if self.head:
            current = self.head
            while current.next:
                if current.val == new_val or current.next.val == new_val:  # duplicate check
                    return
                if current.next.val > new_val > current.val:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print("\n--------")

    def delete(self, del_val):
        if not self.head:
            return
        current = self.head
        prev = None
        while current:
            if current.val == del_val:
                if prev:
                    prev.next = current.next
                else:
                    self.head = None
            prev = current
            current = current.next

    def contains(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False


c = Set()

c.insert(1)
c.insert(3)
c.insert(1)
c.insert(3)
c.insert(2)
c.print()
print(c.contains(2))
c.delete(2)
c.print()
print(c.contains(2))


