"""
Problem: [LRU Cache]
Link: https://leetcode.com/problems/lru-cache/
Difficulty: [Medium]
Topics: [Array, Hash Table, Doubly Linked List]

Pattern: [Doubly Linked List, HashTable, Least Recently Used]

Key Insight:

* This problem is designing the LRU cache, from the description - it looks pretty straight forward, get the value using key
and put the key and value in the cache. This could be achieved using dictionary data structure.

* However, we have to implement the eviction policy - lru where least recently used element is popped from the cache and new
one is added.

* To implement this we will be using doubly linked list where most recently used elements like add or get will be appended
to the end of the list so that the least recently used item is at the beginning.

* We will be using 2 dummy nodes for extreme left and extreme right for quick insertion and removal.

* Anytime cache size is more than the capacity then top node should be removed.

Time Complexity: O(1)
Space Complexity: O(capacity)

Solved: [02/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.left = self.right = Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev, node.next = prev, self.right

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        node.next = node.prev = None

    def get(self, key):
       if key in self.cache:
            value = self.cache[key]
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return value.val
       return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)

if __name__ == "__main__":
    operations = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
    inputs = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    outputs = [None, None, 1, None, -1, None, -1, 3, 4]
    sol = LRUCache(2)
    for index, operation in enumerate(operations):
        if operation == "put":
            assert sol.put(inputs[index][0], inputs[index][1]) == outputs[index]
        else:
            assert sol.get(inputs[index][0]) == outputs[index]
    print("✅ All tests passed!")