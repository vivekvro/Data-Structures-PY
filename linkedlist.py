from typing import Literal

class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def __repr__(self):
        pass
    def __contains__(self,value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False
    def __len__(self):
        current = self.head
        counter = 0
        while current:
            counter+=1
            current=current.next
        return counter
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def prepend(self,value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node
    def insert(self,value,index):
        if index == 0:
            self.prepend(value)
        else:
            current = self.head
            for i in range(index-1):
                if current.next is None:
                    raise ValueError("Index out of bounds")
                current = current.next
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node

    def delete(self,value):
        current = self.head
        prev = None
        if current and current.value==value:
            print("value deleted")
            self.head = current.next
            return
        
        while current and current.value!=value:
            prev = current
            current = current.next
        if not current:
            print("value not found")
        
        prev.next = current.next
        
        print("value deleted")


    def pop_by_index(self, index:int=-1):
        if not isinstance(index,int):
            print("index must be a number")
        if not self.head:
            print("list is empty")
            return
        length =  len(self)
        if index <0:
            index = length + index
        if index < 0 or index >= length:
            raise IndexError("Index out of range")

        current = self.head
        counter = 0

        value = None
        if index==0:
            value = current.value
            self.head = current.next
            return value
        for _ in range(index-1):
            current = current.next
        popped_node = current.next
        current.next = popped_node.next
        return popped_node.value
    def pop_by_side(self,side=Literal["left","right"]):
        if not self.head:
            print("list is empty")
            return
        if side=="left":
            popped_node = self.head
            self.head = self.head.next if self.head.next else None
            return popped_node.value
        elif side=="right":
            if self.head.next is not None:
                popped_node = self.head
                self.head = None
                return popped_node
            current = self.head
            while current.next.next:
                current = current.next
            popped_node = current.next
            current.next = None
            return popped_node.value


    def __getitem__(self, index=-1):
        if not self.head:
            print("list is empty")
            return
        length =  len(self)
        if index <0:
            index = length + index
        if index < 0 or index >= length:
            raise IndexError("Index out of range")
        if index == 0:
            return self.head.value
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __str__(self)->str:
        if not self.head:
            return "list is empty"
            
        ll_str = ""
        current = self.head
        while current:
            ll_str = ll_str +str(current.value) + " -> "
            current = current.next
        ll_str = ll_str + "None"
        return ll_str




prompt  = """
Select LinkedList Operations:
-----------------------------------
    - to init Linkedlist enter: "init"
    - to Display enter: "display"
    - to Append enter: "append"
    - to Delete an element enter: "delete"
    - to Insert an element at specific index enter : "insert"
    - to Pop an element out of LL enter : "pop"
    - to get element by index enter: "get"
    - to get the length enter : "len"
    """




linked_list = None
def init_ll():
    global linked_list
    linked_list = LinkedList()
def display_ll():
    try:
        print(linked_list)
    except:
        print("first init the linked list")
def append_ll():
    try:
        value = int(input("Enter Value: "))
        linked_list.append(value)
        print( "appended")
        print(linked_list)
    except:
        print("first init the linked list")
def pop_ll(iter:int=0):
    if iter>0:
        print("wrong input.\n (try again)")
    try:
        pop_by = str(input("pop element by side or index? : ")).lower().strip()
        if pop_by == "side":
            side = str(input("select POP side-> left or right ?: ")).lower().strip()
            if side not in["left","right"]:
                pop_ll(1)
                return
            value = linked_list.pop_by_side(side=side)
            print("popped: ",value)
            print(linked_list)
            return
        elif pop_by=="index":
            index = int(input("enter index: "))
            value = linked_list.pop_by_index(index=index)
            print("popped: ",value)
            print(linked_list)
            return
        else:
            pop_ll(1)
            return
    except:
        print("first init the linked list")

def delete_ll():
    value = int(input("enter the value you want to delete"))
    try:
        linked_list.delete(value)
        print("element deleted")
        print(linked_list)
    except ValueError as e:
        print(str(e))
    except:
        print("first init the linked list")





operations_list = ["init","display","append","delete","insert","pop","get","len"]
operations_dict = {
    "init":init_ll,
    "display":display_ll,
    "append":append_ll,
    "delete":delete_ll,
    "insert":1,
    "pop":pop_ll,
    "get":1,
    "len":1
}





if __name__=="__main__":
    
    while True:
        print(prompt)
        user_input = input("\nEnter here: ")
        user_input = user_input.lower().strip()
        if user_input in ["/exit","/bye","/quit"]:
            break
        if user_input in operations_dict:
            operations_dict[user_input]
        else:
            print("Sry. no extra Conversation")

        

