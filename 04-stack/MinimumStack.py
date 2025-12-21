"""
Problem: [Minimum Stack]
Link: https://leetcode.com/problems/min-stack/
Difficulty: [Medium]
Topics: [Stack - 2 stacks]

Pattern: [Get 2 stacks - one which is normal and second which stores a minimum value on top]

Key Insight:
* Get 2 stacks - normal stack and second one which stores the minimum element.

* Push all the elements in the first stack and in the second one add only if the new value is less than
the top element.

* Pop the top element on the stack and if it's a top element of the min_stack then pop it too as well.

* To get the top element, return the last element inserted in the stack and to get the minimum element

Time Complexity: O(n) - push + O(1) - pop + O(1) - top + O(1) - get min
Space Complexity: O(n)

Solved: [7/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if self.min_stack[-1] == value:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]

if __name__ == "__main__":
    sol = MinStack()
    operations = ["push","push","push","getMin","pop","top","getMin"]
    inputVal = [-2,0,-3,None,None,None,None]
    output = [None,None,None,-3,None,0,-2]
    for i, op in enumerate(operations):
        if op == "push":
            sol.push(inputVal[i])
        elif op == "pop":
            sol.pop()
        elif op == "top":
            assert sol.top() == output[i]
        else:
            assert sol.getMin() == output[i]

    print("✅ All tests passed!")