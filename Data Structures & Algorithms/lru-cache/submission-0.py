class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

class LRUCache:
    # approach
    # create hashmap for cache
    # create doubly link list to store values
    # add add funtion in link list
    # add remove funtion in link list
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} 
        self.left = Node(0, 0) # next will be LRU
        self.right = Node(0, 0) # prev will be MRU
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            existing_node = self.cache[key]
            answer = existing_node.value
            self.remove(existing_node)
            self.add(existing_node)
        else:
            answer = -1
        return answer

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            existing_node = self.cache[key]
            self.remove(existing_node)
            existing_node.value = value
            self.add(existing_node)
            # new_node = Node(key, value)
            # self.cache[key] = new_node
            # self.add(new_node)
        else:
            if len(self.cache) < self.cap:
                new_node = Node(key, value)
                self.cache[key] = new_node
                self.add(new_node)
            else:
                lru = self.left.next
                del self.cache[lru.key]
                self.remove(lru)
                new_node = Node(key, value)
                self.cache[key] = new_node
                self.add(new_node)



