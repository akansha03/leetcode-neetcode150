"""
Problem: [Task Scheduler]
Link: https://leetcode.com/problems/task-scheduler/description/
Difficulty: [Medium]
Topics: [Max Heap, Priority Queue]

Pattern: []
Key Insight: []

Time Complexity: O(nlogn)
Space Complexity: O()

Solved: [07/04/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
from heapq import heappush, heappop, heapify
from collections import Counter, deque
class Solution(object):
    def leastInterval(self, tasks, n):
        # Step 1: Get the frequency of all the tasks and store it in a max heap
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapify(maxHeap)

        # Declare a queue to keep check on the non utilised tasks along with the time gap
        time = 0
        queue = deque()
        while maxHeap or queue:
            time += 1
            if not maxHeap:
                time = queue[0][1]
            else:
                counter = 1 + heappop(maxHeap)
                if counter:
                    queue.append([counter, time+n])
            if queue and time == queue[0][1]:
                heappush(maxHeap, queue.popleft()[0])
        return time

if __name__ == "__main__":
    sol = Solution()
    assert sol.leastInterval(["A","A","A","B","B","B"], 2) == 8
    assert sol.leastInterval(["A","C","A","B","D","B"], 1) == 6
    assert sol.leastInterval(["A","A","A", "B","B","B"], 3) == 10
    print("✅ All tests passed!")