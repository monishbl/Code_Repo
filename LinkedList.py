class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None


list = LinkedList()

while True:
    print("1. Append")
    print("2. Prepend")
    print("3. Insert After Node")
    print("4. Delete Node")
    print("5. Delete Node at Position")
    print("6. Print List")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = input("Enter data: ")
        list.append(data)
    elif choice == 2:
        data = input("Enter data: ")
        list.prepend(data)
    elif choice == 3:
        data = input("Enter data: ")
        prev_node = input("Enter previous node: ")
        list.insert_after_node(prev_node, data)
    elif choice == 4:
        data = input("Enter data: ")
        list.delete_node(data)
    elif choice == 5:
        pos = int(input("Enter position: "))
        list.delete_node_at_pos(pos)
    elif choice == 6:
        print("Current List: ")
        list.print_list()
    elif choice == 7:
        break
    else:
        print("Invalid choice")
        
    print()